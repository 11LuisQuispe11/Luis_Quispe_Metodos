# Data Management Plan

**Project:** Primary-Crusher Energy Demand Prediction from Blast and Mine-to-Plant Data  
**Version:** 1.0 course draft  
**Review requirement:** Confirm with supervisor, data owner, and institutional data-protection contact before real-data collection

## 1. Data description

The study may use blast-design, blast-execution, hole-coordinate, truck-cycle, payload, dumping-time, crusher-destination, and primary-crusher historian data. The verified aggregate inventory covers 2,625 fired blasts and 412,543 hole records from 1 January 2024 to 17 June 2026.

Restricted analytical data would be stored in columnar formats such as Parquet, with CSV extracts only when necessary. Documentation will use Markdown, YAML, JSON, and a versioned data dictionary. The public repository contains synthetic data only.

## 2. FAIR compliance

**Findable:** code and public documentation will be indexed in GitHub and, at the final publication stage, archived in Zenodo or an institutional repository with a DOI.

**Accessible:** synthetic data and public documentation may be openly accessible. Restricted operational data will remain FAIR through clear metadata, identifiers, and access conditions, even though they are not open.

**Interoperable:** use CSV/Parquet, ISO-formatted timestamps, UTF-8 encoding, explicit units, a codebook, and controlled category definitions.

**Reusable:** each public artifact will include provenance, version, license, intended use, prohibited use, and reproducibility instructions. Code may use MIT terms and original documents CC BY 4.0, subject to institutional approval.

## 3. Anonymization approach

Direct operational identifiers will be removed or pseudonymized. Coordinates will be translated, generalized, or excluded; timestamps may be aggregated; equipment and location codes will be mapped to non-identifying labels; public summaries will suppress rare cells with fewer than five operational units.

Formal k-anonymity and l-diversity are not the principal mechanism because no person-level dataset is intended for public release. Nevertheless, the minimum-cell-size rule provides an operational analogue against singling out rare events. Differential privacy is not assigned an epsilon at this stage because only approved aggregates and synthetic data are public. If real query outputs are later released, the privacy mechanism and budget will be selected with institutional review and the utility loss will be reported.

## 4. Storage and backup

Restricted data will reside in encrypted institutional or data-owner-approved storage. Access will be role-based, least-privilege, and logged. Data will not be synchronized to personal public cloud accounts or committed to GitHub.

The backup plan follows the 3-2-1 principle: a primary encrypted working copy, a second protected copy, and one encrypted off-site or institutionally managed copy. Recovery will be tested periodically.

## 5. Legal compliance

The project will use Ley 29733 as the baseline if any personal data are encountered, although the intended analytical dataset is operational rather than person-level. Institutional authorization, purpose limitation, confidentiality, and intellectual-property restrictions apply independently of personal-data status.

GDPR applicability is currently not expected because no EU data subjects are planned. Cross-border transfer is not planned. Any later change will trigger a new legal assessment and documented transfer mechanism before data movement.

The current course checklist and breach-response timing must be verified against the rule in force at the time of collection and the institution's internal process.

## 6. Sharing plan

Public sharing will include:

- protocol and audit documents;
- synthetic data generator;
- synthetic supporting notebook;
- aggregate statistics approved for publication;
- code templates;
- Model Card, Datasheet, DMP, and reproducibility manifest.

Raw operational records, real coordinates, equipment identifiers, security configurations, and personnel-related fields will not be shared publicly. Controlled access, if allowed, will require a data-use agreement and an approved research purpose.

## 7. Retention and disposal

Research records, code, public documentation, and approved anonymized outputs will be retained for at least five years after thesis completion unless institutional or contractual rules require otherwise.

Restricted raw data will be deleted, returned, or archived according to the data-use agreement. Secure deletion will be documented, including date, storage location, responsible person, and method. Public synthetic data may be retained indefinitely with clear versioning.


---

# Legal Compliance Checklist

**Status:** Course-aligned draft. Verify with the competent institutional office before real-data collection.

| # | Requirement | Yes / N/A | Project-specific justification |
|---:|---|---|---|
| 1 | Lawful basis for processing is recorded | YES | Anonymous academic-use authorization exists; formal record must be archived privately |
| 2 | Consent is specific, informed, and documented | N/A | No individual human participants are planned; specialist review will require voluntary consent |
| 3 | Sensitive personal data are identified | YES | None are intended; schema review will check operator names/IDs and free text |
| 4 | Data minimization is applied | YES | Only variables needed for traceability and prediction are retained |
| 5 | Ley 29733 obligations are mapped | YES | Applies if personal data appear; current design removes such fields |
| 6 | GDPR applicability is checked | N/A | No EU data subjects are planned; reassess if scope changes |
| 7 | Cross-border transfer mechanism exists | N/A | No cross-border transfer is planned |
| 8 | Storage, encryption, and access controls are defined | YES | Encrypted approved storage, least privilege, access logging |
| 9 | Breach-response plan exists | YES | Follow institutional and applicable legal notification process; verify deadline before collection |
| 10 | Retention and secure-deletion date are defined | YES | Five years after thesis or shorter contractual period |
| 11 | Data Protection Officer consulted if required | N/A / PENDING | Consult if personal data, cross-border transfer, or public release is introduced |
| 12 | CARE principles applied for Indigenous-community data | N/A | No Indigenous-community data are planned; new scope would require collective-governance review |

## Release gate

No real data collection, extraction, or transfer should begin until every item is either confirmed YES or documented N/A by the responsible institutional authority.
