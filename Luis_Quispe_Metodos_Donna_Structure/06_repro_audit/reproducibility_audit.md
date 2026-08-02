# Reproducibility Audit

**Audit object:** `05_pipeline/`  
**Verdict:** GREEN for the synthetic demonstration; AMBER for the proposed real-data scientific claim.

## Audit question

Can an independent user recreate the public synthetic dataset, execute the temporal pipeline, and recover the documented artifacts without confidential mine data?

## Evidence

| Dimension | Evidence | Verdict |
|---|---|---|
| Code | Versioned Python scripts and one-command runner | GREEN |
| Data | Deterministic synthetic generator calibrated to verified aggregates | GREEN |
| Split | 2024-2025 train, 2026 test | GREEN |
| Leakage control | Preprocessing inside pipeline | GREEN |
| Environment | Pinned requirements and Dockerfile | GREEN |
| Data versioning | DVC stages, lock, artifact manifest | GREEN |
| Artifacts | Model, predictions, metrics, chart | GREEN |
| Real-data reproducibility | No authorized row-level dataset hash | AMBER |
| Experiment tracking | No genuine MLflow runs | AMBER |

## Reproduced synthetic result

| Model | MAE (kW) | RMSE (kW) | R2 |
|---|---:|---:|---:|
| Historical mean | 283.34 | 359.62 | -0.002 |
| Linear regression | 106.00 | 135.67 | 0.857 |
| HistGradientBoosting | 121.37 | 154.23 | 0.816 |

These values verify pipeline execution only. They are not operational-performance evidence.

## Stranger test

```bash
cd 05_pipeline
pip install -r requirements.txt
python src/run_pipeline.py
```

## Remaining requirements

1. Immutable restricted-data hash or private DVC reference.
2. Real experiment tracking.
3. Locked final temporal test period.
4. Feature-availability matrix.
5. Independent rerun by another researcher.

## Final judgment

The repository passes the course reproducibility requirement for a public synthetic teaching artifact. The empirical doctoral claim remains AMBER until the real linked cohort and experiment artifacts exist.
