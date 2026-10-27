r"""
paths.py
Central place for data locations in the DSC180A-D15 repo.
Each person points this at their own copy of the shared "CBB Analytics Data"
folder, so no one's local path ends up on GitHub.

Set your data folder ONE of two ways:
  1. Create local_paths.py in the repo root (it is gitignored) containing:
       DATA_DIR = r"C:\path\to\CBB Analytics Data"
     (copy local_paths.example.py and edit it)
  2. Set the environment variable CAPSTONE_DATA_DIR

Usage in any script or notebook:
  from paths import load, PLAYERS_FULL
  players = load(PLAYERS_FULL)          # or load("players_full")

Notebooks in a subfolder (e.g. notebooks/) need the repo root on the path first:
  import sys; sys.path.insert(0, "..")
  from paths import load

Check that every file is found:
  python paths.py
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
  raise FileNotFoundError(
    f"DATA_DIR does not exist: {DATA_DIR}\n"
    "Check the path in local_paths.py (it should be the folder containing README.md)."
  )


def _find(stem):
  """Large tables are compressed (.csv.gz), small ones are plain .csv. Return whichever exists."""
  for ext in (".csv", ".csv.gz"):
    path = DATA_DIR / f"{stem}{ext}"
    if path.exists():
      return path
  return DATA_DIR / f"{stem}.csv"  # reported as MISSING by check()


# Reference
README = DATA_DIR / "README.md"
DATA_DICT = DATA_DIR / "data_dictionary.csv"

# Season level, all 8 seasons (2018-19 to 2025-26)
PLAYERS = _find("players")                        # player-season, 65 curated columns
PLAYERS_FULL = _find("players_full")              # player-season, all 881 columns
TEAMS = _find("teams")                            # team-season, 30 curated columns
TEAMS_FULL = _find("teams_full")                  # team-season, all 1,187 columns
CONFERENCES = _find("conferences")                # conference strength, rank, tier (+ 2026-27)

# Conference games only, all 8 seasons
PLAYERS_CONF = _find("players_conference_only")
TEAMS_CONF = _find("teams_conference_only")
TEAMS_PBP_CONF = _find("teams_pbp_conference_only")

# Playstyle
POSSESSION_TYPES = _find("team_possession_types")  # long format: team x side x possession type/length
LINEUPS = _find("lineups")                         # 5-man lineups, 2023-24 to 2025-26

# Game level
GAMES = _find("games")                            # one row per game, all 8 seasons
TEAM_GAMES = _find("team_games")                  # one row per team per game, all 8 seasons
PLAYER_GAMES = _find("player_games")              # one row per player per game, 2023-24 to 2025-26

# Transfers
TRANSFERS = _find("transfers")                    # before/after stats for every transfer

# Optional: not everyone needs these, and check() won't flag them as missing
PROJECTIONS_2026_27 = _find("projections_2026_27")
PLAYERS_PBP_CONF_2025_26_INCOMPLETE = _find("players_pbp_conference_only_2025_26_INCOMPLETE")

ALL_FILES = {
  "README": README,
  "DATA_DICT": DATA_DICT,
  "PLAYERS": PLAYERS,
  "PLAYERS_FULL": PLAYERS_FULL,
  "TEAMS": TEAMS,
  "TEAMS_FULL": TEAMS_FULL,
  "CONFERENCES": CONFERENCES,
  "PLAYERS_CONF": PLAYERS_CONF,
  "TEAMS_CONF": TEAMS_CONF,
  "TEAMS_PBP_CONF": TEAMS_PBP_CONF,
  "POSSESSION_TYPES": POSSESSION_TYPES,
  "LINEUPS": LINEUPS,
  "GAMES": GAMES,
  "TEAM_GAMES": TEAM_GAMES,
  "PLAYER_GAMES": PLAYER_GAMES,
  "TRANSFERS": TRANSFERS,
}

OPTIONAL_FILES = {
  "PROJECTIONS_2026_27": PROJECTIONS_2026_27,
  "PLAYERS_PBP_CONF_2025_26_INCOMPLETE": PLAYERS_PBP_CONF_2025_26_INCOMPLETE,
}


def load(name_or_path, **kwargs):
  """Load a table as a DataFrame. Accepts a path constant or a file stem:
    load(PLAYERS_FULL)   or   load("players_full")
  Works for both .csv and .csv.gz."""
  import pandas as pd
  path = Path(name_or_path) if isinstance(name_or_path, Path) else _find(str(name_or_path))
  if not path.exists():
    raise FileNotFoundError(f"{path} not found. Run: python paths.py")
  kwargs.setdefault("low_memory", False)
  return pd.read_csv(path, **kwargs)


def check():
  """Print whether every expected data file is found."""
  print(f"DATA_DIR: {DATA_DIR}\n")
  ok = True
  for name, path in ALL_FILES.items():
    found = path.exists()
    ok = ok and found
    status = "OK     " if found else "MISSING"
    size = f"{path.stat().st_size / 1e6:8.1f} MB" if found else ""
    print(f"  {status} {name:<20} {path.name:<45} {size}")
  print("\n  Optional:")
  for name, path in OPTIONAL_FILES.items():
    status = "OK     " if path.exists() else "not present"
    print(f"  {status} {name:<20} {path.name}")
  print("\nAll required files found." if ok else "\nSome files are missing, check DATA_DIR.")


if __name__ == "__main__":
  check()
