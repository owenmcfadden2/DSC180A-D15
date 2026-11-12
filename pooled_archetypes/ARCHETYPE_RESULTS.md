# Scouting-Selected Archetype Results

## 1. The eleven roles

| Role | What the profile represents | College anchor seasons |
| --- | --- | --- |
| Initiator PG | Primary handler who organizes the offense and sets up teammates | Braden Smith, Purdue 2024–25. Tyler Kolek, Marquette 2023–24. Jamal Shead, Houston 2023–24. |
| Combo Guard | Secondary handler who can create and contribute off the ball | Jared McCain, Duke 2023–24. Jase Richardson, Michigan State 2024–25. |
| Scoring Guard | Scoring-first perimeter player with a smaller playmaking role | Ace Bailey, Rutgers 2024–25. Antonio Reeves, Kentucky 2023–24. |
| Shooter | Three-point specialist who gets most of his made threes off assists | Isaac McKneely, Louisville 2025–26. Jordan Hawkins, UConn 2022–23. |
| True Wing | Wing who can handle, pass, shoot, and contribute on the glass | Jaime Jaquez Jr., UCLA 2022–23. Jalen Williams, Santa Clara 2021–22. Pelle Larsson, Arizona 2023–24. |
| Off-Ball Wing/4 | Defense-first wing or forward who cuts, spots up, and rebounds | Jordan Walsh, Arkansas 2022–23. Carter Bryant, Arizona 2024–25. Ryan Dunn, Virginia 2023–24. |
| Stretch 4 | Forward who spaces the floor and contributes as a rebounder | Jabari Smith Jr., Auburn 2021–22. Rasheer Fleming, Saint Joseph’s 2024–25. |
| Bruiser 4 | Physical forward who runs the floor, finishes inside, and rebounds | Coen Carr, Michigan State 2024–25. Tari Eason, LSU 2021–22. |
| Small Ball Big | Smaller big who handles interior work and adds passing or spacing | Jaylin Williams, Arkansas 2021–22. Isaiah Mobley, USC 2021–22. |
| True 5 | Interior center whose profile emphasizes finishing, rebounding, and rim protection | Zach Edey, Purdue 2023–24. Armando Bacot, UNC 2023–24. Ryan Kalkbrenner, Creighton 2022–23. |
| Stretch 5 | Center who takes threes regularly and still contributes inside | Kyle Filipowski, Duke 2023–24. Quinten Post, Boston College 2023–24. Amaël L’Etang, Dayton 2025–26. |

## 2. Results for players we reviewed

The earlier column uses the group-weighted fit with one example per role and the three-attempt minimum for Stretch 5. The pooled column uses the eleven profiles above, the distance penalty, and the current eligibility rules.

| Player-season | Earlier largest role | Pooled largest role |
| --- | --- | --- |
| Henri Veesaar, 2025–26 | Off-Ball Wing/4, 35.9% | Stretch 5, 50.9% |
| Maxime Raynaud, 2024–25 | Stretch 4, 38.0% | Stretch 5, 60.8% |
| Donovan Clingan, 2023–24 | True 5, 41.5% | True 5, 67.3% |
| Ryan Kalkbrenner, 2024–25 | True 5, 39.2% | True 5, 79.4% |
| Aniwaniwa Tait-Jones, 2024–25 | True Wing, 61.1% | True Wing, 79.9% |
| Nordin Kapic, 2024–25 | Scoring Guard, 27.7% | Stretch 4, 49.8% |
| Bol Dengdit, 2025–26 | Shooter, 26.5% | True Wing, 25.7% |
| Hudson Mayes, 2025–26 | True Wing, 29.2% | Small Ball Big, 35.6% |
| Cooper Flagg, 2024–25 | True Wing, 40.4% | Stretch 4, 46.4% |

Veesaar’s Stretch 5 share rose from 7.6% to 50.9%. Clingan remains at 0% Stretch 5 after the shooting eligibility check. Kalkbrenner’s 2024–25 season gets 0% Stretch 5 under the 15% shot-share minimum.

Bol’s True Wing share is close to his True 5 share (25.2%), with another 16.3% Stretch 5. His shooting and passing contribute to the wing and spacing parts of the fit. His 14.5% defensive rebound rate was below all three Stretch 5 anchors.

## 3. Interpretation limits

The role weights are shares of a statistical reconstruction. Bol’s half-point lead illustrates how a top label can hide a mixed profile. Mayes’s Small Ball Big share and Flagg’s Stretch 4 and Initiator PG mix remain cases to review.

We used these player examples to guide the model changes. Veesaar’s season was outside the anchor pools, and his result informed the tuning. The comparison is descriptive. It has no independent test of role accuracy. Related stats can still influence the fit through different groups, and median-filled rates can affect profiles when a player has few opportunities.

## 4. Standardized role profiles

Each profile is the average of its selected player-seasons. The tables list the ten largest absolute z-scores for each role. A score of +1.00 is one standard deviation above the pooled player-season mean, and −1.00 is one below. These are profile values before the fit applies equal stat-group weights. The ranked stats describe the examples we selected and can reveal traits they share beyond the role definition.

### Initiator PG

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `% Of Team Ast` | High | +4.38 |
| `Ast %` | High | +4.17 |
| `Alley-Oop Ast/40` | High | +3.31 |
| `Stl + Blk Per PF` | High | +3.25 |
| `% Of Team TO` | High | +2.81 |
| `Ast/TO` | High | +2.74 |
| `Stl %` | High | +2.06 |
| `3PM Assisted %` | Low | -1.69 |
| `% Of Team FGA` | High | +1.53 |
| `Individual Stop %` | High | +1.42 |

### Combo Guard

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `TO %` | Low | -1.19 |
| `Fast Break Pts % Pts` | High | +1.15 |
| `Ast/TO` | High | +1.12 |
| `Transition Shot %` | High | +1.02 |
| `Blk Rcv %` | High | +1.02 |
| `Alley-Oop Ast/40` | High | +1.02 |
| `% Ast Dunk` | High | +1.01 |
| `PF %` | Low | -1.01 |
| `% Ast Paint` | High | +0.82 |
| `Blocked Per FGA` | Low | -0.81 |

### Scoring Guard

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `% Of Team FGA` | High | +1.93 |
| `Usage %` | High | +1.48 |
| `% Ast Paint` | High | +1.37 |
| `TO %` | Low | -1.17 |
| `% Of Team FTA` | High | +0.93 |
| `Transition Shot %` | High | +0.88 |
| `Layup FGA Freq %` | Low | -0.80 |
| `% Of Team TO` | High | +0.75 |
| `Rim 2 Attempt Share %` | Low | -0.68 |
| `PF %` | Low | -0.66 |

### Shooter

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `3P Attempt Share %` | High | +1.56 |
| `3PM % Pts` | High | +1.54 |
| `Paint Pts % Pts` | Low | -1.37 |
| `Layup FGA Freq %` | Low | -1.29 |
| `% Ast Dunk` | High | +1.28 |
| `TO %` | Low | -1.23 |
| `Rim 2 Attempt Share %` | Low | -1.18 |
| `Blocked Per FGA` | Low | -0.97 |
| `% Of Team FGA` | High | +0.95 |
| `PF %` | Low | -0.86 |

### True Wing

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `% Of Team FGA` | High | +1.43 |
| `% Of Team FTA` | High | +1.25 |
| `% Of Team TO` | High | +1.19 |
| `Alley-Oop Ast/40` | High | +1.17 |
| `% Of Team Ast` | High | +1.14 |
| `Ast %` | High | +0.98 |
| `Ast/TO` | High | +0.95 |
| `Usage %` | High | +0.93 |
| `% Ast Dunk` | High | +0.87 |
| `% Ast Rim` | High | +0.84 |

### Off-Ball Wing/4

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `Individual Stop %` | High | +2.03 |
| `Blk %` | High | +1.87 |
| `Stl + Blk Per PF` | High | +1.63 |
| `% Ast Dunk` | High | +1.50 |
| `Dunk FGA Freq %` | High | +1.15 |
| `Stl %` | High | +1.13 |
| `Rim Assisted %` | High | +1.02 |
| `DReb %` | High | +0.84 |
| `Ast %` | Low | -0.71 |
| `3PM Assisted %` | High | +0.62 |

### Stretch 4

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `DReb %` | High | +2.10 |
| `Stl + Blk Per PF` | High | +1.82 |
| `% Of Team FGA` | High | +1.19 |
| `% Of Team FTA` | High | +1.13 |
| `Individual Stop %` | High | +1.11 |
| `Blk %` | High | +1.09 |
| `Usage %` | High | +1.03 |
| `Off Fouls Drawn %` | Low | -0.77 |
| `TO %` | Low | -0.73 |
| `Layup FGA Freq %` | Low | -0.69 |

### Bruiser 4

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `Dunk FGA Freq %` | High | +2.86 |
| `FGA Freq % Halfcourt` | Low | -2.35 |
| `Transition Shot %` | High | +2.12 |
| `Fast Break Pts % Pts` | High | +2.12 |
| `Stl + Blk Per PF` | High | +1.89 |
| `Individual Stop %` | High | +1.49 |
| `Shooting Foul Drawn %` | High | +1.48 |
| `Blk %` | High | +1.43 |
| `Stl %` | High | +1.40 |
| `Rim 2 Attempt Share %` | High | +1.30 |

### Small Ball Big

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `Off Fouls Drawn %` | High | +2.61 |
| `DReb %` | High | +2.29 |
| `Individual Stop %` | High | +1.35 |
| `Ffl Drawn %` | High | +1.23 |
| `And1 %` | High | +1.21 |
| `% Of Team FTA` | High | +1.10 |
| `FT Ratio` | Low | -1.09 |
| `% Of Team Ast` | High | +1.09 |
| `Fouls Drawn Per FGA` | High | +1.02 |
| `Stl + Blk Per PF` | High | +1.01 |

### True 5

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `Ffl Drawn %` | High | +2.98 |
| `% Of Team FTA` | High | +2.54 |
| `OReb %` | High | +2.14 |
| `Dunk FGA Freq %` | High | +2.10 |
| `Stl + Blk Per PF` | High | +2.10 |
| `Blk %` | High | +1.82 |
| `DReb %` | High | +1.60 |
| `Shooting Foul Drawn %` | High | +1.58 |
| `Non-Rim 2 Assisted %` | High | +1.53 |
| `Rim 2 Attempt Share %` | High | +1.47 |

### Stretch 5

| Prominent statistic | Direction | Z-score |
| --- | --- | ---: |
| `% Of Team TO` | High | +1.81 |
| `DReb %` | High | +1.80 |
| `Blk %` | High | +1.74 |
| `Ffl Drawn %` | High | +1.65 |
| `Usage %` | High | +1.41 |
| `% Of Team FTA` | High | +1.28 |
| `% Of Team FGA` | High | +1.24 |
| `Fast Break Pts % Pts` | Low | -1.17 |
| `Transition Shot %` | Low | -1.10 |
| `Individual Stop %` | High | +0.89 |
