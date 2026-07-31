**UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS**

**Faculty of Systems and Informatics Engineering - Graduate Unit\**
Doctoral Program in Deep Technologies with a Focus on Artificial Intelligence and Emerging Technologies

Research Protocol v0.3

**Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data in a Peruvian Open-Pit Copper Mine**

| **Course** | Research Methods and Scientific Integrity in AI and Advanced Technologies |
|:---|:---|
| **Instructor** | Dr. Loveleen Gaur |
| **Student** | Luis Quispe Inquil |
| **Deliverable** | Session 3 revised deliverable - verified data update |
| **Revision date** | 17 June 2026 |

| Provenance and version control: The six-page initial proposal is retrospectively labeled Proposal v0.0. The protocol audit evaluated v0.0. Protocol v0.1 was the first structured revision; Protocol v0.2 incorporated the instructor feedback of 14 June 2026. This document is Protocol v0.3 and replaces the provisional zero-state inventory with verified blast, haulage, payload, authorization, and primary-crusher information. Audit findings refer to Proposal v0.0, not to this version. |
|----|

# Response to audit and instructor feedback

| **Finding** | **Revision made** | **Location** |
|:---|:---|:---|
| Version inconsistency | Added provenance notes to Protocol v0.3 and Audit v1.2; all audit evidence now cites Proposal v0.0 page numbers. | This note; Audit v1.2 Sections 1-2 |
| Data foundation not quantified | Added a verified inventory of 2,625 fired blasts and 412,543 holes for 2024-17 June 2026; confirmed truck-cycle origin, payload, timestamps, crusher destination, one-second display resolution for two primary-crusher power tags, anonymous academic-use authorization, and a one-crusher direct-feed cohort. | Sections 6.2-6.5 and 7 |
| Interpretivist tension | Expert SHAP review reframed as an artifact-validity and rigor check. | Sections 6.10 and 7 |
| E.D.F.C.V. status and weights | Clarified in the separate Method-Fit Matrix. | Method-Fit Matrix Sections 2-3 |
| Multiple outcomes unclear | Defined three target-specific models sharing one feature pipeline; peak power receives tail-specific treatment. | Sections 5 and 6.7 |
| Online learning not defended | Added a direct comparison against static and scheduled batch-retraining policies and a data-readiness gate. | Sections 6.5 and 6.9 |
| SMART objectives lacked acceptance thresholds | Added a priori success criteria for linkage, prediction, calibration, adaptation, explanation, and reproducibility. | Section 5.5 |
| Title too long/library-led | Shortened title; libraries moved to abstract and architecture. | Title and Sections 2, 6.7 |
| PRISMA reconciliation | Revised mini-review separates six domain studies from four a priori methodological foundations. | Separate Mini-SLR v1.1 |

# Executive summary

This study will design and evaluate a probabilistic, adaptive, and interpretable artifact for anticipating primary-crusher energy demand from blast-planning and mine-to-plant data. The verified source inventory covers 2,625 fired blasts and 412,543 hole-level records from 1 January 2024 to 17 June 2026, together with a haulage table that records source location, truck cycle, measured payload, dumping time, and crusher destination. Two primary-crusher power signals are available at second-level display resolution. To reduce material-mixing and equipment heterogeneity, the confirmatory cohort will focus on direct polygon-to-crusher feeds for one selected crusher. Candidate components are CatBoost, quantile losses, River residual correction, ADWIN, and SHAP. Three target-specific models will address average power, specific energy, and peak power. Online adaptation will be retained only if the linked cohort satisfies the readiness gate and outperforms scheduled batch retraining.

# Problem in one sentence (maximum 25 words)

Weak blast-to-crusher traceability prevents timely prediction of energy demand and reliable management of high-load operating conditions.

# 1. Title

Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data in a Peruvian Open-Pit Copper Mine.

# 2. Abstract

Blasting initiates rock fragmentation and influences the load imposed on downstream crushing. This research will integrate blast-design, geological, geomechanical, truck-haulage, payload, and crusher-historian records to predict average power, specific energy, and peak-power risk. The verified operational inventory comprises 2,625 fired blasts and 412,543 associated holes between 1 January 2024 and 17 June 2026. Truck-cycle records provide source coordinates or polygon, loading equipment, truck and LOADID, measured payload, dumping timestamp, and crusher destination; two confirmed primary-crusher power tags are visualized at one-second resolution. The primary cohort will use direct feeds to one selected crusher, excluding stock-origin and ambiguous mixtures. CatBoost, River, ADWIN, and SHAP remain candidate implementation tools. Evaluation will use locked temporal testing, leakage controls, strong baselines, block-bootstrap intervals, and comparison of static, scheduled-retraining, and online policies.

# 3. Introduction and problem statement

In open-pit mining, blasting is the first stage of rock fragmentation and affects loading, hauling, crushing, and grinding. At the primary crusher, variation in particle size, ore competence, lithology, moisture, feed rate, and blending may appear as changes in power, specific energy, stability, and overload risk. Although the operation produces blast-design and plant-historian data, the absence of reliable traceability between the two domains often forces a reactive response.

The scientific gap is not the absence of predictive algorithms in general. It is the limited evidence on an integrated artifact that combines target-specific tabular prediction, calibrated uncertainty, a defensible adaptation policy, and explanations that can be reviewed by mine-to-plant specialists. The project is relevant to energy efficiency, operational stability, and digital integration in Peruvian copper mining. Access and anonymous academic use are confirmed; the remaining feasibility question is the final percentage of high-confidence direct-feed truck cycles that can be aligned with valid crusher-processing windows.

# 4. Preliminary literature review

Mine-to-Mill and Mine-to-Crusher studies indicate that blast design, fragmentation, and ore properties influence downstream throughput, specific energy, and cost. Crusher-modeling reviews describe a transition toward empirical, mechanistic, and data-driven approaches. Methodologically, CatBoost supports strong tabular learning with categorical variables; SHAP provides additive feature attributions; River supports continual learning on dynamic streams; and ADWIN provides adaptive-window drift detection. The revised mini-systematic review distinguishes six search-retrieved domain studies from four a priori methodological foundations and documents the PRISMA flow separately.

# 5. Research questions, hypotheses, and objectives

## 5.1 General research question

How can a probabilistic, adaptive, and interpretable artifact be designed and evaluated to predict primary-crusher energy demand from blast-planning data?

## 5.2 Specific questions

- Which blast, geological, geomechanical, fragmentation, and operating variables explain the greatest temporal variation in crusher energy demand?

- How much do target-specific CatBoost models improve average-power and specific-energy prediction over linear, persistence, and tree-based baselines?

- How should peak power be modeled and evaluated as an upper-tail event rather than an ordinary mean outcome?

- Do Q10-Q90 predictions achieve acceptable empirical coverage and interval width?

- Under what data volume and temporal density does online residual correction outperform scheduled batch retraining?

- Are SHAP explanations stable over time and technically coherent when reviewed as an artifact-validity check?

## 5.3 Evaluation hypotheses

- H1: The best target-specific CatBoost model will reduce MAE by at least 10% relative to the strongest non-hybrid baseline on the locked temporal test set.

- H2: Q10-Q90 intervals will attain 76%-84% empirical coverage and lower pinball loss than an empirical-quantile baseline.

- H3: For peak-power events, the tail-aware model will improve Q90/Q95 pinball loss and threshold-exceedance recall over ordinary mean regression.

- H4: Online residual correction will be retained only if it reduces post-drift cumulative MAE by at least 5% versus the best scheduled-retraining policy or shortens recovery time by at least 20%.

- H5: At least 80% of the directionality judgments for the ten leading SHAP drivers will be rated technically plausible by at least three specialists, with disagreements retained as evidence.

## 5.4 General objective

To develop and evaluate a probabilistic, adaptive, interpretable, and reproducible artifact for predicting primary-crusher energy demand from blast-design and linked mine-to-plant data in a Peruvian open-pit copper mine.

## 5.5 SMART objectives and acceptance thresholds

| **Objective** | **Time-bound acceptance criterion** |
|:---|:---|
| Data linkage | By Month 6, deliver a versioned one-crusher direct-feed cohort with at least 70% high-confidence linkage among eligible truck cycles, less than 10% unexplained missingness in mandatory fields, documented payload-field selection, and an archived anonymous-use authorization record. |
| Average power and specific energy | By Month 16, compare at least three baselines and obtain at least 10% MAE improvement over the strongest baseline on the locked temporal test set. |
| Peak power | By Month 19, define a tail event and improve Q90/Q95 pinball loss plus threshold-exceedance recall over ordinary mean regression. |
| Uncertainty | By Month 21, achieve Q10-Q90 coverage between 76% and 84%, report mean interval width, and provide calibration plots by operating regime. |
| Adaptation policy | By Month 25, compare static, scheduled batch, and online residual policies; retain online learning only if H4 is met. |
| Explanation rigor | By Month 28, complete SHAP stability analysis and structured review by at least three specialists with at least 80% plausible directionality judgments. |
| Reproducibility | By Month 32, enable an independent rerun that reproduces headline metrics within 1% relative difference using versioned code, data pointers, runs, and environment. |

# 6. Methodology

## 6.1 Paradigm and governing method

The study uses Design Science Research with post-positivist quantitative evaluation. Expert review of explanations is a validation procedure for the artifact, not an independent interpretivist study.

## 6.2 Design and unit of analysis

The design is longitudinal and non-randomized, with a retrospective build phase and a prospective shadow-mode phase when operationally authorized. The primary unit of analysis is a processing window in one selected primary crusher, constructed from direct truck feeds whose source can be linked to an identified blast or blast polygon. The traceability chain is blast_name or source polygon -\> loading equipment -\> truck and LOADID -\> measured payload -\> dumping timestamp -\> selected primary crusher -\> power window. Stock-origin records and unquantified mixtures will be excluded from the confirmatory cohort and reserved for sensitivity analysis.

## 6.3 Verified data inventory and access status as of 17 June 2026

| **Year** | **Unique fired blasts** | **Hole records** | **Blast-size range** | **Mean holes/blast** | **Median holes/blast** |
|:---|:---|:---|:---|:---|:---|
| 2024 | 1,070 | 154,821 | 1-907 | 144.69 | 112 |
| 2025 | 1,039 | 180,018 | 4-1,297 | 173.26 | 140 |
| 2026 to 17 June | 516 | 77,704 | 4-779 | 150.59 | 123 |

The primary period therefore contains 2,625 unique fired blasts and 412,543 hole-level records, with a weighted mean of 157.16 holes per blast. Ninety-six partial blast records are also available for 2023 but are excluded from the primary period. Events with fewer than five recorded holes will be reviewed for operational type and completeness rather than excluded automatically. Authorization is confirmed for anonymous academic use; the mine and source systems will not be named, and only aggregated results will be published.

## 6.4 Traceability architecture and primary analytical cohort

| **Source** | **Verified available information** | **Analytical role** |
|:---|:---|:---|
| Blast database | blast_name; X, Y, Z and bench; firing date/time; design and execution variables; designed, loaded, and blasted states. | Defines blast provenance and pre-crusher predictors. |
| Truck-cycle table | Source polygon/location and loading GPS; shovel; truck/LOADID; loading and dumping timestamps; destination/primary crusher; measured and adjusted payload fields. | Links blast origin to crusher arrival and supplies tonnes by truck cycle. |
| Primary-crusher historian | Two confirmed primary-crusher kW tags, operating state, crusher settings, stock-level context, and related process variables; one-second display resolution. | Builds average-power, energy, and validated peak-power outcomes by processing window. |
| Authorization and anonymity | Academic use is authorized on an anonymous basis; the mine and source systems will not be identified. | Defines governance, publication, and anonymization constraints. |

- The primary cohort will be restricted to direct feeds from identified blast polygons to one selected primary crusher. The selected crusher will be the unit with the highest continuity and completeness across power, operating-state, truck-dumping, and payload records. This restriction reduces equipment heterogeneity and avoids unquantified stockpile blending.

- High-confidence linkage requires a valid blast or source-polygon identifier, valid load and dump timestamps, a valid crusher destination, a positive operationally plausible measured payload, and valid crusher-power coverage. Spatial containment of loading coordinates within a blast polygon may support a medium-confidence linkage when the textual identifier is incomplete. Stock-origin or ambiguous records will be excluded from the confirmatory cohort.

- The official payload field will be selected from the available measured and historically adjusted tonnage variables using operational metadata and consistency checks. Nominal truck capacity will be used only as a fallback. Specific energy will be computed as integrated crusher energy in kWh divided by the sum of valid tonnes discharged within the same processing window.

- Historian values displayed at one-second resolution will be aggregated into operational windows and will not be treated as independent observations. Profiling will document whether extracted values are recorded, compressed, exception-based, or interpolated; timestamp continuity, quality flags, missing periods, and sensor changes will also be audited. The effective sample size is the number of high-confidence processing windows, not the number of raw historian rows.

## 6.5 Data-readiness gate and fallback plan

| **Decision tier** | **Observed inventory rule** | **Permitted design** |
|:---|:---|:---|
| Tier A - streaming evaluation | At least 1,000 high-confidence direct-feed processing windows, at least 18 months, crusher signals at 1-minute frequency or finer, linkage \>=70%, and mandatory-field missingness \<=10%. | Evaluate static, scheduled retraining, River residual correction, ADWIN, and prequential performance. |
| Tier B - periodic batch | 400-999 high-confidence windows or 12-17 months, or signals available only as 5-15 minute aggregates. | Use scheduled monthly/quarterly or every-N-lot retraining; use drift indicators for monitoring, not as proof of online superiority. |
| Tier C - retrospective pilot | 150-399 high-confidence windows or 6-11 months. | Use static target-specific models, blocked temporal validation, bootstrap uncertainty, and no online-learning claim. |
| Tier D - insufficient for predictive thesis | Fewer than 150 high-confidence windows or less than 6 months of usable linked coverage. | Reframe as a data-linkage and feasibility artifact, or expand the period/site before confirmatory modeling. |

At the raw-source level, the project already meets the duration and event-volume conditions for a streaming comparison. Final Tier A classification remains conditional on the linked one-crusher cohort, particularly the number of high-confidence windows, linkage percentage, mandatory-field missingness, and historian quality.

## 6.6 Data preparation and leakage control

- Pre-register linkage identifiers, direct-feed eligibility, processing-window rules, overlap and lag rules, payload hierarchy, mixing exclusions, and feature-availability times before model fitting.

- Split data by time and, where required, by blast or material group before imputation, encoding, selection, scaling, or target-derived feature construction.

- Fit all transformations on training data only and lock a final temporal test set until model and threshold choices are complete.

- Audit duplicate, near-duplicate, future-information, group, and target leakage; preserve an exclusion log and versioned data hashes.

- Report performance by time block, lithology, operating range, and data-quality stratum.

## 6.7 Target-specific modeling strategy

The project will not use a single undifferentiated multi-output model as the default. It will use three target-specific models that share a common versioned feature pipeline:

| **Target** | **Modeling and evaluation treatment** |
|:---|:---|
| Average power | Continuous central-tendency target; compare linear/persistence/tree baselines and CatBoost using MAE, RMSE, R2, and regime-specific error. |
| Specific energy | Continuous ratio target; model only when the denominator is reliable, audit low-throughput instability, and report MAE/RMSE plus error by throughput band. |
| Peak power | Upper-tail target defined per traceable lot/window; evaluate Q90/Q95 pinball loss, exceedance recall/precision, calibration, and an extreme-value or peak-over-threshold benchmark when sample size permits. |

## 6.8 Probabilistic and explanation layers

Quantile models will estimate Q10, Q50, and Q90 for routine uncertainty and Q95 for peak-risk analysis when supported by data. SHAP will be used for global, local, temporal, and high-demand explanations. Specialist review will use a structured rating form focused on technical plausibility, sign/direction, missing confounders, and operational usefulness; the results are evidence about artifact validity, not qualitative theory building.

## 6.9 Static, scheduled-retraining, and online policies

| **Policy** | **Definition** |
|:---|:---|
| Policy S0 - static | Train once on the development period; no update during the shadow test. |
| Policy S1 - scheduled batch | Retrain every calendar month/quarter or after a pre-specified number of new traceable lots; frequency selected using the development period only. |
| Policy S2 - online residual correction | Keep the offline base model and update a River residual component sequentially; ADWIN monitors error or residual change. |
| Selection rule | Choose the simplest policy that meets accuracy, recovery, stability, compute, and governance thresholds. Online learning is not assumed to be superior. |

## 6.10 Evaluation and statistical analysis

| **Dimension** | **Indicators and tests** |
|:---|:---|
| Point prediction | MAE, RMSE, R2, regime-specific error, block-bootstrap 95% CIs, and paired error comparisons by time block. |
| Tail/peak performance | Q90/Q95 pinball loss, event recall/precision, false-alarm rate, calibration of exceedance probabilities, and stability by operating regime. |
| Uncertainty | Pinball loss, empirical coverage, mean prediction-interval width, and calibration curves. |
| Adaptation | Prequential MAE, post-change cumulative error, recovery time, update frequency, false drift alerts, compute and maintenance burden. |
| Explanation | SHAP rank stability across time, local scenario review, specialist plausibility ratings, and documented disagreements. |
| Ablation | Base predictor; + quantiles; + scheduled update; + online residual; + drift trigger; + explanation layer. |

## 6.11 Reproducibility

Code will be versioned with Git; data or data pointers with DVC; parameters, metrics, and artifacts with MLflow; and the environment with pinned requirements and Docker. Python, NumPy, and model-library seeds will be recorded, as will hardware, drivers, and nondeterministic operations. Results will be reported across multiple seeds where stochasticity exists. A stranger-test README and a reproducibility manifest will bind each reported table to a code commit, data hash, and run identifier.

# 7. Ethics, governance, and scientific integrity

- The study uses industrial process and haulage data and does not seek to identify individuals. Academic use has been authorized on an anonymous basis. The mine, source systems, personnel names, operator identifiers, credentials, and sensitive coordinates will not be disclosed; required operational identifiers will be pseudonymized.

- A documentary record of authorization, access scope, retention, encryption, publication aggregation, deletion, and intellectual-property conditions will be archived in the project governance record before confirmatory modeling and publication.

- Operationally sensitive configurations and security information will not be published.

- All transformations, exclusions, protocol deviations, negative results, and model-selection decisions will be traceable.

- Specialist SHAP review will be voluntary, minimal-risk, and used only to assess artifact coherence; if identifiable responses are collected, institutional ethics requirements will be checked before review.

- The work will align with the CONCYTEC National Code of Scientific Integrity and applicable UNMSM rules.

# 8. Expected results

- An archived anonymous-use authorization record, anonymization plan, and publication-governance pathway.

- A versioned one-crusher direct-feed dataset and linkage dictionary reporting high-, medium-, and low-confidence traceability, payload completeness, and historian coverage.

- Separate validated models for average power, specific energy, and peak power.

- Calibrated uncertainty bands and an evidence-based decision on scheduled versus online updating.

- SHAP explanations with temporal stability analysis and structured artifact-validity review.

- A reproducible repository, deployment guide, design principles, and at least one scientific manuscript.

# 9. Timeline and indicative budget

## 9.1 Thirty-six-month timeline

| **Phase** | **Months** | **Product** |
|:---|:---|:---|
| Governance, protocol, and scope freeze | 1-4 | Archived anonymous-use authorization; anonymization plan; Protocol v1.0; one-crusher cohort definition. |
| Systematic review and traceability design | 3-8 | Verified SLR; truck-cycle linkage specification; processing-window protocol. |
| Extraction, profiling, and integration | 5-12 | Linked-cohort counts; extraction-mode and quality audit; versioned dataset and dictionary. |
| Baselines and target-specific models | 11-18 | Average-power, specific-energy, and peak-power models. |
| Quantiles and calibration | 16-22 | Q10/Q50/Q90/Q95 assessment. |
| Policy comparison | 20-27 | Static vs scheduled vs online evaluation, conditional on data tier. |
| SHAP and specialist rigor check | 24-29 | Stability analysis and structured review. |
| Shadow pilot and refinement | 27-32 | Operationally monitored prototype or retrospective fallback. |
| Writing, publication, and defense | 31-36 | Thesis, article, repository, and defense. |
| Contingency | Distributed | 25%-30% embedded in access, integration, and evaluation phases. |

## 9.2 Indicative budget

| **Item** | **Estimated amount** | **Rationale** |
|:---|:---|:---|
| Storage and compute | S/ 12,000 | Experimentation, backup, reproducible runs. |
| Specialized services/connectors | S/ 5,000 | Tools or connectors unavailable institutionally. |
| Technical visits and coordination | S/ 8,000 | Requirements, data-linkage validation, transfer. |
| Minor equipment and secure backup | S/ 6,500 | Encrypted disks and contingency accessories. |
| Publication and dissemination | S/ 9,000 | Editing, conference, or APC if applicable. |
| Contingency | S/ 8,000 | Access delay, compute extension, unexpected activities. |
| TOTAL | S/ 48,500 | Subject to agreements and institutional resources. |

# 10. References

Bifet, A., & Gavaldà, R. (2007). Learning from time-changing data with adaptive windowing. In Proceedings of the 2007 SIAM International Conference on Data Mining (pp. 443-448). https://doi.org/10.1137/1.9781611972771.42

CONCYTEC. (2024). Resolución de Presidencia N.° 028-2024-CONCYTEC-P: Código Nacional de Integridad Científica.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. Patterns, 4(9), 100804. https://doi.org/10.1016/j.patter.2023.100804

Lastra, G., Jokovic, V., & Kanchibotla, S. (2021). Understanding the impact of geotechnical ore properties and blast design on comminution circuits using simulations. Minerals Engineering, 170, 107001. https://doi.org/10.1016/j.mineng.2021.107001

Losaladjome Mboyo, H., Huo, B., Mulenga, F. K., Mabe Fogang, P., & Kalenga Kaunde Kasongo, J. (2024). Assessing the impact of surface blast design parameters on the performance of a comminution circuit processing a copper-bearing ore. Minerals, 14(12), 1226. https://doi.org/10.3390/min14121226

Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems, 30.

Montiel, J., Halford, M., Mastelini, S. M., et al. (2021). River: Machine learning for streaming data in Python. Journal of Machine Learning Research, 22(110), 1-8.

Navarro Torres, V. F., Ferreira, F. V., de Carvalho, V. A., Veras, E., & Sitônio, F. F. (2024). Application of blast-pile image analysis in a Mine-to-Crusher model to minimize overall costs in a large-scale open-pit mine in Brazil. Mining, 4(4), 983-993. https://doi.org/10.3390/mining4040055

Nikkhah, A., Vakylabad, A. B., Hassanzadeh, A., Niedoba, T., & Surowiak, A. (2022). An evaluation on the impact of ore fragmented by blasting on mining performance. Minerals, 12(2), 258. https://doi.org/10.3390/min12020258

Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372, n71. https://doi.org/10.1136/bmj.n71

Pineau, J., et al. (2021). Improving reproducibility in machine learning research: A report from the NeurIPS 2019 Reproducibility Program. Journal of Machine Learning Research, 22(164), 1-20.

Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: Unbiased boosting with categorical features. Advances in Neural Information Processing Systems, 31.

Saldana, M., et al. (2024). Applications of Kuz-Ram models in Mine-to-Mill integration and optimization-A review. Minerals, 14(11), 1162. https://doi.org/10.3390/min14111162

Yamashita, A. S., Thivierge, A., & Euzébio, T. A. M. (2021). A review of modeling and control strategies for cone crushers in the mineral processing and quarrying industries. Minerals Engineering, 170, 107036. https://doi.org/10.1016/j.mineng.2021.107036
