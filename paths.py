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

Usage in any script or notebook:
  import pandas as pd
  from paths import PLAYERS_FULL
  players = pd.read_parquet(PLAYERS_FULL)

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

DATA_DICT = DATA_DIR / "data_dictionary.csv"

# full/
PLAYERS_FULL = DATA_DIR / "full" / "players_full.parquet"
TEAMS_FULL = DATA_DIR / "full" / "teams_full.parquet"

# clean/
PLAYERS = DATA_DIR / "clean" / "players.csv"
TEAMS = DATA_DIR / "clean" / "teams.csv"
CONFERENCES = DATA_DIR / "clean" / "conferences.csv"
TRANSFERS = DATA_DIR / "clean" / "transfers.csv"

# raw/
RAW_BACKUP = DATA_DIR / "raw" / "cbb_raw_backup.zip"

ALL_FILES = {
  "DATA_DICT": DATA_DICT,
  "PLAYERS_FULL": PLAYERS_FULL,
  "TEAMS_FULL": TEAMS_FULL,
  "PLAYERS": PLAYERS,
  "TEAMS": TEAMS,
  "CONFERENCES": CONFERENCES,
  "TRANSFERS": TRANSFERS,
  "RAW_BACKUP": RAW_BACKUP,
}


def check():
  """Print whether every expected data file is found."""
  print(f"DATA_DIR: {DATA_DIR}\n")
  ok = True
  for name, path in ALL_FILES.items():
    found = path.exists()
    ok = ok and found
    status = "OK     " if found else "MISSING"
    print(f"  {status} {name:<20} {path.relative_to(DATA_DIR)}")
  print("\nAll files found." if ok else "\nSome files are missing, check DATA_DIR.")


if __name__ == "__main__":
  check()
