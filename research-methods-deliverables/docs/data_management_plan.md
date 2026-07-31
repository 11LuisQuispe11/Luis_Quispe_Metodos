# Data Management Plan and Legal Compliance Checklist

**Project:** Probabilistic, Adaptive, and Interpretable Prediction of Primary Crusher Energy Demand from Blast-Design Data  
**Status:** Draft for course alignment; to be updated before real data extraction.

## 1. Data description

The research may use blast-design, blast-execution, truck-cycle, payload, crusher-historian, and derived processing-window data. The GitHub repository contains only synthetic data calibrated from verified aggregate statistics.

## 2. FAIR compliance

| FAIR principle | Planned implementation |
|---|---|
| Findable | Repository README, structured folders, data dictionary, versioned files. |
| Accessible | Synthetic data are accessible in the repository; raw data remain restricted. |
| Interoperable | CSV, Markdown, YAML, Python scripts, and documented variable names. |
| Reusable | Clear license/conditions for synthetic material; explicit prohibition on operational interpretation. |

## 3. Anonymization and confidentiality

Raw operational identifiers will not be published. Coordinates, mine name, source-system name, truck identifiers, shovel identifiers, personnel names, and equipment codes must be removed, generalized, or pseudonymized before academic reporting.

## 4. Storage and backup

Raw data, if re-obtained, must be stored in encrypted institutional or approved storage. Public GitHub must contain only synthetic, aggregated, or non-identifying documentation.

## 5. Legal and institutional compliance

The project will follow UNMSM rules, the CONCYTEC National Code of Scientific Integrity, and applicable Peruvian data-protection requirements. Although industrial process data are not human-subject medical data, operational confidentiality and intellectual-property constraints still apply.

## 6. Sharing plan

Public sharing will be limited to:

- protocol documents;
- synthetic EDA demonstration;
- aggregate statistics;
- code templates;
- non-identifying figures;
- model documentation.

Restricted materials will not be uploaded.

## 7. Retention period

Synthetic data can be retained with the repository. Any future raw data should follow the authorization agreement and be deleted or archived according to institutional policy after thesis completion.

## 8. Compliance checklist

- [x] No raw operational rows in GitHub.
- [x] No real coordinates published.
- [x] No mine name published.
- [x] No source-system name published.
- [x] No personnel identifiers published.
- [x] Synthetic data labelled as synthetic.
- [x] Aggregate evidence separated from simulated rows.
- [ ] Formal authorization record archived privately.
- [ ] Final data dictionary completed after any future authorized extraction.
- [ ] DVC or hash-based data versioning added for real restricted datasets.
