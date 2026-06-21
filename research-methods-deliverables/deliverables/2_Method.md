**UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS**

**Faculty of Systems and Informatics Engineering - Graduate Unit\**
Doctoral Program in Deep Technologies with a Focus on Artificial Intelligence and Emerging Technologies

Research Question and Method-Fit Matrix - Revised

**Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data in a Peruvian Open-Pit Copper Mine**

| **Course** | Research Methods and Scientific Integrity in AI and Advanced Technologies |
|:---|:---|
| **Instructor** | Dr. Loveleen Gaur |
| **Student** | Luis Quispe Inquil |
| **Deliverable** | Session 2 revised deliverable - verified data update |
| **Revision date** | 17 June 2026 |

# 1. Refined research question

How can a probabilistic, adaptive, and interpretable artifact be designed and evaluated to predict primary-crusher energy demand from blast-planning data in a Peruvian open-pit copper mine?

The question foregrounds the contribution rather than software libraries. CatBoost, River, ADWIN, and SHAP remain implementation candidates described in the protocol and may be replaced if evaluation shows a better technical choice.

# 2. Status and definition of the E.D.F.C.V. framework

| **Framework attribution:** E.D.F.C.V. is a course-specific analytical decision aid, not a published or validated psychometric scale. It operationalizes five method-selection dimensions discussed in the course: Epistemological fit, Data availability, Feasibility, Contribution type, and Venue fit. The acronym is used for transparent comparison, not as an external standard. |
|----|

| **Criterion** | **Operational definition** |
|:---|:---|
| E - Epistemological fit | Consistency between the research question, paradigm, evidence, and knowledge claim. |
| D - Data availability | Access, volume, temporal coverage, granularity, linkage quality, and permissions. |
| F - Feasibility | Time, compute, cost, skills, operational access, and implementation complexity. |
| C - Contribution type | Capacity to produce the intended artifact and transferable design knowledge. |
| V - Venue fit | Alignment with the standards of mining, mineral processing, energy, and applied-AI venues. |

# 3. Weighting rule

All five criteria are equally weighted at the proposal stage because no single dimension should compensate for a fatal weakness in another. Equal weighting also prevents the matrix from being tuned after the preferred method is known. A one-at-a-time sensitivity check was conducted: even if any single criterion is given double weight, Design Science Research remains the highest-ranked method. The choice is therefore not an artifact of the default weights.

# 4. Candidate methods

- Design Science Research (DSR): build, evaluate, refine, and communicate an artifact and transferable design principles.

- Retrospective longitudinal quasi-experimental evaluation: compare models on non-randomized historical data using temporal splits, baselines, and paired statistical analysis.

- Scenario-based simulation: represent fragmentation and operational conditions to study counterfactual energy-demand scenarios that are rare or unsafe to test operationally.

# 5. Method-fit matrix

| **Criterion** | **DSR** | **Longitudinal quasi-experimental** | **Simulation** |
|:---|:---|:---|:---|
| E | 5/5 - Direct fit with knowledge through building and evaluating the artifact. | 4/5 - Strong for performance evidence, but incomplete for design knowledge. | 3/5 - Useful for counterfactuals, secondary to the build objective. |
| D | 4/5 - Verified event volume, time span, truck-cycle traceability, and crusher signals are available; the final high-confidence linkage rate remains to be measured. | 5/5 - Directly exploits the verified historical blast, haulage, payload, and crusher records. | 4/5 - Can use verified data plus assumptions, but still requires operational calibration. |
| F | 4/5 - Complex but manageable through staged prototypes and fallback tiers. | 4/5 - Feasible, but limited to observational evidence. | 3/5 - Requires mechanistic assumptions and additional validation. |
| C | 5/5 - Produces artifact, design principles, and utility evidence. | 3/5 - Produces empirical comparison with less architectural novelty. | 4/5 - Produces counterfactual insight, not necessarily a deployable system. |
| V | 5/5 - Strong fit with engineering and intelligent-systems journals. | 4/5 - Acceptable if causal limits and rigor are explicit. | 3/5 - Better fit for simulation venues than for the proposed contribution. |
| Total | 23/25 | 20/25 | 17/25 |

# 6. Selected method and explicit rejection of alternatives

DSR is selected because the doctoral objective is to create and evaluate a technological artifact whose contribution cannot be established by correlation or algorithm comparison alone. The quasi-experimental component is embedded within DSR as the principal evaluation strategy. Simulation is retained only for sensitivity analysis and low-frequency high-risk scenarios. A pure quasi-experiment is rejected as the governing method because it does not structure artifact construction and refinement; pure simulation is rejected because the main claim concerns performance on operationally traced mine-to-plant data.

# 7. Verified data foundation and conditional adaptation policy

The raw operational inventory is now verified for 1 January 2024 to 17 June 2026: 2,625 fired blasts, 412,543 hole-level records, an intermediate truck-cycle table with origin, payload, timestamps, and crusher destination, and high-frequency power signals for two confirmed primary crushers. The raw volume and time span support a formal streaming evaluation. However, the final decision to retain online learning remains conditional on the number and quality of high-confidence direct-feed processing windows linked to one selected crusher. Scheduled batch retraining remains the primary industrial comparator.

# 8. Remaining methodological tension

The traceability architecture is now defined as blast or source polygon -\> loading equipment -\> truck and LOADID -\> measured payload -\> dumping timestamp -\> selected primary crusher -\> crusher-power window. The remaining methodological tension is the operational definition of the processing window and the treatment of overlapping truck arrivals or mixed material. The confirmatory cohort will therefore use direct polygon-to-crusher feeds at high linkage confidence; stock-origin or ambiguous mixtures will be excluded from the primary analysis.

# 9. Methodological references

Creswell, J. W., & Creswell, J. D. (2023). Research design: Qualitative, quantitative, and mixed methods approaches (6th ed.). SAGE.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Yin, R. K. (2018). Case study research and applications: Design and methods (6th ed.). SAGE.
