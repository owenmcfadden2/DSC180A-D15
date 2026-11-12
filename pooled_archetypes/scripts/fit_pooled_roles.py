"""Fit player mixtures against the eleven scouting-selected profiles."""

import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits


STYLE_GROUPS = {
    "Offensive load and ball security": ["Usage %", "% Of Team FGA", "% Of Team FTA", "TO %", "% Of Team TO"],
    "Playmaking": ["Ast %", "Ast/TO", "% Of Team Ast", "% Ast Rim", "% Ast Paint", "% Ast Dunk", "% Ast3", "Alley-Oop Ast/40"],
    "Shot selection and context": ["Rim 2 Attempt Share %", "3P Attempt Share %", "Dunk FGA Freq %", "Layup FGA Freq %",
                                   "Transition Shot %", "FGA Freq % Halfcourt", "Att1 Attempt Share %"],
    "Assisted scoring": ["3PM Assisted %", "Rim Assisted %", "Non-Rim 2 Assisted %"],
    "Scoring distribution": ["3PM % Pts", "Paint Pts % Pts", "Fast Break Pts % Pts", "2nd Chance Pts % Pts"],
    "Contact and foul drawing": ["FT Rate", "FT Ratio", "Fouls Drawn Per FGA", "Shooting Foul Drawn %",
                                 "Ffl Drawn %", "Off Fouls Drawn %", "And1 %", "Blocked Per FGA"],
    "Rebounding": ["OReb %", "DReb %", "Blk Rcv %"],
    "Defense": ["Stl %", "Blk %", "Individual Stop %", "PF %", "Stl + Blk Per PF"],
}
ANCHORS = {
    'Initiator PG': [('Braden Smith', '2024-25', None), ('Tyler Kolek', '2023-24', None), ('Jamal Shead', '2023-24', None)],
    'Combo Guard': [('Jared McCain', '2023-24', None), ('Jase Richardson', '2024-25', None)],
    'Scoring Guard': [('Ace Bailey', '2024-25', None), ('Antonio Reeves', '2023-24', None)],
    'Shooter': [('Isaac McKneely', '2025-26', None), ('Jordan Hawkins', '2022-23', None)],
    'True Wing': [('Jaime Jaquez Jr.', '2022-23', None), ('Jalen Williams', '2021-22', None), ('Pelle Larsson', '2023-24', None)],
    'Off-Ball Wing/4': [('Jordan Walsh', '2022-23', None), ('Carter Bryant', '2024-25', None), ('Ryan Dunn', '2023-24', None)],
    'Stretch 4': [('Jabari Smith', '2021-22', None), ('Rasheer Fleming', '2024-25', None)],
    'Bruiser 4': [('Coen Carr', '2024-25', None), ('Tari Eason', '2021-22', None)],
    'Small Ball Big': [('Jaylin Williams', '2021-22', 'Arkansas'), ('Isaiah Mobley', '2021-22', None)],
    'True 5': [('Zach Edey', '2023-24', None), ('Armando Bacot', '2023-24', None), ('Ryan Kalkbrenner', '2022-23', None)],
    'Stretch 5': [('Kyle Filipowski', '2023-24', None), ('Quinten Post', '2023-24', None), ("Amael L'Etang", '2025-26', None)],
}


def project_simplex(values):
    sorted_values = np.sort(values, axis=1)[:, ::-1]
    count = np.arange(1, values.shape[1] + 1)
    offsets = (sorted_values.cumsum(axis=1) - 1) / count
    active = (sorted_values > offsets).sum(axis=1) - 1
    threshold = offsets[np.arange(len(values)), active]
    return np.maximum(values - threshold[:, None], 0)


def fit_mixtures(players, profiles, distance_penalty=0.0):
    gram = profiles @ profiles.T
    cross = players @ profiles.T
    if distance_penalty:
        # The player norm is constant because the mixture weights sum to one.
        squared_distances = gram.diagonal() - 2 * cross
        cross = cross - 0.5 * distance_penalty * squared_distances
    step = 1 / np.linalg.eigvalsh(gram)[-1]
    weights = np.full_like(cross, 1 / len(profiles))
    momentum = weights.copy()
    for iteration in range(1, 2001):
        updated = project_simplex(momentum - step * (momentum @ gram - cross))
        momentum = updated + (iteration - 1) / (iteration + 2) * (updated - weights)
        weights = updated
        if iteration % 25 == 0:
            residual = project_simplex(weights - step * (weights @ gram - cross)) - weights
            if np.abs(residual).max() < 1e-8:
                break
    else:
        raise RuntimeError("Mixture optimization did not converge")
    if not np.allclose(weights.sum(axis=1), 1) or (weights < 0).any():
        raise ValueError("Invalid mixture weights")
    return weights


def fit_roles(standardized, records, height, three_attempt_share, three_attempts_per_100):
    """Return percentage weights and weighted squared errors for each player-season."""
    stat_weights = pd.Series({
        stat: 1 / len(group) for group in STYLE_GROUPS.values() for stat in group
    })
    scaled = standardized[stat_weights.index].mul(np.sqrt(stat_weights), axis="columns")
    profiles = []
    for role, pool in ANCHORS.items():
        ids = []
        for name, season, team in pool:
            matches = records["Player"].eq(name) & records["Season"].eq(season)
            if team is not None:
                matches &= records["Team"].eq(team)
            if matches.sum() != 1:
                raise ValueError(f"Expected one player-season for {role}: {name}, {season}")
            ids.append(records.index[matches][0])
        profiles.append(scaled.loc[ids].mean(axis=0).to_numpy())

    roles = list(ANCHORS)
    eligible = np.ones((len(records), len(roles)), dtype=bool)
    eligible[:, roles.index("True 5")] = height.ge(82)
    eligible[:, roles.index("Stretch 5")] = (
        height.ge(82) & three_attempts_per_100.ge(3) & three_attempt_share.ge(15)
    )
    eligible[:, roles.index("Small Ball Big")] = height.le(82)

    players = scaled.to_numpy()
    profiles = np.stack(profiles)
    weights = np.zeros(eligible.shape)
    with threadpool_limits(limits=2):
        for allowed in np.unique(eligible, axis=0):
            rows = (eligible == allowed).all(axis=1)
            weights[np.ix_(rows, allowed)] = fit_mixtures(
                players[rows], profiles[allowed], distance_penalty=0.20
            )
    if not np.allclose(weights.sum(axis=1), 1) or (weights[~eligible] != 0).any():
        raise ValueError("Invalid role weights")
    error = np.square(players - weights @ profiles).sum(axis=1)
    return pd.DataFrame(100 * weights, index=records.index, columns=roles), error
