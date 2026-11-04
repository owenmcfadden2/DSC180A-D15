# Preliminary Archetype Results

## 1. The 49 variables

These are the model inputs, using the exact names in the preparation notebook. Player and season identifiers are excluded.

| # | Variable |
| ---: | --- |
| 1 | `Height (in)` |
| 2 | `Usage %` |
| 3 | `TS %` |
| 4 | `FT Rate` |
| 5 | `OReb %` |
| 6 | `DReb %` |
| 7 | `Ast %` |
| 8 | `TO %` |
| 9 | `Stl %` |
| 10 | `Blk %` |
| 11 | `Ast/TO` |
| 12 | `Transition Shot %` |
| 13 | `Blocked Per FGA` |
| 14 | `Fouls Drawn Per FGA` |
| 15 | `2nd Chance Pts % Pts` |
| 16 | `Fast Break Pts % Pts` |
| 17 | `Paint Pts % Pts` |
| 18 | `3PM % Pts` |
| 19 | `% Of Team Ast` |
| 20 | `% Of Team FGA` |
| 21 | `% Of Team FTA` |
| 22 | `% Of Team TO` |
| 23 | `PF %` |
| 24 | `% Ast Rim` |
| 25 | `% Ast Paint` |
| 26 | `Rim Assisted %` |
| 27 | `FGA Freq % Halfcourt` |
| 28 | `% Ast Dunk` |
| 29 | `Dunk FGA Freq %` |
| 30 | `Layup FGA Freq %` |
| 31 | `Alley-Oop Ast/40` |
| 32 | `% Ast3` |
| 33 | `3PM Assisted %` |
| 34 | `Pts Created/40` |
| 35 | `Pts Scored Unassisted/40` |
| 36 | `2PM Unassisted/40` |
| 37 | `3PM Unassisted/40` |
| 38 | `Shooting Foul Drawn %` |
| 39 | `And1 %` |
| 40 | `Ffl Drawn %` |
| 41 | `Off Fouls Drawn %` |
| 42 | `FT Ratio` |
| 43 | `Blk Rcv %` |
| 44 | `Individual Stop %` |
| 45 | `Att1 Attempt Share %` |
| 46 | `Stl + Blk Per PF` |
| 47 | `Non-Rim 2 Assisted %` |
| 48 | `Rim 2 Attempt Share %` |
| 49 | `3P Attempt Share %` |

## 2. The 45-variable version

This version removes four efficiency/scoring-outcome variables to put more emphasis on playing style. `TS %` measures efficiency; the other three measure made-shot production rather than efficiency directly. All other inputs remain the same.

| Removed variable | Reason |
| --- | --- |
| `TS %` | Measures scoring efficiency rather than how the player plays. |
| `Pts Scored Unassisted/40` | Depends on points actually scored, mixing self-creation with scoring outcomes. |
| `2PM Unassisted/40` | Counts made unassisted twos, so it depends on conversion as well as shot creation. |
| `3PM Unassisted/40` | Counts made unassisted threes, so it depends on conversion as well as shot creation. |

`Pts Created/40` stays in both versions, as agreed.

## 3. Archetype counts tested

Both datasets were fitted with **K = 6, 7, 8, 9, 10, 11 and 12**, using three starts per count (seeds 42, 43 and 44). The sample was player-seasons from 2021-22 onward with at least 200 minutes. The results below show the selected **K = 9** models.

## 4. The two nine-archetype results

### Labels

| Archetype | 49-variable version | 45-variable version |
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

### How to read the statistics

Each table lists the ten largest absolute standardized deviations, strongest first. **High** and **Low** mean above or below the pooled player-season mean after median imputation. These describe the fitted archetype, not an average of a hard-assigned player group. The short explanations also use supporting statistics from the saved profiles.

`% Ast3`, `% Ast Rim` and `% Ast Dunk` describe where a player’s assists lead. Assisted-make percentages describe how the player’s own shots were created. `% Of Team ...` variables are the individual player’s shares of team totals. Numerical profiles and player records remain private.

### 49-variable version

#### A1: Offensive rebounder

| Prominent statistic | Direction |
| --- | --- |
| `Att1 Attempt Share %` | Low |
| `2nd Chance Pts % Pts` | High |
| `Fouls Drawn Per FGA` | High |
| `PF %` | High |
| `FGA Freq % Halfcourt` | Low |
| `Rim 2 Attempt Share %` | High |
| `Layup FGA Freq %` | High |
| `Blocked Per FGA` | High |
| `FT Rate` | High |
| `OReb %` | High |

**Why this label:** High offensive rebounding, second-chance scoring and rim-attempt share support this label. Low usage and shot creation suggest a cleanup role. Compared with A8, A1 is more oriented toward offensive rebounds and less toward blocks and dunks.

#### A2: Lead guard

| Prominent statistic | Direction |
| --- | --- |
| `3PM Unassisted/40` | High |
| `% Of Team Ast` | High |
| `Ast %` | High |
| `3PM Assisted %` | Low |
| `Pts Scored Unassisted/40` | High |
| `Pts Created/40` | High |
| `% Of Team TO` | High |
| `Alley-Oop Ast/40` | High |
| `% Of Team FGA` | High |
| `Usage %` | High |

**Why this label:** High assist rate, points created and usage identify a primary ball handler. High unassisted scoring and low assisted-three percentage support self-created offense.

#### A3: Defensive connector / secondary ball handler

| Prominent statistic | Direction |
| --- | --- |
| `TO %` | High |
| `Off Fouls Drawn %` | High |
| `Fouls Drawn Per FGA` | High |
| `Individual Stop %` | High |
| `TS %` | Low |
| `Blocked Per FGA` | High |
| `Stl %` | High |
| `Ast %` | High |
| `Rim Assisted %` | Low |
| `FGA Freq % Halfcourt` | High |

**Why this label:** High assist rate, steals and individual stops support secondary ball handling with defensive activity. Turnover rate is the largest deviation, so the connector label remains under review.

#### A4: Three-point specialist

| Prominent statistic | Direction |
| --- | --- |
| `3PM % Pts` | High |
| `% Ast3` | High |
| `3P Attempt Share %` | High |
| `% Ast Rim` | Low |
| `Paint Pts % Pts` | Low |
| `Layup FGA Freq %` | Low |
| `TO %` | Low |
| `Individual Stop %` | Low |
| `2PM Unassisted/40` | Low |
| `And1 %` | Low |

**Why this label:** A high three-point attempt share and a high share of points from threes support a specialist shooter. Rim attempts and paint scoring are low. Its assists also tend to create threes.

#### A5: Interior scoring big

| Prominent statistic | Direction |
| --- | --- |
| `% Of Team FTA` | High |
| `2PM Unassisted/40` | High |
| `Ffl Drawn %` | High |
| `Pts Scored Unassisted/40` | High |
| `Usage %` | High |
| `% Of Team TO` | High |
| `% Of Team FGA` | High |
| `Pts Created/40` | High |
| `DReb %` | High |
| `Transition Shot %` | Low |

**Why this label:** High usage, unassisted two-point scoring, free-throw involvement and defensive rebounding support an interior scorer. Three-point share is low; dunk frequency is not elevated enough to make dunking its defining trait.

#### A6: Low-usage floor spacer

| Prominent statistic | Direction |
| --- | --- |
| `FT Ratio` | Low |
| `And1 %` | High |
| `3PM % Pts` | High |
| `FT Rate` | Low |
| `3P Attempt Share %` | High |
| `Shooting Foul Drawn %` | Low |
| `Pts Scored Unassisted/40` | Low |
| `Ffl Drawn %` | Low |
| `Fouls Drawn Per FGA` | Low |
| `% Of Team FTA` | Low |

**Why this label:** High three-point share, low usage and low free-throw involvement support a floor spacer. The extreme And1 percentage is conditional on shooting-foul draws and can reflect few opportunities; FT Ratio remains undefined.

#### A7: Defensive / transition player

| Prominent statistic | Direction |
| --- | --- |
| `Fast Break Pts % Pts` | High |
| `Transition Shot %` | High |
| `FGA Freq % Halfcourt` | Low |
| `Stl %` | High |
| `Stl + Blk Per PF` | High |
| `Individual Stop %` | High |
| `% Ast Rim` | High |
| `Blocked Per FGA` | High |
| `% Ast3` | Low |
| `Layup FGA Freq %` | High |

**Why this label:** High transition shooting and fast-break scoring, together with high steals and stops, support a defensive/transition role. The defensive part of the label remains under review.

#### A8: Traditional big

| Prominent statistic | Direction |
| --- | --- |
| `Blk %` | High |
| `Dunk FGA Freq %` | High |
| `Individual Stop %` | High |
| `Stl + Blk Per PF` | High |
| `Height (in)` | High |
| `Rim 2 Attempt Share %` | High |
| `Non-Rim 2 Assisted %` | High |
| `Paint Pts % Pts` | High |
| `TS %` | High |
| `Att1 Attempt Share %` | Low |

**Why this label:** Height, blocks and dunk frequency are the defining traits. High rim-attempt share and assisted interior makes support a traditional big; blocks and dunks distinguish A8 from offensive-rebounding A1.

#### A9: Perimeter scoring wing

| Prominent statistic | Direction |
| --- | --- |
| `% Ast Rim` | High |
| `% Ast Dunk` | High |
| `% Ast3` | Low |
| `3PM % Pts` | High |
| `Layup FGA Freq %` | Low |
| `3P Attempt Share %` | High |
| `And1 %` | Low |
| `Blocked Per FGA` | Low |
| `Paint Pts % Pts` | Low |
| `Rim 2 Attempt Share %` | Low |

**Why this label:** High three-point share and low rim involvement support perimeter scoring. Usage is higher than A4 and A6. High rim/dunk assist shares describe where its passes create baskets, rather than where it takes its own shots.


### 45-variable version

#### A1: Offensive rebounder

| Prominent statistic | Direction |
| --- | --- |
| `Att1 Attempt Share %` | Low |
| `2nd Chance Pts % Pts` | High |
| `PF %` | High |
| `Fouls Drawn Per FGA` | High |
| `Blocked Per FGA` | High |
| `Rim 2 Attempt Share %` | High |
| `Layup FGA Freq %` | High |
| `FGA Freq % Halfcourt` | Low |
| `FT Rate` | High |
| `Shooting Foul Drawn %` | High |

**Why this label:** High offensive rebounding and second-chance scoring support the label, alongside a rim-heavy shot diet. Low usage suggests a cleanup role; A8 is more distinctive for blocks and dunks.

#### A2: Lead guard

| Prominent statistic | Direction |
| --- | --- |
| `% Of Team Ast` | High |
| `Ast %` | High |
| `% Of Team TO` | High |
| `Pts Created/40` | High |
| `3PM Assisted %` | Low |
| `Alley-Oop Ast/40` | High |
| `% Of Team FTA` | High |
| `% Of Team FGA` | High |
| `Usage %` | High |
| `Height (in)` | Low |

**Why this label:** High assist rate, points created, assist-to-turnover ratio and usage support a lead guard. Low assisted-three percentage provides evidence of self-created shots even after unassisted scoring-volume inputs are removed.

#### A3: Connective wing

| Prominent statistic | Direction |
| --- | --- |
| `Off Fouls Drawn %` | High |
| `Individual Stop %` | High |
| `Fouls Drawn Per FGA` | High |
| `TO %` | High |
| `PF %` | High |
| `Shooting Foul Drawn %` | High |
| `FGA Freq % Halfcourt` | High |
| `FT Rate` | High |
| `Transition Shot %` | Low |
| `Blk Rcv %` | High |

**Why this label:** Above-average assists and defensive rebounding, with less scoring involvement than A5, motivated connective wing. However, offensive fouls drawn and stop rate are the largest deviations, while turnovers are high. The label remains under review.

#### A4: Three-point specialist

| Prominent statistic | Direction |
| --- | --- |
| `% Ast3` | High |
| `% Ast Rim` | Low |
| `3PM % Pts` | High |
| `3P Attempt Share %` | High |
| `Layup FGA Freq %` | Low |
| `Paint Pts % Pts` | Low |
| `FT Ratio` | High |
| `And1 %` | Low |
| `Individual Stop %` | Low |
| `% Of Team TO` | Low |

**Why this label:** High three-point attempt and scoring shares, with little rim or paint involvement, support a specialist shooter. Its passes also tend to create threes. High FT Ratio does not imply frequent foul drawing; its definition remains unresolved.

#### A5: Scoring wing

| Prominent statistic | Direction |
| --- | --- |
| `% Of Team FTA` | High |
| `Ffl Drawn %` | High |
| `Usage %` | High |
| `DReb %` | High |
| `% Of Team FGA` | High |
| `% Of Team TO` | High |
| `Pts Created/40` | High |
| `Shooting Foul Drawn %` | High |
| `OReb %` | High |
| `Height (in)` | High |

**Why this label:** High usage, team shot share, free-throw involvement and rebounding support a scoring role with forward/big characteristics. The saved label is scoring wing, although its low three-point share makes it an interior-oriented scorer.

#### A6: Low-usage floor spacer

| Prominent statistic | Direction |
| --- | --- |
| `FT Ratio` | Low |
| `And1 %` | High |
| `3PM % Pts` | High |
| `FT Rate` | Low |
| `3P Attempt Share %` | High |
| `Shooting Foul Drawn %` | Low |
| `Ffl Drawn %` | Low |
| `Fouls Drawn Per FGA` | Low |
| `% Of Team FTA` | Low |
| `% Of Team TO` | Low |

**Why this label:** High three-point share, low usage and low free-throw involvement support a floor spacer. The extreme And1 percentage can be based on few shooting-foul draws; FT Ratio remains undefined.

#### A7: Defensive / transition player

| Prominent statistic | Direction |
| --- | --- |
| `Fast Break Pts % Pts` | High |
| `Transition Shot %` | High |
| `Stl %` | High |
| `FGA Freq % Halfcourt` | Low |
| `Stl + Blk Per PF` | High |
| `Individual Stop %` | High |
| `Blocked Per FGA` | High |
| `Height (in)` | Low |
| `% Ast Rim` | High |
| `% Ast3` | Low |

**Why this label:** Fast-break scoring and transition shooting dominate the offensive profile. High steals and individual stops supply the defensive component, which remains a provisional interpretation.

#### A8: Traditional big

| Prominent statistic | Direction |
| --- | --- |
| `Blk %` | High |
| `Dunk FGA Freq %` | High |
| `Stl + Blk Per PF` | High |
| `Individual Stop %` | High |
| `Height (in)` | High |
| `Rim 2 Attempt Share %` | High |
| `Non-Rim 2 Assisted %` | High |
| `Paint Pts % Pts` | High |
| `Att1 Attempt Share %` | Low |
| `FGA Freq % Halfcourt` | Low |

**Why this label:** Extreme blocks and dunk frequency, together with height and a rim-heavy shot diet, support a traditional big. A8 is more block/dunk oriented than A1, while A1 has more offensive rebounding.

#### A9: Perimeter scoring wing

| Prominent statistic | Direction |
| --- | --- |
| `% Ast Rim` | High |
| `% Ast3` | Low |
| `% Ast Dunk` | High |
| `3PM % Pts` | High |
| `3P Attempt Share %` | High |
| `Layup FGA Freq %` | Low |
| `Blocked Per FGA` | Low |
| `And1 %` | Low |
| `Shooting Foul Drawn %` | Low |
| `Paint Pts % Pts` | Low |

**Why this label:** High three-point share and low rim involvement support perimeter scoring, with more usage than A4 and A6. Rim/dunk assist shares describe its passes; its own made shots are mostly assisted.
