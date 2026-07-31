# Dataset Datasheet — Synthetic Demonstration and Verified Aggregate Inventory

**Project:** Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data  
**Student:** Luis Quispe Inquil  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies  
**Institution:** Universidad Nacional Mayor de San Marcos  
**Status:** Pre-modelling dataset documentation; synthetic row-level demonstration with verified aggregate calibration.

## 1. Dataset identity

This datasheet documents the dataset concept used in the research protocol and the synthetic demonstration dataset included in this repository. The repository does not contain raw operational records. It contains synthetic row-level data generated from verified aggregate statistics.

## 2. Motivation

The dataset supports the design and evaluation of a traceable, uncertainty-aware, adaptive, and explainable artifact for predicting primary-crusher energy demand from blast-design and material-traceability information.

## 3. Verified aggregate evidence

The real evidence used to calibrate the synthetic demonstration is limited to non-identifying aggregate statistics:

| Year | Unique fired blasts | Blast-hole records | Blast-size range | Mean holes/blast | Median holes/blast |
|---:|---:|---:|---:|---:|---:|
| 2024 | 1,070 | 154,821 | 1–907 | 144.69 | 112 |
| 2025 | 1,039 | 180,018 | 4–1,297 | 173.26 | 140 |
| 2026 to 17 June | 516 | 77,704 | 4–779 | 150.59 | 123 |

Total verified analytical period: **1 January 2024 to 17 June 2026**.  
Total unique fired blasts: **2,625**.  
Total blast-hole records: **412,543**.  
Weighted mean holes per blast: **157.16**.

## 4. What the synthetic dataset contains

The synthetic dataset is generated only for reproducibility, documentation, and methodological demonstration.

| Synthetic table | Unit of analysis | Purpose |
|---|---|---|
| `synthetic_blasts.csv` | Blast event | Demonstrates blast-level inventory and distribution of holes per blast. |
| `synthetic_truck_cycles.csv` | Truck cycle | Demonstrates linkage through `blast_name`, `LOADID`, payload, dump timestamp, and crusher destination. |
| `synthetic_crusher_signals.csv` | Time-stamped crusher signal | Demonstrates historian-quality checks, operating-state filtering, and power-window aggregation. |

## 5. What is not included

The repository excludes:

- raw blast-design records;
- raw truck-cycle records;
- raw crusher-historian values;
- real X/Y/Z coordinates;
- real mine name;
- real source-system name;
- real truck, shovel, operator, and equipment identifiers;
- credentials, IP addresses, screenshots, or system exports.

## 6. Recommended uses

This dataset may be used to:

- demonstrate a reproducible data workflow;
- test notebook execution;
- document traceability-confidence logic;
- prepare the Model Card and protocol appendices;
- demonstrate scientific-integrity controls when raw data cannot be shared.

## 7. Prohibited uses

This dataset must not be used to:

- infer actual mine performance;
- estimate true crusher energy demand;
- report operational KPIs;
- identify the mine, source systems, or equipment;
- train a production model.

## 8. Collection and generation process

Verified aggregate statistics were obtained from operational systems before access was discontinued. The synthetic tables are generated using deterministic Python scripts with a fixed random seed. Synthetic values are designed to be structurally plausible, not operationally factual.

## 9. Data quality and limitations

The synthetic data intentionally includes missingness, ambiguous traceability, stockpile-origin records, and historian-quality flags to demonstrate audit logic. These patterns are simulated and should not be interpreted as measured defect rates.

## 10. Ethical and legal considerations

The research design uses anonymous, aggregated, and non-identifying academic information. The repository does not publish confidential data. Any future use of raw operational records must follow institutional authorization, anonymization, access control, retention rules, and publication restrictions.

## 11. Maintenance

If verified aggregate counts change, update `eda/config/verified_aggregates.yml`, regenerate the synthetic data, rerun the notebook, and commit the new outputs with a clear change message.
