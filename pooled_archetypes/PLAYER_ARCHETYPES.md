# Player Archetypes with Scouting-Selected Profiles

This experiment describes college basketball playing styles using eleven profiles chosen from college player-seasons. Each player-season receives a mixture of role weights. The original comparison learned its profiles from the sample and assigned basketball labels after fitting. Here we define the roles and choose their examples first.

## 1. Files and reading order

| File | Purpose |
| --- | --- |
| [Preparation and fit notebook](notebooks/01_player_archetypes_eda.ipynb) | Prepare the inputs from the shared data, fit the eleven roles, and export player percentages. |
| [Model script](scripts/fit_pooled_roles.py) | Specify the role pools and stat groups, apply eligibility rules, and solve for mixture weights. |
| [Results](ARCHETYPE_RESULTS.md) | Review the role pools, player examples, and interpretation limits. |
| [Player archetype weights](results/player_archetype_results.csv) | Browse the eleven fitted role weights and top three roles for each eligible player-season. |

## 2. Data and preparation

The notebook uses the same source and sample rules as the [earlier comparison](../PLAYER_ARCHETYPES.md). It keeps player-seasons from 2021–22 onward with at least 200 total minutes. The analyzed snapshot contains 16,723 player-seasons through 2025–26.

We reconstruct usage, assist, offensive rebound, defensive rebound, and block rates from counts. Derived shot shares use matched classified attempts. We fill missing values with the observed feature median, preserve the missingness mask, and standardize each input across the sample.

The fit starts from the earlier 45-feature style set and uses 43 stats. Height controls center eligibility, and we drop `Pts Created/40` because it combines scoring and playmaking. Each of the eight stat groups has equal total weight. The stats within a group split that weight evenly. The model script lists all 43 stats by group.

## 3. Fit and interpret the mixtures

Each role profile is the mean of the standardized stat lines of its two or three selected player-seasons. The model fits nonnegative role weights that add to 100%. It minimizes weighted reconstruction error plus 0.20 times the mixture-weighted squared distances to the individual role profiles. This term favors profiles that are individually closer to the player.

| Role | Eligibility |
| --- | --- |
| Small Ball Big | At most 6′10″ |
| True 5 | At least 6′10″ |
| Stretch 5 | At least 6′10″, at least 3 three-point attempts per 100 possessions, and at least 15% of classified attempts from three |

The other eight roles are open to all players in the sample. Three-point volume per 100 possessions is calculated from source `3PA` and `Poss`. At exactly 6′10″, a player can qualify for Small Ball Big and True 5, as well as Stretch 5 if they meet its shooting minimums.

## 4. Reproduce the results

Use Python 3.12 and configure the shared data path as described in [SETUP.md](../SETUP.md). From the repository root, install the dependencies in your analysis environment and register its notebook kernel.

```bash
python -m pip install -r requirements-archetypes.txt
python -m ipykernel install --user --name capstone --display-name "Python (capstone)"
```

Run the [notebook](notebooks/01_player_archetypes_eda.ipynb) top to bottom. It exports player, season, team, position, class, all eleven percentages, and the three largest roles to `local_outputs/pooled_archetypes/results/player_archetype_results.csv`. It also saves a missingness mask under the same gitignored analysis folder. The branch contains the notebook with cleared outputs.
