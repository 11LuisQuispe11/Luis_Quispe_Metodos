# Response to Instructor Feedback Memo v1.1

**Student:** Luis Quispe Inquil  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies  
**Program:** Doctoral Program in Deep Technologies with a Focus on Artificial Intelligence and Emerging Technologies  
**Institution:** Universidad Nacional Mayor de San Marcos  
**Revision date:** 17 June 2026

## Purpose

This memo summarizes the revisions made after the instructor feedback on the first full package of deliverables. The revised set resolves the apparent inconsistency between the protocol audit and the research protocol, quantifies the data foundation, clarifies the traceability design, and strengthens reproducibility, ethics, and PRISMA documentation.

## Main revisions completed

| Instructor comment | Revision made | File/location |
|---|---|---|
| Audit and Protocol appeared to describe different documents. | Added provenance notes and a version register. The audit now explicitly evaluates Proposal v0.0, while Protocol v0.3 is the revised current protocol. | `03_research_protocol_v0_3.md`; `04_research_protocol_audit_v1_2.md` |
| Data foundation was not quantified. | Added verified inventory for 1 January 2024 to 17 June 2026: 2,625 unique fired blasts and 412,543 blast-hole records. | Protocol Sections 6.3–6.5 |
| Traceability was not operationalized. | Defined the traceability chain: `blast_name/source polygon → loading equipment → truck/LOADID → measured payload → dump timestamp → selected primary crusher → crusher-power window`. | Protocol Section 6.4 |
| Online learning needed stronger defense. | Reframed online learning as conditional. Static and scheduled-retraining policies remain required comparators. | Protocol Sections 6.5 and 6.9 |
| Multiple outcomes were unclear. | Separated average power, specific energy, and peak power into target-specific modelling tasks. | Protocol Section 6.7 |
| Peak power required separate treatment. | Treated peak power as an upper-tail/threshold-exceedance problem. | Protocol Sections 5.3, 6.7, and 6.10 |
| E.D.F.C.V. required definition/attribution. | Defined E.D.F.C.V. as a course-specific analytical decision aid and explained equal weighting. | Method-Fit Matrix Sections 2–3 |
| SHAP review looked interpretivist. | Reframed specialist review as an artifact-validity check, not a separate epistemology. | Paradigm Justification; Protocol Sections 6.8 and 7 |
| PRISMA flow needed complete counts. | Added a reconciled pilot flow: 39 identified, 34 screened, 16 eligible full texts, 6 domain studies included, plus 4 methodological foundations outside PRISMA. | Mini-SLR Section 4 |

## Integrity note

The revised package distinguishes verified aggregate operational information from future raw-data analysis. Raw operational records, mine identifiers, source-system names, coordinates, and equipment identifiers are not published. Any synthetic-data workflow included in the repository is explicitly labelled as synthetic and is used only to demonstrate reproducible methodology.
