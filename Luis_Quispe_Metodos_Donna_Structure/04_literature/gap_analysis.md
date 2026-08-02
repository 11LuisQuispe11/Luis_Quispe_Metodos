# Gap Analysis

**Review scope:** Blast design, fragmentation, primary crushing, comminution energy, probabilistic prediction, temporal adaptation, drift detection, and explainability.

## 1. Knowledge gap

Existing mine-to-mill and mine-to-crusher studies support the relationship between blast design, fragmentation, throughput, and comminution performance. However, the literature does not provide a sufficiently validated end-to-end artifact that predicts three distinct primary-crusher outcomes from traceable blast-to-crusher records: average power, specific energy, and peak-power risk.

## 2. Methodological gap

Four weaknesses recur:

- deterministic point prediction without calibrated uncertainty;
- random train/test partitioning despite temporal dependence;
- limited comparison between static, periodically retrained, and online-adaptive policies;
- explanations reported without temporal-stability or specialist-validity checks.

The proposed study addresses these weaknesses with locked temporal evaluation, target-specific models, quantile prediction, block-bootstrap uncertainty, and a pre-specified policy comparison.

## 3. Contextual gap

The identified studies are concentrated in non-Peruvian contexts or use simulation, review, and cost-optimization designs. There is limited published evidence from an anonymous large-scale Peruvian open-pit copper operation with verified blast inventory, truck-cycle traceability, measured payload, dump timestamps, one selected primary crusher, and high-frequency power signals.

## 4. Theoretical gap

The literature contains technical components - gradient boosting, quantile regression, stream learning, drift detection, and feature attribution - but offers limited design knowledge about when they should be combined and when adaptation should be rejected.

The Design Science contribution is therefore not the simple combination of libraries. It is a governed architecture with rules for data readiness, model updating, tail-risk evaluation, reproducibility, and explanation validation.

## 5. Gap-to-design mapping

| Gap | Design response | Evidence required |
|---|---|---|
| No target-specific end-to-end energy artifact | Separate models for average power, specific energy, and peak risk | Temporal holdout results |
| Limited uncertainty calibration | Quantile models and coverage testing | Pinball loss and empirical coverage |
| Weak temporal rigor | Chronological split and locked final period | Leakage audit and preregistration |
| Unproven online-learning advantage | Compare static, scheduled, and online policies | Prequential error and recovery time |
| Site-specific evidence missing | Anonymous Peruvian mine case | Linked-cohort quality report |
| Explanations treated as self-validating | SHAP stability and specialist rigor check | Review protocol and disagreement log |
| Reproducibility underreported | Git, DVC, Docker, artifacts, hashes, and trace report | Independent stranger test |

## 6. Final gap statement

The unresolved research problem is the absence of a reproducible and governed mine-to-plant artifact that uses traceable blast and haulage information to produce calibrated, temporally valid, and interpretable predictions of primary-crusher energy demand under operational change.
