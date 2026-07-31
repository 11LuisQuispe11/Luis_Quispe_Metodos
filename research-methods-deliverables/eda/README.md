# Synthetic EDA for Blast-to-Truck-to-Crusher Traceability

This folder contains a reproducible supporting notebook for the Dataset Datasheet and Model Card.

## Integrity note

The EDA does not use raw operational records. It generates synthetic data calibrated from verified aggregate statistics.

## Run

```bash
pip install -r requirements.txt
python eda/src/generate_synthetic_data.py
jupyter notebook eda/notebooks/01_synthetic_eda_blast_truck_crusher.ipynb
```

## Output

The workflow creates synthetic CSV files, figures, and a Markdown EDA summary.
