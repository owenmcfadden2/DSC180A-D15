"""
player_prep.py

Shared data preparation for the player archetype work. Both notebooks import
from here, so the sample filters and feature definitions live in one place.

Usage (from a notebook in notebooks/):
  import sys
  from pathlib import Path
  sys.path.insert(0, str(Path.cwd().parent))
  import player_prep as prep

  pf = prep.load_filtered_players()
  feat, ids = prep.build_style_features(pf)

Decisions behind each setting are documented in the Notes section of
notebooks/01_player_archetypes_eda.ipynb.
"""
import numpy as np
import pandas as pd

import paths

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
MIN_TOTAL_COL = "Min"       # season total minutes
MIN_PG_COL = "Min/G"        # minutes per game
GP_COL = "G"                # games played
FGA_COL = "FGA"             # season total field goal attempts
ID_COLS = ["Player ID", "Season"]

MIN_MINUTES = 250                        # default minimum minutes in a season
SEASON_MIN_MINUTES = {"2020-21": 200}    # shortened COVID season
LIMITED_GAMES_MIN_G = 8                  # limited-games rule: minimum games...
LIMITED_GAMES_MIN_MPG = 25               # ...at this many minutes per game
DROP_SEASONS = ["2018-19"]               # incomplete play-by-play tagging, old 3P line
LOW_FGA = 50                             # flag: zone shares are noisy below this
LOW_COV = 0.8                            # flag: share of plays with play-by-play tagging

BASIC5 = ["Rim Shot %", "Paint Shot %", "Midrange Shot %",
          "Corner 3 Shot %", "Above Break 3 Shot %"]
ZONE_AST = ["Rim Ast", "Paint Ast", "Midrange Ast", "Corner 3 Ast", "Above Break 3 Ast"]
ROLE_COLS = ["Usage %", "Ast %", "TO %", "OReb %", "DReb %", "Stl %", "Blk %",
             "FT Rate", "PF %", "Self OReb Share", "Blocked Per FGA"]

# Helper columns added below; excluded when treating pf as raw data
HELPER_COLS = ["make_tag_cov", "ast_tag_cov"]
FLAG_COLS = ["low_fga", "low_coverage", "keep_reason"]


# ---------------------------------------------------------------------------
# Sample filters
# ---------------------------------------------------------------------------
def load_filtered_players(players_full=None, verbose=True):
  """
  Load players_full and apply the agreed sample filters.

  Returns one row per player-season, with three added columns:
    keep_reason   "minutes", "covid_threshold", or "limited_games"
    low_fga       fewer than LOW_FGA field goal attempts
    low_coverage  under LOW_COV of makes or assists tagged in play-by-play
  """
  if players_full is None:
    players_full = paths.load(paths.PLAYERS_FULL)
  if players_full.duplicated(subset=ID_COLS).any():
    raise ValueError("players_full has duplicate player-seasons")

  df = players_full
  n_start = len(df)

  # 1. Minutes threshold, with a COVID-season threshold and a limited-games rule
  season_min = df["Season"].map(SEASON_MIN_MINUTES).fillna(MIN_MINUTES)
  meets_default = df[MIN_TOTAL_COL] >= MIN_MINUTES
  meets_season = df[MIN_TOTAL_COL] >= season_min
  limited = (
    (df[GP_COL] >= LIMITED_GAMES_MIN_G)
    & (df[MIN_PG_COL] >= LIMITED_GAMES_MIN_MPG)
    & ~meets_season
  )
  reason = np.select(
    [meets_default, meets_season, limited],
    ["minutes", "covid_threshold", "limited_games"],
    default="",
  )
  pf = df[reason != ""].copy()
  pf["keep_reason"] = reason[reason != ""]
  n_minutes = len(pf)

  # 2. Drop seasons with unreliable play-by-play data
  pf = pf[~pf["Season"].isin(DROP_SEASONS)].copy()
  n_seasons = len(pf)

  # 3. Drop player-seasons with no shot zone data
  pf = pf[pf[BASIC5].sum(axis=1) >= 99].copy()
  n_final = len(pf)

  # Flags for low-information rows (kept, not dropped)
  pf["low_fga"] = pf[FGA_COL] < LOW_FGA
  pf["make_tag_cov"] = (pf["FGM Assisted"] + pf["FGM Unassisted"]) / pf["FGM"]
  pf["ast_tag_cov"] = pf[ZONE_AST].sum(axis=1) / pf["Ast"]
  pf["low_coverage"] = (pf["make_tag_cov"] < LOW_COV) | (pf["ast_tag_cov"] < LOW_COV)

  if verbose:
    print(f"Start:                         {n_start:,}")
    print(f"After minutes rules:           {n_minutes:,}")
    print(f"After dropping {DROP_SEASONS}: {n_seasons:,}")
    print(f"After dropping missing zones:  {n_final:,}")
    print("\nKept by rule:")
    print(pf["keep_reason"].value_counts().to_string())
    print(f"\nFlagged low_fga:      {pf['low_fga'].sum():,}")
    print(f"Flagged low_coverage: {pf['low_coverage'].sum():,}")

  return pf


# ---------------------------------------------------------------------------
# Style features
# ---------------------------------------------------------------------------
def build_style_features(pf):
  """
  Build the 32 style-only features from a filtered player table.

  Returns
    feat  DataFrame of features (same index as pf)
    ids   DataFrame of identifiers and flags (same index as pf)
  """
  feat = pd.DataFrame(index=pf.index)

  # Location (7): left and right sides combined
  feat["Rim"] = pf["Rim Shot %"]
  feat["Paint"] = pf["Paint Shot %"]
  for zone in ["Baseline 2", "Elbow 2", "Corner 3", "Wing 3"]:
    feat[zone] = pf[f"Left {zone} FGA Freq %"] + pf[f"Right {zone} FGA Freq %"]
  feat["Top of Key 3"] = pf["Top of Key 3 FGA Freq %"]

  # Deep shooting (1)
  feat["NBA 3"] = pf["NBA 3 FGA Freq %"]

  # Shot type (5)
  feat["Dunk"] = pf["Dunk FGA Freq %"]
  feat["Layup"] = pf["Layup FGA Freq %"]
  feat["Alley-Oop"] = pf["Alley-Oop FGA Freq %"]
  feat["Putback"] = pf["FGA Freq % Putback"]
  feat["Transition"] = pf["Transition Shot %"]

  # Self-creation (2): share of made shots that were assisted (over tagged makes)
  feat["2PM Assisted"] = pf["2PM Assisted %"]
  feat["3PM Assisted"] = pf["3PM Assisted %"]

  # Rim contact (1): shooting fouls drawn per rim shot attempt
  feat["Rim Fouls Drawn"] = 100 * pf["Rim Shooting Foul Drawn"] / pf["Rim Shot Att"]

  # Passing destination (5): stored as fractions, converted to 0-100
  for zone in ["Rim", "Paint", "Midrange", "Corner 3", "Above Break 3"]:
    feat[f"Ast to {zone}"] = 100 * pf[f"% Ast {zone}"]

  # Role (11)
  for col in ROLE_COLS:
    feat[col] = pf[col]

  feat = feat.replace([np.inf, -np.inf], np.nan)
  ids = pf[ID_COLS + FLAG_COLS].copy()
  return feat, ids
