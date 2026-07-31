# Model Card — Proposed Predictive Artifact

**Project:** Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data  
**Student:** Luis Quispe Inquil  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies  
**Status:** Design-stage Model Card. No real operational model is trained in this repository.

## 1. Model details

The proposed artifact will be a target-specific predictive system for primary-crusher energy demand. Candidate methods include tree-based tabular models, probabilistic/quantile prediction, scheduled retraining, online residual correction, drift monitoring, and SHAP-based explanation.

The protocol treats CatBoost, River, ADWIN, and SHAP as candidate implementation tools, not as guaranteed final choices.

## 2. Intended use

The model is intended to support research on whether blast-design and traceable mine-to-plant data can predict:

1. average crusher power;
2. specific energy in kWh/t;
3. peak-power or high-load risk.

The model is not intended for autonomous operational control.

## 3. Factors and inputs

Candidate predictors include:

- blast design variables;
- hole-count and blast-size features;
- bench and anonymized spatial features;
- geological and geomechanical indicators;
- material category;
- truck-cycle payload;
- dump timestamp and processing-window features;
- selected primary crusher;
- operating-state and data-quality indicators available before or during the allowed prediction moment.

Features unavailable before the prediction moment must not be used in the initial forecasting model.

## 4. Target-specific outputs

| Target | Treatment |
|---|---|
| Average power | Central tendency regression; MAE/RMSE/R² and regime-specific error. |
| Specific energy | Ratio outcome using integrated kWh divided by valid tonnes; audit low-throughput instability. |
| Peak power | Upper-tail or threshold-exceedance problem; Q90/Q95 pinball loss, recall, precision, and false-alarm rate. |

## 5. Evaluation plan

The evaluation must use:

- locked temporal test set;
- leakage controls;
- strong baselines;
- block-bootstrap confidence intervals;
- comparison against scheduled retraining;
- prequential evaluation only if data-readiness gates are met;
- ablation studies for each architectural layer.

## 6. Baselines

Minimum required baselines:

1. persistence or historical median baseline;
2. linear model baseline;
3. tuned tree-based baseline;
4. scheduled batch retraining baseline.

Online learning must not be retained unless it beats scheduled retraining on pre-specified criteria.

## 7. Metrics

| Evaluation dimension | Planned metrics |
|---|---|
| Point prediction | MAE, RMSE, R², block-bootstrap intervals. |
| Uncertainty | Pinball loss, empirical Q10–Q90 coverage, interval width. |
| Peak events | Q90/Q95 pinball loss, event recall, precision, false-alarm rate. |
| Adaptation | Prequential MAE, post-change cumulative error, recovery time, false drift alerts. |
| Explanation | SHAP rank stability, specialist plausibility rating, disagreement log. |
| Reproducibility | Independent rerun within 1% relative difference for headline metrics. |

## 8. Ethical and scientific-integrity considerations

The model will use industrial process data. The mine, source systems, coordinates, personnel identifiers, and equipment identifiers must remain confidential. Results must be reported only in anonymized and aggregated form.

## 9. Caveats

The current repository contains a synthetic EDA demonstration only. It does not contain a trained production model or real operational rows. Any conclusions produced from synthetic data are methodological demonstrations, not operational findings.

## 10. Model status

- Current status: proposed artifact and reproducible synthetic workflow.
- Next status: baseline model on authorized linked data or synthetic baseline for course demonstration.
- Required before final claim: real linked cohort, temporal validation, reproducibility manifest, and governance record.
