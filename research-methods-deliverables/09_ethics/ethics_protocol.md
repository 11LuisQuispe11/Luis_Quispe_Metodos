# Research Ethics Protocol v0.1

**Project:** Primary-Crusher Energy Demand Prediction from Blast and Traceability Data  
**Researcher:** Luis Quispe Inquil  
**Institution:** Universidad Nacional Mayor de San Marcos  
**Risk classification proposed:** Minimal risk / secondary industrial-data research, subject to institutional confirmation

## 1. Purpose and participants

The study will design and evaluate a predictive artifact for average primary-crusher power, specific energy, and peak-power risk. It does not intentionally recruit patients, community members, employees, or other human participants.

Specialists may later review SHAP explanations. If identifiable specialist responses are recorded, they will be treated as voluntary research participation and submitted to the applicable UNMSM ethics pathway before collection.

## 2. Data collection and provenance

The planned sources are blast-design and execution records, hole coordinates, truck-cycle records, measured payload, dumping timestamps, crusher destination, and high-frequency crusher-historian signals. Academic use has been authorized on an anonymous basis, but the final scope, retention period, and publication restrictions must be documented privately before confirmatory modelling.

No scraped social-media data, biometric data, health data, or Indigenous-community data are planned.

## 3. Consent strategy and lawful authorization

Individual informed consent is not applicable to machine and process measurements that contain no personal data. Organizational authorization from the data owner is required and will be archived.

If operator names, employee identifiers, or free-text fields containing personal data are encountered, they will be removed before analysis. Their use will require a separate legal and ethical assessment rather than being silently incorporated.

For specialist explanation review, participation will be voluntary, information will be provided in plain language, and withdrawal will be permitted until responses are anonymized and aggregated.

## 4. Risk and harm map

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| Disclosure of confidential operational information | Medium | High | No mine or system name; no raw coordinates; restricted storage; aggregate publication |
| Reidentification through timestamps, locations, or equipment combinations | Medium | High | Generalization, pseudonymization, temporal aggregation, cell suppression |
| Model used to assign blame to personnel | Low–Medium | High | Exclude operator identity; state prohibited use; human governance |
| Model used to push equipment beyond safe limits | Low–Medium | High | Shadow mode only; operating limits remain authoritative; no autonomous control |
| Incorrect predictions affecting operational decisions | Medium | Medium–High | Temporal validation, uncertainty, monitoring, rollback, human review |
| Explanations interpreted as causal proof | Medium | Medium | Explicitly label SHAP as associational explanation |
| Conflict between adaptation speed and governance | Medium | Medium | Online learning retained only after controlled comparison and approval |
| Specialist-review power asymmetry | Low | Medium | Voluntary participation, no employment consequence, aggregated reporting |

## 5. Benefits

Potential benefits include improved understanding of the blast-to-crusher relationship, more transparent prediction of energy demand, better uncertainty reporting, and design principles for responsible mine-to-plant analytics.

No direct benefit to an individual participant is promised. Operational benefits remain hypothetical until validated with authorized real data.

## 6. Confidentiality and anonymization

The public repository will not contain:

- mine name;
- source-system names;
- real coordinates;
- real truck, shovel, crusher, operator, or employee identifiers;
- credentials or infrastructure details;
- raw process rows.

Identifiers will be pseudonymized, coordinates translated or generalized, timestamps aggregated where necessary, and rare public summary cells suppressed. Synthetic data will be labelled prominently.

## 7. Data storage, access, retention, and breach response

Real restricted data, if re-obtained, will be stored in encrypted institutional or explicitly approved storage with role-based access. Public GitHub will contain only code, documentation, synthetic data, and approved aggregates.

A 3-2-1 backup approach will be used for authorized research artifacts. Retention will be five years after thesis completion unless the data-use agreement requires a shorter period. Secure deletion will use approved cryptographic or storage-provider deletion procedures.

Any suspected breach will be reported through the institutional process and handled according to the applicable data-owner and legal requirements.

## 8. Conflicts of interest, dual roles, and intellectual property

The researcher may have professional familiarity with the operational domain. This creates a duty to separate academic analysis from employer decision-making, avoid unauthorized extraction, and disclose any relevant employment or funding relationship.

Ownership of operational data remains with the data owner. The thesis will publish only authorized aggregate findings, general methods, and non-confidential design principles.

## 9. AI-specific ethics additions

### Training-data provenance

Every dataset version must have a documented source, extraction date, authorization scope, and transformation history.

### Deployment harms

The research artifact will not be used for autonomous plant control or personnel evaluation. A later deployment would require independent validation, monitoring, incident response, and operational approval.

### Dual-use

The same predictions that could reduce energy variability could also be used to increase throughput unsafely or to attribute responsibility unfairly. These uses are explicitly prohibited.

### Bias and distribution shift

Because the model is industrial rather than person-facing, demographic fairness metrics are not the primary audit. The study will instead test error stability across time, lithology, bench, material type, crusher, throughput, and data-quality strata. This robustness analysis does not replace a human-rights assessment if the system later affects employment decisions.

### Explainability

SHAP outputs will be treated as model explanations, not causal mechanisms. Specialist review will assess technical plausibility and missing confounders.

## 10. Ethics approval gate

Before real-data extraction or specialist-response collection, the researcher will confirm with the relevant UNMSM committee whether the study is exempt, requires expedited review, or requires full review. Approval will not be assumed retroactively.

## 11. Scientific-integrity commitments

The researcher will preserve protocol deviations, exclusions, negative results, version history, and AI-use disclosures. No synthetic result will be presented as an operational finding.
