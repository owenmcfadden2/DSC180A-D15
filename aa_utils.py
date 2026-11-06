"""Helpers for the archetype notebooks (v2). Keep next to the .ipynb files."""
import re
import numpy as np
import pandas as pd

ZONES = ["Rim", "Paint", "Midrange", "Corner 3", "Above Break 3"]


# ----------------------------------------------------------------------------- integrity
def precision_audit(df, max_unique=12):
    """Rate-like columns with suspiciously few distinct values (rounded fractions)."""
    num = df.select_dtypes("number")
    cols = [c for c in num.columns if re.search(r"%|Rate|Ratio|Usage", c)]
    out = pd.DataFrame({
        "nunique": num[cols].nunique(),
        "min": num[cols].min(),
        "median": num[cols].median(),
        "max": num[cols].max(),
        "share_zero": (num[cols] == 0).mean().round(3),
        "coverage": num[cols].notna().mean().round(3),
    })
    return out[out["nunique"] <= max_unique].sort_values("nunique")


def _div(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        r = a / b
    return r.replace([np.inf, -np.inf], np.nan)


def derive_rates(df):
    """Recompute core rate stats from counts. Several candidates where the
    CBB Analytics field definitions are ambiguous; pick with compare_derived()."""
    on = _div(df["Min"], df["Team Min / 5"])            # share of team minutes on floor
    d = pd.DataFrame(index=df.index)
    d["usg_box"] = 100 * _div(df["FGA"] + 0.44 * df["FTA"] + df["TO"],
                              on * (df["FGA Team"] + 0.44 * df["FTA Team"] + df["TO Team"]))
    d["ast_box"] = 100 * _div(df["Ast"], on * df["FGM Team"] - df["FGM"])
    d["oreb_chances"] = 100 * _div(df["OReb FG"] + df["OReb FT"], df["OReb FG Chances"] + df["OReb FT Chances"])
    d["oreb_box"] = 100 * _div(df["OReb"], on * (df["OReb Team"] + df["DReb Opp"]))
    d["dreb_chances"] = 100 * _div(df["DReb FG"] + df["DReb FT"], df["DReb FG Chances"] + df["DReb FT Chances"])
    d["dreb_box"] = 100 * _div(df["DReb"], on * (df["DReb Team"] + df["OReb Opp"]))
    d["blk_box"] = 100 * _div(df["Blk"], on * (df["FGA Opp"] - df["3PA Opp"]))
    d["blk_dposs"] = 100 * _div(df["Blk"], df["D Poss"])
    d["stl_dposs"] = 100 * _div(df["Stl"], df["D Poss"])
    d["stl_box"] = 100 * _div(df["Stl"], on * df["D Poss Team"])
    return d


DERIVED_TARGET = {  # derived candidate prefix -> stored column, plausible D1 median range (percent units)
    "usg": ("Usage %", (15, 25)),
    "ast": ("Ast %", (8, 20)),
    "oreb": ("OReb %", (3, 10)),
    "dreb": ("DReb %", (10, 20)),
    "blk": ("Blk %", (0.5, 5)),
    "stl": ("Stl %", (1, 3)),
}


def compare_derived(df, derived):
    rows = []
    for c in derived:
        stored, (lo, hi) = DERIVED_TARGET[c.split("_")[0]]
        med = derived[c].median()
        rows.append({"derived": c, "stored": stored,
                     "r_vs_stored": derived[c].corr(df[stored]) if stored in df else np.nan,
                     "median": med, "p01": derived[c].quantile(.01), "p99": derived[c].quantile(.99),
                     "coverage": derived[c].notna().mean(), "median_plausible": lo <= med <= hi})
    return pd.DataFrame(rows).round(3)


def pick_derived(table):
    """Best candidate per stat: plausible median first, then highest r with stored."""
    t = table.assign(stat=table["derived"].str.split("_").str[0])
    t = t.sort_values(["stat", "median_plausible", "r_vs_stored"], ascending=[True, False, False])
    return t.groupby("stat").head(1).set_index("stat")["derived"].to_dict()


# ----------------------------------------------------------------------------- transforms
def shrink_rate(num, den, prior, m):
    """Empirical-Bayes style shrink of num/den toward prior with m pseudo-attempts."""
    return (num + m * prior) / (den + m)


def zone_shares(df, m=20, by="Season"):
    """Shot-zone shares from counts, shrunk toward the season mix (no zeros, so clr is safe)."""
    cnt = df[[f"{z} FGA" for z in ZONES]].astype(float).fillna(0)
    cnt.columns = ZONES
    tot = cnt.sum(axis=1)
    prior = cnt.groupby(df[by]).transform("sum")
    prior = prior.div(prior.sum(axis=1), axis=0)
    return (cnt + m * prior).div(tot + m, axis=0)


def clr(shares, prefix="clr_"):
    lz = np.log(shares)
    return lz.sub(lz.mean(axis=1), axis=0).add_prefix(prefix)


def season_z(frame, season):
    return frame.groupby(season).transform(lambda s: (s - s.mean()) / s.std(ddof=0))


def robust_extreme_share(X, groups, thresh=4):
    rz = (X - X.median()) / (X.quantile(.75) - X.quantile(.25)).replace(0, np.nan)
    return (rz.abs() > thresh).any(axis=1).groupby(groups, observed=True).mean()



def match_archetypes(Z1, Z2):
    """Hungarian match of two archetype sets; returns order for Z2 and per-pair distance."""
    from scipy.optimize import linear_sum_assignment
    D = np.linalg.norm(Z1[:, None, :] - Z2[None, :, :], axis=2)
    r, c = linear_sum_assignment(D)
    return c, D[r, c]
