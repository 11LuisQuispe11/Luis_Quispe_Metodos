# Session 5 - Reproducible Synthetic ML Pipeline

## Purpose

This executable pipeline demonstrates the reproducibility controls requested by the course without publishing confidential mine data.

The row-level dataset is synthetic but calibrated to the verified aggregate blast inventory.

## Workflow

1. Generate deterministic synthetic blast-to-crusher records.
2. Split chronologically: 2024-2025 for training and 2026 for testing.
3. Compare historical mean, linear regression, and HistGradientBoosting.
4. Save model, predictions, metrics, chart, DVC lock, and artifact hashes.

## Run

```bash
cd 05_pipeline
pip install -r requirements.txt
python src/run_pipeline.py
```

## Docker

```bash
docker build -t crusher-repro-pipeline .
docker run --rm crusher-repro-pipeline
```

## DVC

```bash
dvc repro
```

## Integrity warning

The generated metrics are valid only for the synthetic demonstration dataset. They are not results from the real mine.
