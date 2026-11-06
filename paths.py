r"""
paths.py
Central place for data locations in the DSC180A-D15 repo.
Each person points this at their own copy of the shared data folder,
so no one's local path ends up on GitHub.

Set your data folder ONE of two ways:
  1. Create local_paths.py in the repo root (it is gitignored) containing:
       DATA_DIR = r"C:\path\to\shared\data\folder"
     (copy local_paths.example.py and edit it)
  2. Set the environment variable CAPSTONE_DATA_DIR

All data files live directly in DATA_DIR (no subfolders).

Usage in any script or notebook:
  import pandas as pd
  from paths import PLAYERS_FULL
  players = pd.read_csv(PLAYERS_FULL)   # pandas handles .gz automatically

Notebooks in a subfolder (e.g. notebooks/) need the repo root on the path first:
  import sys; sys.path.insert(0, "..")
  from paths import PLAYERS_FULL
"""

import os
import runpy
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent


def _find_data_dir():
  env = os.environ.get("CAPSTONE_DATA_DIR")
  if env:
    return Path(env)

  local_file = REPO_ROOT / "local_paths.py"
  if local_file.exists():
    settings = runpy.run_path(str(local_file))
    if "DATA_DIR" in settings:
      return Path(settings["DATA_DIR"])

  raise RuntimeError(
    "Data folder not set. Copy local_paths.example.py to local_paths.py "
    "in the repo root and set DATA_DIR, or set CAPSTONE_DATA_DIR."
  )


DATA_DIR = _find_data_dir()

if not DATA_DIR.exists():
  raise FileNotFoundError(f"DATA_DIR does not exist: {DATA_DIR}")


def _glob_one(pattern, fallback):
  """Resolve a file whose exact name may vary (e.g. season suffix)."""
  matches = sorted(DATA_DIR.glob(pattern))
  return matches[0] if matches else DATA_DIR / fallback


# Reference
DATA_DICT = DATA_DIR / "data_dictionary.csv"
README = DATA_DIR / "README.md"
CONFERENCES = DATA_DIR / "conferences.csv"
TRANSFERS = DATA_DIR / "transfers.csv"

# Players
PLAYERS = DATA_DIR / "players.csv"
PLAYERS_FULL = DATA_DIR / "players_full.csv.gz"
PLAYERS_CONF_ONLY = DATA_DIR / "players_conference_only.csv"
PLAYERS_PBP_CONF_ONLY = _glob_one(
  "players_pbp_conference*.csv",
  "players_pbp_conference_only_25_26_INCOMPLETE.csv",
)

# Teams
TEAMS = DATA_DIR / "teams.csv"
TEAMS_FULL = DATA_DIR / "teams_full.csv"
TEAMS_CONF_ONLY = DATA_DIR / "teams_conference_only.csv"
TEAMS_PBP_CONF_ONLY = DATA_DIR / "teams_pbp_conference_only.csv"
TEAM_POSSESSION_TYPES = DATA_DIR / "team_possession_types.csv"

# Game level
GAMES = DATA_DIR / "games.csv.gz"
TEAM_GAMES = DATA_DIR / "team_games.csv.gz"
PLAYER_GAMES = DATA_DIR / "player_games.csv.gz"
LINEUPS = DATA_DIR / "lineups.csv.gz"

ALL_FILES = {
  "DATA_DICT": DATA_DICT,
  "README": README,
  "CONFERENCES": CONFERENCES,
  "TRANSFERS": TRANSFERS,
  "PLAYERS": PLAYERS,
  "PLAYERS_FULL": PLAYERS_FULL,
  "PLAYERS_CONF_ONLY": PLAYERS_CONF_ONLY,
  "PLAYERS_PBP_CONF_ONLY": PLAYERS_PBP_CONF_ONLY,
  "TEAMS": TEAMS,
  "TEAMS_FULL": TEAMS_FULL,
  "TEAMS_CONF_ONLY": TEAMS_CONF_ONLY,
  "TEAMS_PBP_CONF_ONLY": TEAMS_PBP_CONF_ONLY,
  "TEAM_POSSESSION_TYPES": TEAM_POSSESSION_TYPES,
  "GAMES": GAMES,
  "TEAM_GAMES": TEAM_GAMES,
  "PLAYER_GAMES": PLAYER_GAMES,
  "LINEUPS": LINEUPS,
}


def check():
  """Print whether every expected data file is found."""
  print(f"DATA_DIR: {DATA_DIR}\n")
  ok = True
  for name, path in ALL_FILES.items():
    found = path.exists()
    ok = ok and found
    status = "OK     " if found else "MISSING"
    print(f"  {status} {name:<24} {path.name}")
  print("\nAll files found." if ok else "\nSome files are missing, check DATA_DIR.")


if __name__ == "__main__":
  check()