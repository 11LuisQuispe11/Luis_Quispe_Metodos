# Research Protocol v0.1 - Archived Structured Draft

**Student:** Luis Quispe Inquil  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies  
**Status:** Archived first structured protocol; superseded by `protocol_v1.0.md`

## Provenance note

This version records the first structured protocol developed after the initial six-page proposal and before the operational-data inventory was verified. It is retained to make the audit-then-revise cycle visible. Statements about data access in this archived version were provisional.

## 1. Working title

**Hybrid Prediction of Primary-Crusher Energy Demand from Blast-Design Data Using Probabilistic, Adaptive, and Interpretable Machine Learning**

## 2. Problem statement

Open-pit mining operations produce blast-design, geological, geomechanical, haulage, and plant-historian information, yet the information is often stored in separate systems. The absence of a reliable blast-to-crusher linkage limits the ability to anticipate primary-crusher power demand and high-load conditions. Operational responses therefore tend to be reactive.

## 3. General research question

To what extent can a hybrid model based on gradient boosting, quantile prediction, online learning, drift detection, and SHAP explanations improve the prediction of average power, peak power, and specific energy at a primary crusher?

## 4. Objectives

### General objective

Design and evaluate a predictive, interpretable, and adaptive model for primary-crusher energy demand using blast-planning and mine-to-plant data.

### Specific objectives

1. Build an integrated analytical dataset linking blast events with energy indicators.
2. Train an offline tree-based predictive model.
3. Estimate uncertainty using quantile prediction.
4. Evaluate an online-learning correction layer.
5. Detect distribution change with an adaptive-window method.
6. Explain predictions using SHAP values.

## 5. Proposed method

The study adopts Design Science Research with quantitative model evaluation. The artifact will be built iteratively and evaluated using historical operational records. Candidate tools include CatBoost, River, ADWIN, and SHAP.

## 6. Preliminary data plan

The anticipated sources are blast-design records, hole coordinates, geological and geomechanical attributes, truck-cycle records, payload, crusher destination, and plant-historian power signals. At this version, the number of blast events, time span, final linkage rate, and exact sampling semantics were not yet quantified.

## 7. Evaluation plan

The initial evaluation proposed MAE, RMSE, R², quantile loss, and explanation review. A temporal holdout and multiple baseline models were recommended but not yet fully specified.

## 8. Ethics

The study uses sensitive industrial data. The mine and source systems will be anonymized, access will be restricted, and only aggregate findings will be published. Formal authorization and the applicable UNMSM ethics pathway must be confirmed before real-data extraction.

## 9. Reproducibility

Code will be versioned in Git. Data versions, seeds, package versions, and model parameters will be recorded. DVC and MLflow are proposed for later phases.

## 10. Known weaknesses in this version

- Data inventory is not quantified.
- The research question is library-led.
- Average power, peak power, and specific energy are not clearly separated.
- Online learning is not compared against scheduled retraining.
- Acceptance thresholds are missing.
- The timeline, budget, and legal checklist are incomplete.

These weaknesses were corrected in the revised protocol.
