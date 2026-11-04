# Player Archetypes: Two Preliminary Experiments

This work compares two feature sets for describing college basketball playing styles with
archetypal analysis. Each player-season receives a mixture of archetype weights. The
objective is an interpretable starting point for style analysis, not a prediction of player quality.

## 1. Files and reading order

| File | Purpose |
| --- | --- |
| [Preparation notebook](notebooks/01_player_archetypes_eda.ipynb) | Load the private source, audit and repair inputs, derive features, and prepare both matrices. |
| [Baseline model](scripts/02_archetypes_baseline.py) | Fit the 49-feature experiment. |
| [Reduced model](scripts/03_archetypes_style_variant.py) | Fit the 45-feature experiment using the same sample, preprocessing and model settings. |
| [Results](ARCHETYPE_RESULTS.md) | Aggregate comparison, working labels and interpretation limits. |

The notebook follows the numbered sections, short code cells, plain comments and final
Notes section of `01_player_archetypes_eda.ipynb` on `player-archetype-testing`
(reference commit `5e0e3d6`). Its older 32-feature setup and different sample rules are
not the rules used for these two experiments.

## 2. Data and preparation

Use the licensed `players_full.csv.gz` source through the repository's existing `paths.py`
configuration. Keep player-seasons from 2021-22 onward with at least 200 total minutes,
including exactly 200. The analyzed snapshot contains 16,723 observations and 8,304
player IDs. Player ID plus Season is unique; no duplicate removal or aggregation was needed.

The notebook makes the following decisions explicit:

- Reconstruct Usage %, Ast %, OReb %, DReb % and Blk % from available count inputs.
  Their exported fractions were coarsely rounded. The formulas were checked against
  more precise conference-only rates; those rates were not copied into full-season rows.
- Calculate matched-denominator shot shares, possession-sequence share, non-rim-two
  assisted percentage and combined steals/blocks per foul. Retain detailed zones and
  other component fields separately for interpretation.
- Keep missing and undefined rates visible in the observed tables. For the initial fit,
  fill them with each feature's observed median, preserve the missingness mask, and
  standardize by the pooled population standard deviation. Genuine zeros stay zero.
- Use the same rows and the same per-column parameters for both variants. Keep
  low-opportunity and incomplete-PBP flags outside the fit. Do not clip players,
  automatically remove correlated inputs or add unrecorded feature weights.

The baseline has 49 features. The reduced variant removes exactly `TS %`,
`Pts Scored Unassisted/40`, `2PM Unassisted/40` and `3PM Unassisted/40`.
The latter three are scoring-volume measures, so the reduced set is not described as
entirely free of outcome-related information. `Pts Created/40` remains in both.
The complete feature lists and formulas are in the notebook.

## 3. Reproduce the experiments

Use Python 3.12 and configure `local_paths.py` or `CAPSTONE_DATA_DIR` as described in
[SETUP.md](SETUP.md). The data directory must remain outside the repository.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-archetypes.txt
python -m ipykernel install --user --name capstone --display-name "Python (capstone)"
```

Run the preparation notebook top to bottom in the `capstone` kernel. Then, from the repo root:

```bash
python scripts/02_archetypes_baseline.py
python scripts/03_archetypes_style_variant.py
```

For a shorter inspection of the selected count:

```bash
python scripts/02_archetypes_baseline.py --k 9
python scripts/03_archetypes_style_variant.py --k 9
```

Both scripts use `archetypes.AA` 0.12.2, NNLS optimization, counts 6-12 and three
separate initializations (seeds 42, 43, 44). Each script retains every run and selects
the lowest final reconstruction error at each count. It checks coefficient constraints,
recomputes RSS and aligns profiles across starts before reporting initialization sensitivity.
The scripts are deliberately self-contained and use the same fitting logic.

Validation of this cleaned workflow executed the preparation notebook and both complete
model scripts. Both matrices reproduced the saved inputs exactly; all 42 fits reproduced
the saved coefficient arrays, loss histories, selected seeds and aggregate metrics.

## 4. Private outputs and interpretation

Generated files go under `local_outputs/archetype_comparison/`, which is gitignored.
Preparation saves observed features, standardized matrices, identifiers, interpretation
fields, original rounded rates, missingness/support flags and fitted scaling parameters.
Model folders save all coefficient arrays and loss histories, original-unit profiles,
player mixture weights, representative player-seasons and imputation influence.

Exclude Record ID and descriptive labels from model inputs. For interpreting actual
players, return to observed values and the missingness flags: median placeholders are
not measured player behavior. The nine-archetype labels are provisional and apply to
the corresponding fitted model; a future refit needs profile alignment before reusing names.

## 5. Scope and limitations

The comparison fits all eligible observations for descriptive exploration. It has no
held-out predictive evaluation. Fit preprocessing on training observations only if a
train/test experiment is added. Three starts check initialization sensitivity, not
bootstrap stability. Small-denominator percentages, correlated features and valid extremes
can affect the profiles. FT Ratio's exported definition remains unresolved.

Only code, output-free notebook source, methodology and aggregate findings belong in
GitHub. Raw observations, player examples, fitted numerical profiles, mixture weights,
arrays and executed notebooks remain local. Clear notebook outputs before committing;
`nbstripout --install` is available through the pinned workflow's requirements.

Package reference: [archetypes.AA documentation](https://archetypes.readthedocs.io/en/latest/reference/_autosummary/numpy/archetypes.AA.html).
