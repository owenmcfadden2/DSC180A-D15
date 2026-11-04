# Preliminary Archetype Results

## 1. Experiment summary

Two feature sets were fitted to the same 16,723 player-seasons from 2021-22 through 2025-26, each with at least 200 minutes. There were 42 seeded fits: two datasets, seven archetype counts (6-12) and three starts per count. No players or selected features were removed during modeling.

The 49-feature baseline includes TS % and three unassisted-scoring volume fields. The 45-feature reduced variant excludes those four fields. All shared inputs use identical preprocessing parameters.

## 2. Reconstruction comparison

Values below are best-run RSS divided by each dataset's own total centered standardized sum of squares. Lower values mean better reconstruction of that particular feature set. Because the feature sets differ, a lower ratio in one dataset alone does not establish that it is a better model.

| Archetypes | 49-feature baseline | 45-feature reduced |
| --- | ---: | ---: |
| 6 | 0.4816 | 0.4813 |
| 7 | 0.4545 | 0.4572 |
| 8 | 0.4322 | 0.4312 |
| 9 | 0.4112 | 0.4118 |
| 10 | 0.3962 | 0.3945 |
| 11 | 0.3825 | 0.3763 |
| 12 | 0.3645 | 0.3646 |

## 3. Why review nine archetypes?

Reconstruction improved gradually as the count increased, without a sharp single cutoff. A discrete curve-knee screen suggested nine for the baseline and eight for the reduced variant. Nine had the lowest average matched-profile and player-mixture differences across the three starts within both datasets, making it a useful common review count. This is a provisional review choice, not a validated optimum.

| Initialization sensitivity at K=9 | Baseline | Reduced |
| --- | ---: | ---: |
| Aligned profile RMS difference (feature SD units) | 0.652 | 0.782 |
| Mean player-mixture L1 difference | 0.223 | 0.358 |

All 42 runs met the configured stopping criterion. Some NNLS loss histories were nonmonotone, so stopping is not evidence of a global optimum. Every history was retained and fitted weights, archetype construction and RSS were independently checked. These sensitivity measures compare initializations on the same observations; they are not resampling confidence estimates.

## 4. Working labels for the nine-profile review

The names below are descriptive working labels developed from the fitted profiles and local player examples. They are not hard classes: each player retains all nine mixture weights. A3 and A7 remain under review. IDs are specific to their respective fit.

| ID | 49-feature baseline | 45-feature reduced |
| --- | --- | --- |
| A1 | Offensive rebounder | Offensive rebounder |
| A2 | Lead guard | Lead guard |
| A3 | Defensive connector / secondary ball handler | Connective wing |
| A4 | Three-point specialist | Three-point specialist |
| A5 | Interior scoring big | Scoring wing |
| A6 | Low-usage floor spacer | Low-usage floor spacer |
| A7 | Defensive / transition player | Defensive / transition player |
| A8 | Traditional big | Traditional big |
| A9 | Perimeter scoring wing | Perimeter scoring wing |

The label review distinguished the offensive-rebounding role from the rim-protection/dunk role, and the high-involvement interior scorer from the more assisted perimeter scorer. The baseline A3 profile was more guard-sized and turnover-heavy than the reduced model's corresponding connective-wing profile. Labels describe observed statistical patterns rather than verified possession actions or scouting evaluations.

## 5. Interpretation questions that remain

- A high And1 percentage can be based on only one or two shooting-foul draws. A low-FT spacing profile can therefore have a high conditional And1 rate without frequently drawing fouls. Median imputation does not address valid but sparse observed percentages.
- Assist-destination shares describe where a player's passes create baskets. Own-shot assisted percentages describe how that player's made shots were created. These must be interpreted separately.
- The exported FT Ratio definition remains unresolved. It does not match the tested FTA/FGA, FTA-per-possession or proposed FT-trip-share definitions. High/low values should not be treated as a quality ranking.
- Large construction weights on a few observations are expected for extreme archetypes; small-denominator behavior and initialization variation still need review before durable labels are assigned.
- Equal feature variance does not give each basketball domain equal influence. No correlated-feature pruning, clipping, smoothing or extra domain weights were applied in this initial comparison.

## 6. Reproduction and output boundaries

Run the preparation notebook and both modeling scripts in the order listed in [PLAYER_ARCHETYPES.md](PLAYER_ARCHETYPES.md). Detailed fitted profiles, representative players, mixture weights, missingness masks, arrays and plots remain in the private local analysis outputs; they are deliberately not embedded in this repository. The committed notebook has no outputs.

The table records the initial source snapshot and fitted comparison. Changes to the data, implementation or numerical environment can change local solutions; rerun the experiments and compare profiles before reusing labels.
