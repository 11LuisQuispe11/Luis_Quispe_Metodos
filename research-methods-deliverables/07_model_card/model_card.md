# Model Card — Design-Stage Predictive Artifact

**Model name:** Primary-Crusher Energy Demand Predictive Artifact  
**Version:** Design stage 0.3  
**Owner:** Luis Quispe Inquil  
**Status:** No final empirical model is trained in this public repository

## 1. Model details

The proposed artifact will predict primary-crusher energy demand from blast-design, geological, geomechanical, haulage, payload, and crusher-context variables. Candidate implementations include tuned tree-based models, probabilistic quantile models, scheduled batch retraining, conditional online residual correction, drift monitoring, and SHAP-based explanations.

CatBoost, River, ADWIN, and SHAP are candidate tools rather than guaranteed final components.

## 2. Intended use

The artifact is intended for doctoral research and shadow-mode decision support. It will investigate three targets:

1. average crusher power;
2. specific energy in kWh/t;
3. peak-power or high-load risk.

It is not intended for autonomous control, disciplinary evaluation of workers, safety-critical intervention without human review, or direct production deployment from the public synthetic notebook.

## 3. Factors

Performance may vary by:

- year and operating period;
- selected crusher;
- bench and mine zone;
- lithology, geomechanical regime, and material type;
- blast size and design;
- payload and throughput range;
- traceability confidence;
- sensor quality and missingness;
- distribution shift after maintenance or operational change.

No demographic protected attribute is part of the proposed industrial model. Operational robustness slices must not be mislabelled as human fairness metrics.

## 4. Metrics

| Dimension | Planned metrics |
|---|---|
| Average power | MAE, RMSE, R², block-bootstrap 95% confidence intervals |
| Specific energy | MAE, RMSE, error by throughput band |
| Peak power | Q90/Q95 pinball loss, recall, precision, false-alarm rate |
| Uncertainty | Q10–Q90 empirical coverage, interval width, calibration curves |
| Adaptation | Prequential MAE, post-drift error, recovery time, false drift alarms |
| Explanation | SHAP rank stability, specialist plausibility ratings |
| Reproducibility | Independent rerun within 1% relative difference for headline metrics |

Current quantitative results: **UNKNOWN — no authorized final model has been evaluated.**

## 5. Evaluation data

The intended empirical evaluation will use a chronological split and a locked final period. The unit of analysis will be a high-confidence processing window linked from blast or polygon to truck discharge and crusher power.

The public repository uses synthetic demonstration data only. Synthetic results are not valid evidence of mine performance.

## 6. Training data

The planned restricted dataset includes blast, hole, truck-cycle, payload, and crusher-historian information. Verified aggregate evidence covers 2,625 unique fired blasts and 412,543 hole records from 1 January 2024 to 17 June 2026.

Final linked-cohort size, missingness, window count, and historian extraction semantics remain **UNKNOWN — to investigate when authorized data access is available**.

## 7. Quantitative analyses

Required comparisons:

- persistence or historical-median baseline;
- linear baseline;
- tuned tree-based baseline;
- static model;
- scheduled monthly, quarterly, or every-N-lot retraining;
- online residual correction only if the data-readiness gate is met.

All models must receive comparable tuning effort, data access, compute budget, and evaluation protocol. Ablations must isolate the contribution of quantiles, scheduled updates, online correction, drift monitoring, and explanation layers.

## 8. Ethical considerations

The mine, source systems, coordinates, equipment identifiers, operator identifiers, and raw operational records must remain confidential. Predictions must not be used to assign blame to personnel or automate safety-critical control without separate validation and governance.

Dual-use risk includes using the model to pressure throughput beyond safe operating limits or treating explanations as causal proof.

## 9. Caveats and recommendations

- No final model has been trained in this public repository.
- The synthetic notebook demonstrates workflow structure, not operational validity.
- Online learning is conditional and must beat scheduled retraining.
- Peak power requires tail-specific evaluation.
- Explanations are not causal evidence.
- Deployment requires human oversight, monitoring, rollback, and documented authorization.


## Public synthetic demonstration result

The reproducibility pipeline produced the following temporal-holdout result on synthetic data:

- MAE: 121.37 kW
- RMSE: 154.23 kW
- R²: 0.816

These values demonstrate pipeline operation only and are not operational-performance claims.
