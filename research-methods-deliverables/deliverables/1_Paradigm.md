Luis Quispe Inquil \| Research Methods and Scientific Integrity in AI and Advanced Technologies

| **Revision focus:** Expert review of SHAP explanations is treated as an artifact-validity check, not as a separate interpretivist epistemology. Validity criteria are now expressed through a priori success thresholds. |
|----|

# 1. Research topic and context

This research addresses the difficulty of anticipating primary-crusher energy demand before blasted material enters the process. In a Peruvian open-pit copper mine, variation in blast design, geology, geomechanics, fragmentation, and feed conditions may produce power peaks, unstable loading, and increased specific energy. The study seeks to convert fragmented mine-to-plant data into a predictive artifact that is useful, auditable, and adaptable.

# 2. Preliminary research question

How can a probabilistic, adaptive, and interpretable artifact be designed and evaluated to predict average power, peak power, and specific energy from blast-planning data while quantifying uncertainty and preserving performance under operational change?

# 3. Paradigm selection and justification

The primary paradigm is Design Science Research (DSR), complemented by post-positivist quantitative evaluation. The central contribution is not merely an association or model comparison; it is the construction and evaluation of an artifact that integrates tabular prediction, quantile uncertainty, temporal adaptation, drift monitoring, and model explanation. Knowledge claims will be grounded in artifact utility, temporal predictive validity, calibration, reproducibility, and design knowledge derived from build-evaluate-refine cycles. Post-positivism supports falsifiable comparisons using historical and prospective data, error metrics, uncertainty intervals, and statistical tests. Interpretivism is not a co-equal paradigm in this study. Domain specialists will review SHAP outputs only as a structured rigor check on the artifact's technical coherence and face/content validity; their review will not be used to construct a separate account of lived meaning.

# 4. A priori validity criteria

| **Criterion** | **Provisional acceptance threshold** |
|----|----|
| Predictive validity | At least 10% lower MAE than the strongest non-hybrid baseline on a locked temporal test set; block-bootstrap 95% CI for the error difference should favor the proposed model. |
| Probabilistic validity | Q10-Q90 empirical coverage between 76% and 84%, with lower pinball loss than an empirical-quantile baseline. |
| Adaptive utility | Online residual correction is retained only if post-drift cumulative MAE is at least 5% lower than scheduled retraining, or recovery time is at least 20% shorter. |
| Explanation rigor | At least three mine-to-plant specialists review the top ten SHAP drivers; at least 80% of directionality judgments should be technically plausible, with disagreements documented. |
| Reproducibility | An independent rerun from the versioned repository reproduces headline metrics within 1% relative difference. |

# 5. Implications and open tension

The method will use DSR cycles with temporal validation, target-specific models, scheduled-retraining and online-learning comparators, prequential evaluation when data density permits, and SHAP-based artifact checks. The main open tension is whether the available data stream is sufficiently long and dense to justify online learning; a pre-specified data-readiness gate will determine whether River/ADWIN is retained or replaced by periodic batch retraining.

*Methodological basis: Hevner et al. (2004); Creswell and Creswell (2023).*
