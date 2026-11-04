"""03: Archetypal Analysis, 45-Feature Variant

Run after notebooks/01_player_archetypes_eda.ipynb:
    python scripts/03_archetypes_style_variant.py

Use --k 9 to inspect the nine-archetype model only. All generated artifacts are private.
"""

# %% 1. Setup
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
from threadpoolctl import threadpool_limits
from archetypes import AA

REPO_ROOT = Path(__file__).resolve().parents[1]
PREPARED = REPO_ROOT / "local_outputs/archetype_comparison/prepared"
DATASET = "style_variant"
OUT = REPO_ROOT / "local_outputs/archetype_comparison/models" / DATASET
SEEDS = [42, 43, 44]
COUNTS = list(range(6, 13))
MAX_ITER = 500
RELATIVE_TOL = 1e-5
METHOD_PARAMS = {"max_iter_optimizer": 1000, "const": 100.0}
WORKING_LABELS = {
    'A1': 'Offensive rebounder',
    'A2': 'Lead guard',
    'A3': 'Connective wing',
    'A4': 'Three-point specialist',
    'A5': 'Scoring wing',
    'A6': 'Low-usage floor spacer',
    'A7': 'Defensive / transition player',
    'A8': 'Traditional big',
    'A9': 'Perimeter scoring wing',
}


# %% 2. Fit and validate one count
def fit_count(X, k, record_ids, features, metadata):
    folder = OUT / f"k{k:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    tss = float(np.square(X).sum())
    runs = []
    arrays = []
    for seed in SEEDS:
        # This package version uses absolute RSS-change stopping, so express the
        # tolerance relative to total variation for a comparable two-dataset test.
        with threadpool_limits(limits=2):
            model = AA(
                n_archetypes=k, method="nnls", init="uniform", n_init=1,
                random_state=seed, max_iter=MAX_ITER, tol=RELATIVE_TOL * tss,
                method_params=METHOD_PARAMS,
            ).fit(X)
        A, B, Z = model.A_, model.B_, model.archetypes_
        assert all(np.isfinite(v).all() for v in [A, B, Z])
        assert A.min() >= 0 and B.min() >= 0
        assert np.allclose(A.sum(axis=1), 1) and np.allclose(B.sum(axis=1), 1)
        assert np.allclose(B @ X, Z)
        rss = float(np.square(X - A @ Z).sum())
        assert np.isclose(rss, model.rss_)
        loss = np.asarray(model.loss_, dtype=float)
        run = {
            "seed": seed, "rss": rss, "rss_fraction": rss / tss,
            "iterations": int(model.n_iter_),
            "stopping_criterion_met": bool(abs(loss[-1] - loss[-2]) < RELATIVE_TOL * tss),
            "final_above_best_iteration_fraction": float((loss[-1] - loss.min()) / tss),
        }
        runs.append(run)
        arrays.append((A.copy(), B.copy(), Z.copy()))
        np.savez_compressed(folder / f"seed{seed}.npz", A=A, B=B, Z=Z, loss=loss,
                            record_ids=record_ids, feature_names=features)
        print(f"{DATASET}: K={k}, seed={seed}, RSS/TSS={rss / tss:.4f}", flush=True)

    # The package can reach different local solutions; retain every initialization.
    best_index = min(range(len(runs)), key=lambda i: runs[i]["rss"])
    A, B, Z = arrays[best_index]
    stability = []
    for i, (other_A, _, other_Z) in enumerate(arrays):
        if i == best_index:
            continue
        cost = cdist(Z, other_Z, metric="sqeuclidean") / X.shape[1]
        rows, cols = linear_sum_assignment(cost)
        stability.append({
            "other_seed": SEEDS[i],
            "profile_rms_sd": float(np.sqrt(cost[rows, cols].mean())),
            "mixture_l1": float(np.abs(A - other_A[:, cols]).sum(axis=1).mean()),
        })

    # Original statistical units make the archetypes easier to interpret.
    parameters = metadata["parameters"]
    means = np.array([parameters[c]["mean"] for c in features])
    scales = np.array([parameters[c]["scale"] for c in features])
    names = [f"A{i + 1}" for i in range(k)]
    profile_index = pd.Index(names, name="archetype")
    pd.DataFrame(Z, index=profile_index, columns=features).to_csv(folder / "profiles_standardized.csv")
    profiles = pd.DataFrame(Z * scales + means, index=profile_index, columns=features)
    profiles.to_csv(folder / "profiles_original_units.csv")
    mixtures = pd.DataFrame(A, index=pd.Index(record_ids, name="Record ID"), columns=names)
    mixtures["dominant_archetype"] = np.array(names)[A.argmax(axis=1)]
    if k == 9:
        mixtures["working_label"] = mixtures["dominant_archetype"].map(WORKING_LABELS)
    mixtures.to_csv(folder / "player_mixtures.csv")

    # Interpretive fields do not enter the fit. B projects them onto the archetypes.
    interpretation = pd.read_csv(PREPARED / "interpretation.csv").set_index("Record ID").loc[record_ids]
    observed_assistance = interpretation["Assisted Makes %"].to_numpy()
    assert np.isfinite(observed_assistance).all()
    profiles["Made FGs assisted %"] = B @ observed_assistance
    profiles.to_csv(folder / "profiles_with_interpretation.csv")
    mask = pd.read_csv(PREPARED / "missingness_mask.csv").set_index("Record ID").loc[record_ids, features]
    influence = pd.DataFrame(B @ mask.to_numpy(), index=profile_index, columns=features)
    influence.to_csv(folder / "imputation_influence.csv")

    records = pd.read_csv(PREPARED / "records.csv").set_index("Record ID").loc[record_ids]
    examples = []
    for j, name in enumerate(names):
        for rank, row in enumerate(np.argsort(-A[:, j])[:10], 1):
            examples.append({"archetype": name, "rank": rank, "Record ID": record_ids[row],
                             "mixture_weight": float(A[row, j]), **records.iloc[row].to_dict()})
    pd.DataFrame(examples).to_csv(folder / "closest_players.csv", index=False)
    summary = {
        "dataset": DATASET, "k": k, "best_seed": SEEDS[best_index],
        "rss_fraction": runs[best_index]["rss_fraction"],
        "profile_rms_sd": float(np.mean([s["profile_rms_sd"] for s in stability])),
        "mixture_l1": float(np.mean([s["mixture_l1"] for s in stability])),
        "all_runs_stopped": all(r["stopping_criterion_met"] for r in runs),
        "runs": runs, "initialization_stability": stability,
    }
    (folder / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


# %% 3. Run the comparison and save its provenance
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, nargs="+", default=COUNTS, help="Counts to fit (default: 6 through 12)")
    args = parser.parse_args()
    if any(k < 6 for k in args.k):
        parser.error("This experiment starts at six archetypes")
    metadata = json.loads((PREPARED / "preprocessing.json").read_text())
    input_path = PREPARED / f"{DATASET}_standardized.npz"
    with np.load(input_path, allow_pickle=False) as data:
        X, record_ids, features = data["X"], data["record_ids"], data["feature_names"]
    assert features.tolist() == metadata["feature_columns"][DATASET]
    assert np.isfinite(X).all()
    assert len(set(record_ids)) == len(record_ids)
    assert np.allclose(X.mean(axis=0), 0, atol=1e-10)
    assert np.allclose(X.std(axis=0), 1, atol=1e-10)
    OUT.mkdir(parents=True, exist_ok=True)
    summaries = [fit_count(X, k, record_ids, features, metadata) for k in args.k]
    comparison = pd.DataFrame([
        {k: v for k, v in summary.items() if k not in ["runs", "initialization_stability"]}
        for summary in summaries
    ])
    comparison.to_csv(OUT / "model_comparison.csv", index=False)
    provenance = {
        "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "source_sha256": metadata["source_sha256"], "dataset": DATASET,
        "rows": len(X), "features": len(features), "counts": args.k, "seeds": SEEDS,
        "method": "nnls", "init": "uniform", "max_iter": MAX_ITER,
        "tolerance_fraction_tss": RELATIVE_TOL, "method_params": METHOD_PARAMS,
    }
    (OUT / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(comparison.to_string(index=False))


# %% Notes
# - Initialization stability is not bootstrap or preprocessing stability.
# - Archetype labels are display notes for K=9, not hard cluster assignments.
# - Some NNLS loss histories are nonmonotone; inspect all starts and their histories.
# - Original units include fractions, percentages, per-40 rates and ratios.
# - Missingness, player examples, profiles and arrays stay in ignored local outputs.
if __name__ == "__main__":
    main()
