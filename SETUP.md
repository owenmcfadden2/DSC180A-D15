# Setup

How to get the DSC180A-D15 repo and data running on your computer. Takes about 10 minutes.

The code lives on GitHub. The data does **not**: it's in our shared drive folder, and each of us points the code at our own copy of it. Please never commit data files (CSV, Parquet, etc.) to this repo.

## 1. Clone the repo

**GitHub Desktop:** File > Clone repository > find `DSC180A-D15` under your account > Clone.

**Or terminal:**
```
git clone https://github.com/owenmcfadden2/DSC180A-D15.git
```

If you can't see the repo, ask Owen to add you as a collaborator.

## 2. Get the data folder

Download the shared data folder from our shared drive (or sync it with Google Drive for desktop / OneDrive). Put it anywhere **outside** the repo folder.

It should look like this:
```
data_dictionary.csv
README.txt
full/    players_full.parquet, teams_full.parquet
clean/   players.csv, teams.csv, conferences.csv, transfers.csv
raw/     cbb_raw_backup.zip
```

## 3. Create `local_paths.py`

1. In the repo folder, copy `local_paths.example.py` and rename the copy to `local_paths.py`.
2. Open it and set `DATA_DIR` to where you put the data folder:

Windows:
```python
DATA_DIR = r"C:\Users\yourname\Documents\DSC180A-D15 Data"
```

Mac:
```python
DATA_DIR = r"/Users/yourname/Documents/DSC180A-D15 Data"
```

`local_paths.py` is gitignored, so your path stays on your computer.

## 4. Install packages

```
python -m pip install pandas pyarrow nbstripout
```
(On Mac you may need `python3` instead of `python`.)

## 5. Check that everything works

From the repo folder:
```
python paths.py
```
(On Mac you may need `python3`.)

Every line should say `OK`. If you see `MISSING`, `DATA_DIR` is pointing at the wrong folder.

## 6. Turn on notebook output stripping

From the repo folder, run once:
```
python -m nbstripout --install
```

Check it worked with `python -m nbstripout --status` (it should say nbstripout is installed in the repo).

This clears notebook outputs (printed tables, etc.) when you commit, so data never ends up on GitHub by accident. Your local notebooks keep their outputs.

## Loading data

In any script or notebook in the repo root:
```python
import pandas as pd
from paths import PLAYERS_FULL, TEAMS_FULL, DATA_DICT

players = pd.read_parquet(PLAYERS_FULL)
teams = pd.read_parquet(TEAMS_FULL)
dictionary = pd.read_csv(DATA_DICT)
```

In a notebook inside a subfolder (like `notebooks/`), add this first:
```python
import sys; sys.path.insert(0, "..")
```

## Before you commit

Check the Changes list in GitHub Desktop (or `git status`). You should only see code, notebooks, Markdown, and figures. If a CSV or Parquet file shows up, don't commit it and let Owen know.
