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

## 5. Variables supporting each K=9 label

The following evidence comes from the selected seed-44 K=9 fit for each dataset. For each archetype, the ten listed variables are ordered by the absolute value of its standardized profile coordinate. **High** means above the pooled, median-imputed player-season mean; **low** means below it. Ranking uses the unrounded coordinates. These are the largest profile deviations, not causal effects, predictive feature importance, or averages of players assigned to a hard cluster. There is no additional outlier significance threshold.

The label explanations also use relevant supporting fields outside the top ten, including the privately retained own-shot assisted percentage. `% Of Team ...` fields measure the individual player's share of a team total. `% Ast3`, `% Ast Rim` and `% Ast Dunk` describe assist destinations; `3PM Assisted %`, `Rim Assisted %` and `Non-Rim 2 Assisted %` describe the player's own made shots. Numerical profiles and player examples remain local.

### 5.1. 49-feature baseline

#### A1: Offensive rebounder

**Largest deviations, ranked:** `Att1 Attempt Share %` (low), `2nd Chance Pts % Pts` (high), `Fouls Drawn Per FGA` (high), `PF %` (high), `FGA Freq % Halfcourt` (low), `Rim 2 Attempt Share %` (high), `Layup FGA Freq %` (high), `Blocked Per FGA` (high), `FT Rate` (high), `OReb %` (high).

**Label rationale:** High `OReb %`, `2nd Chance Pts % Pts` and `Rim 2 Attempt Share %` support the offensive-rebounding label. Low `Att1 Attempt Share %` is consistent with a greater share of later attempts in a possession. Low `Usage %`, `Ast %` and `Pts Created/40` distinguish this role from the high-involvement interior scorer A5. A1 has more offensive rebounding and a higher rim-attempt share than A8, whose defining extremes are blocks and dunks.

#### A2: Lead guard

**Largest deviations, ranked:** `3PM Unassisted/40` (high), `% Of Team Ast` (high), `Ast %` (high), `3PM Assisted %` (low), `Pts Scored Unassisted/40` (high), `Pts Created/40` (high), `% Of Team TO` (high), `Alley-Oop Ast/40` (high), `% Of Team FGA` (high), `Usage %` (high).

**Label rationale:** High `Ast %`, `% Of Team Ast`, `Pts Created/40` and `Usage %` support a primary creator. High unassisted scoring volume, especially `3PM Unassisted/40`, and low `3PM Assisted %` support self-created offense. Low `Height (in)` adds guard-sized context. `% Of Team TO` is also high, so the label describes responsibility rather than error-free play.

#### A3: Defensive connector / secondary ball handler

**Largest deviations, ranked:** `TO %` (high), `Off Fouls Drawn %` (high), `Fouls Drawn Per FGA` (high), `Individual Stop %` (high), `TS %` (low), `Blocked Per FGA` (high), `Stl %` (high), `Ast %` (high), `Rim Assisted %` (low), `FGA Freq % Halfcourt` (high).

**Label rationale:** High `Ast %` with smaller `Height (in)` supports secondary ball handling. High `Off Fouls Drawn %`, `Stl %` and `Individual Stop %` supply the defensive part of the label. However, `TO %` is the strongest deviation and `TS %` is low. This is a turnover-heavy defensive/creation profile; the connector label remains provisional. Unlike reduced-model A3, its `DReb %` is below the pooled mean.

#### A4: Three-point specialist

**Largest deviations, ranked:** `3PM % Pts` (high), `% Ast3` (high), `3P Attempt Share %` (high), `% Ast Rim` (low), `Paint Pts % Pts` (low), `Layup FGA Freq %` (low), `TO %` (low), `Individual Stop %` (low), `2PM Unassisted/40` (low), `And1 %` (low).

**Label rationale:** High `3P Attempt Share %` and `3PM % Pts`, with low rim share, layup frequency and paint scoring, support a specialized perimeter shot diet. `% Ast3` is high and `% Ast Rim` is low: when this profile records assists, their destinations lean toward threes. Its own made shots are mostly assisted in the interpretation export. Relative to A9, the shot diet is more concentrated in threes and `Usage %` is lower.

#### A5: Interior scoring big

**Largest deviations, ranked:** `% Of Team FTA` (high), `2PM Unassisted/40` (high), `Ffl Drawn %` (high), `Pts Scored Unassisted/40` (high), `Usage %` (high), `% Of Team TO` (high), `% Of Team FGA` (high), `Pts Created/40` (high), `DReb %` (high), `Transition Shot %` (low).

**Label rationale:** High `Usage %`, `% Of Team FGA`, `% Of Team FTA`, unassisted two-point scoring and `Pts Created/40` support a heavily involved interior scorer. High `DReb %` and above-average height add big-player context. Low `3P Attempt Share %` is why this is an interior scoring big rather than a perimeter scoring wing. `Dunk FGA Freq %` is not elevated, so a dunking-big label would overstate the evidence. A8 is much more distinctive for blocks and dunks.

#### A6: Low-usage floor spacer

**Largest deviations, ranked:** `FT Ratio` (low), `And1 %` (high), `3PM % Pts` (high), `FT Rate` (low), `3P Attempt Share %` (high), `Shooting Foul Drawn %` (low), `Pts Scored Unassisted/40` (low), `Ffl Drawn %` (low), `Fouls Drawn Per FGA` (low), `% Of Team FTA` (low).

**Label rationale:** High three-point attempt and scoring shares, low `Usage %`, low free-throw involvement and mostly assisted makes support a low-usage floor spacer. The two largest deviations are actually very low `FT Ratio` and very high `And1 %`. The former has an unresolved definition and the latter is conditional on shooting-foul draws and can be sparse. They distinguish the fitted profile statistically, but do not establish that this player frequently creates and-one opportunities.

#### A7: Defensive / transition player

**Largest deviations, ranked:** `Fast Break Pts % Pts` (high), `Transition Shot %` (high), `FGA Freq % Halfcourt` (low), `Stl %` (high), `Stl + Blk Per PF` (high), `Individual Stop %` (high), `% Ast Rim` (high), `Blocked Per FGA` (high), `% Ast3` (low), `Layup FGA Freq %` (high).

**Label rationale:** High `Fast Break Pts % Pts` and `Transition Shot %`, with low `FGA Freq % Halfcourt`, support transition-oriented offense. High `Stl %`, `Stl + Blk Per PF` and `Individual Stop %` add defensive event activity. This explains the defensive/transition label. These events do not establish overall defensive quality, so the defensive interpretation remains under review.

#### A8: Traditional big

**Largest deviations, ranked:** `Blk %` (high), `Dunk FGA Freq %` (high), `Individual Stop %` (high), `Stl + Blk Per PF` (high), `Height (in)` (high), `Rim 2 Attempt Share %` (high), `Non-Rim 2 Assisted %` (high), `Paint Pts % Pts` (high), `TS %` (high), `Att1 Attempt Share %` (low).

**Label rationale:** Extreme `Blk %`, `Dunk FGA Freq %`, `Individual Stop %` and `Stl + Blk Per PF`, together with high `Height (in)`, support a traditional rim-protecting big. High rim share, paint scoring, `DReb %`, `Rim Assisted %` and `Non-Rim 2 Assisted %` add an assisted interior role. Relative to A1, A8 is taller and much more block/dunk oriented, while A1 has higher offensive rebounding and a larger rim-attempt share.

#### A9: Perimeter scoring wing

**Largest deviations, ranked:** `% Ast Rim` (high), `% Ast Dunk` (high), `% Ast3` (low), `3PM % Pts` (high), `Layup FGA Freq %` (low), `3P Attempt Share %` (high), `And1 %` (low), `Blocked Per FGA` (low), `Paint Pts % Pts` (low), `Rim 2 Attempt Share %` (low).

**Label rationale:** High `3P Attempt Share %` and `3PM % Pts`, with low rim share and paint scoring, support perimeter scoring. Its usage and team shot share are higher than A4's and A6's, while `Ast %` and `Ast/TO` are low. The largest deviations concern assist destinations: high `% Ast Rim` and `% Ast Dunk`, low `% Ast3`. Those describe the baskets created by its relatively infrequent assists, not its own shot locations. Its own makes are mostly assisted; the label does not imply a primary off-dribble creator.

### 5.2. 45-feature reduced variant

#### A1: Offensive rebounder

**Largest deviations, ranked:** `Att1 Attempt Share %` (low), `2nd Chance Pts % Pts` (high), `PF %` (high), `Fouls Drawn Per FGA` (high), `Blocked Per FGA` (high), `Rim 2 Attempt Share %` (high), `Layup FGA Freq %` (high), `FGA Freq % Halfcourt` (low), `FT Rate` (high), `Shooting Foul Drawn %` (high).

**Label rationale:** High `OReb %`, `2nd Chance Pts % Pts` and `Rim 2 Attempt Share %` support offensive rebounding and interior cleanup. Low `Att1 Attempt Share %` is consistent with more later attempts in a possession. Low `Usage %`, `Ast %` and `Pts Created/40` distinguish it from A5. Compared with A8, A1 has more offensive rebounding and a higher rim-attempt share; A8 is much more distinctive for blocks and dunks.

#### A2: Lead guard

**Largest deviations, ranked:** `% Of Team Ast` (high), `Ast %` (high), `% Of Team TO` (high), `Pts Created/40` (high), `3PM Assisted %` (low), `Alley-Oop Ast/40` (high), `% Of Team FTA` (high), `% Of Team FGA` (high), `Usage %` (high), `Height (in)` (low).

**Label rationale:** High `Ast %`, `% Of Team Ast`, `Pts Created/40`, `Ast/TO` and `Usage %` support a lead creator. Low `3PM Assisted %` and low own-shot assistance in the interpretation export support self-created offense, even though the explicit unassisted-scoring volume inputs were removed. Smaller `Height (in)` provides guard context. High `% Of Team TO` reflects substantial turnover involvement alongside the passing responsibility.

#### A3: Connective wing

**Largest deviations, ranked:** `Off Fouls Drawn %` (high), `Individual Stop %` (high), `Fouls Drawn Per FGA` (high), `TO %` (high), `PF %` (high), `Shooting Foul Drawn %` (high), `FGA Freq % Halfcourt` (high), `FT Rate` (high), `Transition Shot %` (low), `Blk Rcv %` (high).

**Label rationale:** Above-average `Ast %`, `DReb %` and height, with less scoring involvement than A5, were the basis for connective wing. Its assist rate exceeds A5's, while `Usage %`, team shot share and rebounding are lower than A5's. However, the strongest fitted deviation is `Off Fouls Drawn %`, followed by defensive-stop and foul-related rates; passing is not its dominant statistical extreme. High `TO %` also weakens a clean connector interpretation. Keep this label under review rather than treating the name as settled.

#### A4: Three-point specialist

**Largest deviations, ranked:** `% Ast3` (high), `% Ast Rim` (low), `3PM % Pts` (high), `3P Attempt Share %` (high), `Layup FGA Freq %` (low), `Paint Pts % Pts` (low), `FT Ratio` (high), `And1 %` (low), `Individual Stop %` (low), `% Of Team TO` (low).

**Label rationale:** High `3P Attempt Share %` and `3PM % Pts`, plus low rim share, paint scoring and layup frequency, support a three-point specialist. High `% Ast3` and low `% Ast Rim` describe where its assists go; its own makes are also mostly assisted. Its usage is lower and its three-point concentration is greater than A9's. High `FT Ratio` is an unresolved exported field, not evidence that the profile draws many free throws: `FT Rate` is low.

#### A5: Scoring wing

**Largest deviations, ranked:** `% Of Team FTA` (high), `Ffl Drawn %` (high), `Usage %` (high), `DReb %` (high), `% Of Team FGA` (high), `% Of Team TO` (high), `Pts Created/40` (high), `Shooting Foul Drawn %` (high), `OReb %` (high), `Height (in)` (high).

**Label rationale:** High `Usage %`, `% Of Team FGA`, `% Of Team FTA`, `Pts Created/40` and foul-drawing rates support a heavily involved scorer. High `DReb %`, `OReb %` and height distinguish it from A3 and A9. The saved name is scoring wing, but low `3P Attempt Share %` and its interior shot diet qualify that wording: the profile is an interior-oriented scorer with forward/big characteristics, not a perimeter wing. It is not as block/dunk oriented as A8.

#### A6: Low-usage floor spacer

**Largest deviations, ranked:** `FT Ratio` (low), `And1 %` (high), `3PM % Pts` (high), `FT Rate` (low), `3P Attempt Share %` (high), `Shooting Foul Drawn %` (low), `Ffl Drawn %` (low), `Fouls Drawn Per FGA` (low), `% Of Team FTA` (low), `% Of Team TO` (low).

**Label rationale:** High three-point attempt and scoring shares, low `Usage %`, low free-throw involvement and mostly assisted makes support a low-usage floor spacer. Very low `FT Ratio` and very high `And1 %` are the largest fitted extremes. As in the baseline, the unresolved FT Ratio definition and the potentially sparse conditional And1 denominator limit how literally those extremes should be interpreted. They are not evidence of frequent and-one creation.

#### A7: Defensive / transition player

**Largest deviations, ranked:** `Fast Break Pts % Pts` (high), `Transition Shot %` (high), `Stl %` (high), `FGA Freq % Halfcourt` (low), `Stl + Blk Per PF` (high), `Individual Stop %` (high), `Blocked Per FGA` (high), `Height (in)` (low), `% Ast Rim` (high), `% Ast3` (low).

**Label rationale:** High `Fast Break Pts % Pts` and `Transition Shot %`, together with low halfcourt frequency, support transition-oriented offense. High `Stl %`, `Stl + Blk Per PF` and `Individual Stop %` support defensive event activity. Its usage and height are lower than baseline A7's. The defensive/transition name remains a descriptive working label rather than a validated overall defensive rating.

#### A8: Traditional big

**Largest deviations, ranked:** `Blk %` (high), `Dunk FGA Freq %` (high), `Stl + Blk Per PF` (high), `Individual Stop %` (high), `Height (in)` (high), `Rim 2 Attempt Share %` (high), `Non-Rim 2 Assisted %` (high), `Paint Pts % Pts` (high), `Att1 Attempt Share %` (low), `FGA Freq % Halfcourt` (low).

**Label rationale:** Very high `Blk %`, `Dunk FGA Freq %`, `Stl + Blk Per PF` and `Individual Stop %`, plus tall `Height (in)`, support a traditional rim-protecting big. High rim share, paint scoring, `DReb %` and own-shot assisted percentages support an assisted interior role. Compared with A1, A8 is taller and much more block/dunk oriented; A1 has more offensive rebounding and a larger rim-attempt share.

#### A9: Perimeter scoring wing

**Largest deviations, ranked:** `% Ast Rim` (high), `% Ast3` (low), `% Ast Dunk` (high), `3PM % Pts` (high), `3P Attempt Share %` (high), `Layup FGA Freq %` (low), `Blocked Per FGA` (low), `And1 %` (low), `Shooting Foul Drawn %` (low), `Paint Pts % Pts` (low).

**Label rationale:** High three-point attempt and scoring shares, low rim share and low paint scoring support a perimeter scorer. Its usage and team shot share exceed A4's and A6's, while `Ast %` and `Ast/TO` are low. High `% Ast Rim` and `% Ast Dunk`, with low `% Ast3`, describe the destinations of its relatively infrequent assists. They do not mean A9 personally finishes at the rim. Its own makes are mostly assisted, so perimeter scoring wing does not imply a primary self-creating scorer.

## 6. Interpretation questions that remain

- A high And1 percentage can be based on only one or two shooting-foul draws. A low-FT spacing profile can therefore have a high conditional And1 rate without frequently drawing fouls. Median imputation does not address valid but sparse observed percentages.
- Assist-destination shares describe where a player's passes create baskets. Own-shot assisted percentages describe how that player's made shots were created. These must be interpreted separately.
- The exported FT Ratio definition remains unresolved. It does not match the tested FTA/FGA, FTA-per-possession or proposed FT-trip-share definitions. High/low values should not be treated as a quality ranking.
- Large construction weights on a few observations are expected for extreme archetypes; small-denominator behavior and initialization variation still need review before durable labels are assigned.
- Equal feature variance does not give each basketball domain equal influence. No correlated-feature pruning, clipping, smoothing or extra domain weights were applied in this initial comparison.

## 7. Reproduction and output boundaries

Run the preparation notebook and both modeling scripts in the order listed in [PLAYER_ARCHETYPES.md](PLAYER_ARCHETYPES.md). Detailed fitted profiles, representative players, mixture weights, missingness masks, arrays and plots remain in the private local analysis outputs; they are deliberately not embedded in this repository. The committed notebook has no outputs.

The table records the initial source snapshot and fitted comparison. Changes to the data, implementation or numerical environment can change local solutions; rerun the experiments and compare profiles before reusing labels.
