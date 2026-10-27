# Setup

How to get the DSC180A-D15 repo and data running on your computer. Takes about 10 minutes.

The code lives on GitHub. The data does **not**: it's in our shared Google Drive folder, **CBB Analytics Data**, and each of us points the code at our own downloaded copy. It's licensed CBB Analytics data, so please never commit data files (CSV, .csv.gz, Parquet, zip, etc.) to this repo. The `.gitignore` blocks them, but double check before you commit.

## 1. Clone the repo

**GitHub Desktop:** File > Clone repository > find `DSC180A-D15` > Clone.

**Or terminal:**
```
git clone https://github.com/owenmcfadden2/DSC180A-D15.git
```

If you can't see the repo, ask Owen to add you as a collaborator.

## 2. Get the data folder

Download the **CBB Analytics Data** folder from our shared Google Drive (right-click > Download; Drive gives you a zip, so unzip it). Put it anywhere **outside** the repo folder.

It's one flat folder (about 320 MB) that looks like this:

```
README.md                         what every file contains
data_dictionary.csv               every column in every file, with the original API field

players.csv / players_full.csv.gz          player-season (curated / all 881 columns), 2018-19 to 2025-26
teams.csv / teams_full.csv                 team-season (curated / all 1,187 columns)
conferences.csv                            conference strength, rank, tier per season (+ 2026-27)
players_conference_only.csv                player-season, conference games only
teams_conference_only.csv                  team-season, conference games only
teams_pbp_conference_only.csv              team play-by-play stats, conference games only
team_possession_types.csv                  team offense/defense by possession type and length
lineups.csv.gz                             5-man lineups, 2023-24 to 2025-26
games.csv.gz                               one row per game
team_games.csv.gz                          one row per team per game
player_games.csv.gz                        one row per player per game, 2023-24 to 2025-26
transfers.csv                              every transfer, before/after stats
```

`.csv.gz` files are compressed CSVs. Don't unzip them; pandas reads them directly.

If you set things up with the old folder (with `full/`, `clean/`, `raw/` subfolders), delete it and use this one instead.

## 3. Create `local_paths.py`

1. In the repo folder, copy `local_paths.example.py` and rename the copy to `local_paths.py`.
2. Open it and set `DATA_DIR` to the data folder (the one containing `README.md`):

Windows:
```python
DATA_DIR = r"C:\Users\yourname\Documents\CBB Analytics Data"
```

Mac:
```python
DATA_DIR = r"/Users/yourname/Documents/CBB Analytics Data"
```

`local_paths.py` is gitignored, so your path stays on your computer.

## 4. Install packages

```
pip install pandas nbstripout
```
(On Mac you may need `pip3`.)

## 5. Check that everything works

From the repo folder:
```
python paths.py
```
(On Mac you may need `python3`.)

Every required file should say `OK`. If you see `MISSING`, `DATA_DIR` is pointing at the wrong folder.

## 6. Turn on notebook output stripping

From the repo folder, run once:
```
nbstripout --install
```

This clears notebook outputs (printed tables, etc.) when you commit, so data never ends up on GitHub by accident. Your local notebooks keep their outputs.

## Loading data

In any script or notebook in the repo root:

```python
from paths import load, PLAYERS_FULL, TEAMS_FULL, POSSESSION_TYPES

players = load(PLAYERS_FULL)
teams = load(TEAMS_FULL)
possessions = load(POSSESSION_TYPES)
```

Notebooks in a subfolder (like `notebooks/`) need one extra line first:

```python
import sys; sys.path.insert(0, "..")
from paths import load
```

Look up any column in the data dictionary:

```python
from paths import load, DATA_DICT
dd = load(DATA_DICT)
dd[dd["column"].str.contains("Corner 3")]
```

## Things to know about the data

- **Joining:** use `Player ID`, `Team ID`, `Game ID`, and `Season` (like `2025-26`). Player IDs stay the same across seasons and schools.
- **Units:** percentages are 0 to 100 (TS % = 58.1, not 0.581).
- **D1 men's only.** D2/D3 stats aren't available through our API access.
- **Season stats exclude games against non-D1 opponents** (CBB Analytics' default), so totals can differ slightly from other sites.
- **`team_games` is one row per team per game** (offensive view). The opponent's numbers are in the "Opp" columns.
- **`team_possession_types` is long format:** separate rows per team, side (Offense/Defense), and possession type or length. Pivot it for one row per team.
- **2018-19 play-by-play stats are thinner** (first season of tracking).
- **Unconfirmed abbreviations:** some columns keep CBB Analytics' codes (S01/S12/S23, Att1/Att2/Att3P, Rim3s, Lane2, Hkm, and a few others). Check the CBB Analytics glossary before relying on them.
