# Bias Audit Report — COMPAS Recidivism Course Exercise

**Dataset:** ProPublica COMPAS two-year recidivism  
**Protected attribute:** Race  
**Privileged group:** Caucasian  
**Unprivileged group:** African-American  
**Favorable outcome:** Predicted not to reoffend within two years  
**Baseline model:** Logistic regression  
**Mitigation:** AIF360 Reweighing  
**Status:** Draft based on the instructor calibration example; rerun the workshop notebook before claiming independent execution

## 1. Setup and direction of the favorable outcome

The favorable outcome is the prediction that a defendant will not reoffend because it corresponds to the less harmful downstream consequence for the individual. Direction must be stated before calculating fairness metrics; reversing it reverses the interpretation of every gap.

The course calibration used 6,167 rows after missing-data handling, with 4,316 training rows and 1,851 test rows under a 70/30 split and seed 42.

## 2. Bias present in the recorded labels

Before fitting a classifier, the training labels showed:

| Metric | Value | Interpretation |
|---|---:|---|
| Disparate impact | 0.850 | Favorable labels occurred less often for the unprivileged group |
| Statistical parity difference | -0.090 | Nine-percentage-point label gap |

This means the historical dataset already contains group disparity. A model trained to minimize aggregate error may inherit or amplify that pattern.

## 3. Baseline metrics

| Metric | Before | Target | Reading |
|---|---:|---:|---|
| Accuracy | 0.664 | Context | Approximately two thirds correct |
| Disparate impact | 0.773 | At least 0.80 | FAIL under the four-fifths screening rule |
| Statistical parity difference | -0.165 | 0 | 16.5 pp fewer favorable predictions |
| Equal opportunity difference | -0.095 | 0 | Favorable-class TPR is lower |
| Average odds difference | -0.139 | 0 | Error rates differ across groups |

The model amplifies the selection-rate gap: the data-level disparate impact was 0.850, while the fitted baseline fell to 0.773.

## 4. Mitigation choice

**Method:** Reweighing, a pre-processing approach.

Reweighing changes the importance assigned to training instances so that group and label become less dependent. It does not alter the feature values or labels and allows the final classifier to remain an ordinary logistic regression.

**Fairness objective:** statistical parity and disparate impact.

**Normative trade-off:** optimizing selection-rate parity does not guarantee calibration or equal error rates. Because base rates differ, no single metric can satisfy every fairness concept simultaneously. The metric choice must therefore be justified by the harm being prioritized.

## 5. After metrics and quantified trade-off

| Metric | Before | After | Change |
|---|---:|---:|---:|
| Accuracy | 0.664 | 0.653 | -0.011 |
| Disparate impact | 0.773 | 0.975 | +0.202 |
| Statistical parity difference | -0.165 | -0.016 | +0.149 toward zero |
| Equal opportunity difference | -0.095 | +0.031 | +0.126; slight sign reversal |
| Average odds difference | -0.139 | +0.015 | +0.154 toward zero |

The four-fifths flag moves from FAIL to PASS. The apparent single-split accuracy cost is 1.1 percentage points. Equal opportunity slightly crosses zero, indicating a possible overcorrection rather than a perfectly neutral improvement.

## 6. Uncertainty across splits

The instructor calibration repeated the pipeline across ten splits:

| Metric | Before mean ± sd | After mean ± sd |
|---|---:|---:|
| Accuracy | 0.671 ± 0.013 | 0.665 ± 0.012 |
| Disparate impact | 0.775 ± 0.032 | 1.000 ± 0.063 |
| Statistical parity difference | -0.161 ± 0.027 | -0.001 ± 0.039 |
| Equal opportunity difference | -0.091 ± 0.029 | +0.053 ± 0.030 |
| Average odds difference | -0.140 ± 0.024 | +0.021 ± 0.036 |

The fairness gain is robust across splits. The accuracy difference is smaller than run-to-run variation and should not be presented as a certain cost. The positive equal-opportunity shift appears more persistent and must be disclosed.

## 7. Recommendation

Do not deploy either model for decisions affecting liberty. Accuracy near two thirds is too weak for a high-stakes criminal-justice decision even if group disparities are reduced.

A review board should require group-specific fairness metrics, within-group calibration, external validation in the deployment jurisdiction, uncertainty intervals, and recurring audits. Intersectional analyses by race and sex or age should be completed before any pilot.

## 8. Honest limitations

This audit evaluates one protected attribute, one dataset, one baseline family, and one mitigation. It does not establish individual fairness, causal fairness, intersectional fairness, or validity in another jurisdiction.

## 9. Transfer to the mining thesis

The mining project currently has no intended demographic protected attribute and should not manufacture one. The appropriate transfer is to disaggregate predictive performance by operational conditions: time period, lithology, bench, material type, crusher, throughput band, traceability confidence, and signal quality.

These robustness slices are scientifically necessary, but they must not be described as demographic fairness. A human fairness audit becomes necessary if the system later affects personnel evaluation, work allocation, or safety decisions.

## AI-use disclosure

AI assistance was used to organize and draft this report from the course template and calibration values. The student must run the provided workshop notebook and replace this disclosure if presenting the report as independently executed.
