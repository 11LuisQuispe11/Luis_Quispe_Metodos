# Reproducibility Statement

## Scope

This repository contains revised Markdown deliverables and a synthetic EDA workflow for the course **Research Methods and Scientific Integrity in AI and Advanced Technologies**.

The repository does not contain raw operational data. Synthetic data are generated from verified aggregate statistics for methodological demonstration.

## Reproducible components

| Layer | Implementation |
|---|---|
| Code | Git/GitHub repository with versioned Markdown, scripts, and notebook. |
| Data | Synthetic data generated deterministically from `verified_aggregates.yml`. |
| Experiments | Current stage: EDA only. Future model experiments should be logged with MLflow. |
| Environment | `requirements.txt` provides Python dependencies for the notebook. |
| Reporting | Markdown deliverables, Dataset Datasheet, Model Card, and this statement. |

## How to run the synthetic EDA

From the repository root:

```bash
pip install -r eda/requirements.txt
python eda/src/generate_synthetic_data.py
jupyter notebook eda/notebooks/01_synthetic_eda_blast_truck_crusher.ipynb
```

The notebook should generate synthetic CSV files, figures, and `eda/reports/synthetic_eda_summary.md`.

## Scientific-integrity declaration

The synthetic workflow is not presented as raw-data analysis. It is a reproducible demonstration of the proposed analysis pipeline, traceability audit, and data-documentation structure.

## Future requirements before real modelling

Before any real model claim is made, the project must record:

- authorization record;
- data extraction date;
- data dictionary;
- data hashes or DVC pointers;
- code commit hash;
- package versions;
- MLflow run IDs;
- random seeds;
- hardware and runtime notes;
- leakage-control checklist;
- locked temporal test-set definition.
