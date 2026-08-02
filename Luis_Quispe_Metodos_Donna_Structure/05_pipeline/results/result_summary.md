# Synthetic Pipeline Result Summary

**Scientific status:** Synthetic demonstration only. These are not real mine-performance results.

## Temporal split

- Training: [2024, 2025] (2,109 rows)
- Test: [2026] (516 rows)

## Model comparison

| Model | MAE (kW) | RMSE (kW) | R2 |
|---|---:|---:|---:|
| Historical mean | 283.34 | 359.62 | -0.002 |
| Linear regression | 106.00 | 135.67 | 0.857 |
| HistGradientBoosting | 121.37 | 154.23 | 0.816 |

The pipeline demonstrates temporal splitting, consistent preprocessing, comparable baselines, artifact serialization, and traceable outputs. It does not demonstrate operational validity because all row-level records and target values are synthetic.
