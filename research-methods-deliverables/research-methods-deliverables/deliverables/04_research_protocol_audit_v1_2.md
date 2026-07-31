**UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS**

**Faculty of Systems and Informatics Engineering - Graduate Unit\**
Doctoral Program in Deep Technologies with a Focus on Artificial Intelligence and Emerging Technologies

Research Protocol Mini-Audit v1.2

**Audit of Proposal v0.0 and documented transition to Protocol v0.3**

| **Course** | Research Methods and Scientific Integrity in AI and Advanced Technologies |
|:---|:---|
| **Instructor** | Dr. Loveleen Gaur |
| **Student** | Luis Quispe Inquil |
| **Deliverable** | Session 3 protocol-audit laboratory - verified data update |
| **Revision date** | 17 June 2026 |

| Provenance note: This audit evaluates the initial six-page project proposal, retrospectively labeled Proposal v0.0. It does not evaluate Protocol v0.3 as though the later sections were absent. Protocol v0.3 is the current revised protocol and includes a verified operational data inventory, traceability architecture, anonymous-use authorization, and a one-crusher direct-feed design. The response map documents the transition. |
|----|

# 1. Version register

| **Version** | **Document** | **Role** | **Date/status** |
|:---|:---|:---|:---|
| Proposal v0.0 | Initial six-page project proposal | Source audited in this document | Archived 13 June 2026 |
| Audit v1.0 | Original mini-audit | Identified red/amber findings in v0.0 | 13 June 2026 |
| Protocol v0.1 | First structured revision | Added protocol sections and addressed most findings | 13 June 2026 |
| Protocol v0.2 | Instructor-feedback revision | Added provenance, thresholds, target-specific models, and policy comparison | 17 June 2026 |
| Protocol v0.3 | Verified-data revision | Adds 2,625 blasts, 412,543 holes, truck-cycle linkage, primary-crusher signals, one-crusher cohort, and anonymous-use authorization | 17 June 2026 |
| Audit v1.2 | This document | Updates response mapping and remaining risks using verified data | 17 June 2026 |

# 2. Audit object and global verdict

Audited document: Proposal v0.0, six pages. General criterion: alignment among problem, question, method, data, feasibility, ethics, and reproducibility.

| Global verdict on Proposal v0.0: AMBER - Scientifically relevant and technically promising, but incomplete as an auditable research protocol. This verdict is historical: Protocol v0.3 now contains the sections that were absent from v0.0. |
|----|

# 3. Evidence-based audit of Proposal v0.0

| **Criterion** | **Label** | **Traceable evidence** | **Interpretation** | **Actionable revision** |
|:---|:---|:---|:---|:---|
| Problem and relevance | GREEN | “This gap limits proactive decision-making at the mine-plant interface and maintains a predominantly reactive logic.” (Proposal v0.0, p. 1) | States an operational consequence and passes the “so what?” test. | Add an empirical baseline for power variability, specific energy, or high-load events when data are received. |
| General question | AMBER | “To what extent does a hybrid model based on CatBoost, online learning with River, SHAP explainability, and quantile prediction allow...” (Proposal v0.0, p. 2) | Combines architecture, precision, interpretation, and adaptation in one library-led question. | Shorten the question and move implementation tools to the abstract/method. |
| Method-contribution alignment | GREEN | “The proposal incorporates... CatBoost... quantiles... River... and SHAP.” (Proposal v0.0, p. 2) | The architecture is consistent with an artifact-building contribution. | Explicitly declare DSR and build-evaluate-refine cycles. |
| SMART objectives | AMBER | “Design and train... Implement... Incorporate... Apply SHAP... Evaluate...” (Proposal v0.0, p. 3) | Specific and relevant, but no deadlines or acceptance thresholds. | Assign months, metrics, and success criteria. |
| Data availability and traceability | AMBER | “Build an integrated database linking blast events with energy and operational indicators...” (Proposal v0.0, p. 3) | Recognizes linkage, but does not quantify volume, span, frequency, identifiers, or permissions. | Add actual verified inventory, requested fields, decision gates, and fallback tiers. |
| Statistical evaluation | RED | No temporal split, baselines, seeds, intervals, tail metrics, or paired comparisons are specified in Proposal v0.0, pp. 1-6. | Performance is not auditable and temporal/group leakage is possible. | Define locked temporal testing, baselines, uncertainty, paired tests, and target-specific evaluation. |
| Timeline and budget | RED | No timeline or budget section appears in Proposal v0.0, pp. 1-6. | Doctoral feasibility cannot be assessed. | Add phases, milestones, 25%-30% contingency, and an indicative budget. |
| Ethics and integrity | RED | No ethics or data-governance section appears in Proposal v0.0, pp. 1-6. | Industrial data may be confidential and operationally sensitive. | Add permissions, minimization, access, retention, publication, and CONCYTEC alignment. |
| Reproducibility | RED | No Git, DVC, MLflow, pinned environment, seeds, or stranger-test documentation appears in Proposal v0.0, pp. 1-6. | A third party could not reconstruct the result. | Add a complete reproducibility plan. |
| Doctoral contribution | GREEN | “Predictive, interpretable and adaptive... quantify uncertainty and adjust to operational changes.” (Proposal v0.0, p. 2) | The combination has applied novelty potential. | State transferable design principles and conditional limits beyond one mine. |

# 4. Critical-sentence revision

Original (Proposal v0.0, p. 2): “In this context, the research problem focuses on the need to build a predictive, interpretable, and adaptive model...”

Revised: “Weak mine-to-plant traceability and the absence of a probabilistic adaptation policy prevent timely prediction of primary-crusher energy demand and management of high-load scenarios.”

Rationale: The revision identifies the observable deficiency, the operational consequence, and the affected unit. It therefore guides the variables, data inventory, and evaluation design more directly.

# 5. Response-to-audit map

| **Original finding** | **Revision** | **Location** | **Status** |
|:---|:---|:---|:---|
| General question - AMBER | Shortened contribution-led question; tools moved to the abstract and architecture. | Protocol v0.3 Sections 1, 2, and 5.1 | RESOLVED |
| SMART objectives - AMBER | Added time-bound acceptance thresholds. | Protocol v0.3 Section 5.5 | RESOLVED |
| Data and traceability - AMBER | Added verified 2024-17 June 2026 inventory (2,625 blasts; 412,543 holes), truck-cycle source/payload/dump/crusher linkage, one-second display-resolution power signals for two primary crushers, one-crusher direct-feed cohort, and anonymous-use authorization. | Protocol v0.3 Sections 6.2-6.5 and 7 | RESOLVED AT SOURCE-INVENTORY LEVEL; FINAL LINKAGE RATE PENDING PROFILING |
| Statistical evaluation - RED | Added locked temporal testing, target-specific metrics, block bootstrap, policy comparison, and ablations. | Protocol v0.3 Sections 6.6-6.10 | RESOLVED IN DESIGN |
| Timeline and budget - RED | Added 36-month schedule, products, contingency, and indicative budget. | Protocol v0.3 Section 9 | RESOLVED |
| Ethics and integrity - RED | Added industrial-data governance, confidentiality, specialist-review safeguards, and CONCYTEC alignment. | Protocol v0.3 Section 7 | RESOLVED IN PROTOCOL |
| Reproducibility - RED | Added Git/DVC/MLflow/Docker, seeds, hardware logging, run binding, and independent-rerun threshold. | Protocol v0.3 Sections 5.5 and 6.11 | RESOLVED IN PROTOCOL |

# 6. Prioritized remaining risks

1.  Select the primary crusher using completeness and continuity criteria, then quantify the high-confidence direct-feed linkage rate and final number of processing windows.

2.  Verify the historian extraction semantics (recorded, compressed, exception-based, or interpolated), timestamp continuity, signal quality, and the official measured-payload field.

3.  Pre-register the processing-window definition, overlap and lag rules, direct-feed eligibility, and the operational threshold and minimum duration for a peak-power event.

4.  Run the static-versus-scheduled-versus-online policy comparison before retaining River or ADWIN in the final artifact.

5.  Preserve search exports and screening logs for the final systematic review.

# 7. Self-assessment against the laboratory rubric

| **Rubric element**                        | **Score** |
|:------------------------------------------|:----------|
| Document and criterion are clear          | 2/2       |
| Verdict is plausible and version-specific | 2/2       |
| Evidence is exact and page-traceable      | 3/3       |
| Explanation connects evidence and verdict | 2/2       |
| Improvement is actionable                 | 1/1       |
| TOTAL                                     | 10/10     |
