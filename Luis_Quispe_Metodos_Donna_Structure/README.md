# UNMSM Research Methods and Scientific Integrity in AI

**Author:** Luis Quispe Inquil  
**Institution:** Universidad Nacional Mayor de San Marcos  
**Program:** Doctoral Program in Deep Technologies with a Focus on Artificial Intelligence and Emerging Technologies  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies  
**Instructor:** Dr. Loveleen Gaur

## Project focus

This repository organizes the course deliverables around the following research topic:

> **Probabilistic, adaptive, and interpretable prediction of primary-crusher energy demand from blast-design and mine-to-plant traceability data in an anonymous Peruvian open-pit copper mine.**

## Academic purpose

The repository follows the sequence of the course: paradigm selection, method choice, protocol development, systematic literature review, reproducible pipeline design, reproducibility audit, Model Card and Datasheet, research ethics, responsible data management, algorithmic-bias audit, and publication integrity.

The repository contains no raw confidential operational data. Public row-level data are synthetic and are used only to demonstrate reproducible methods. The only real operational evidence published here is anonymous aggregate information previously verified by the researcher.

## Verified aggregate foundation

- Study period: 1 January 2024 to 17 June 2026.
- Unique fired blasts: 2,625.
- Blast-hole records: 412,543.
- Primary blast identifier: `blast_name`.
- Traceability design: `blast_name/polygon -> shovel -> truck/LOADID -> payload -> dump timestamp -> primary crusher -> power window`.
- Confirmed primary-crusher power tags: `Chancadora 01 - KW` and `Chancadora 02 - KW`.
- Academic use: anonymous and non-identifying; mine and source systems are not disclosed.

## Repository structure

- `01_paradigm/`: research paradigm justification.
- `02_method/`: method comparison and methodological fit matrix.
- `03_protocol/`: archived protocol v0.1 and revised protocol v1.0.
- `04_literature/`: systematic review, gap analysis, and PRISMA diagram.
- `05_pipeline/`: executable synthetic ML pipeline with DVC and Docker scaffolding.
- `06_repro_audit/`: reproducibility audit and traceability report.
- `07_model_card/`: Model Card and Dataset Datasheet.
- `09_ethics/`: ethics protocol for the industrial-data study.
- `10_data_mgmt/`: Data Management Plan and legal-compliance checklist.
- `11_bias_audit/`: reproducible COMPAS course-calibration evidence and report.
- `12_integrity/`: personal AI-use policy and retracted-paper analysis.

## Scientific-integrity boundary

The synthetic pipeline demonstrates code structure, temporal splitting, artifact tracing, and reporting. Its results are not operational findings and must not be described as performance on the real mine.

Instructor-provided slides, handbooks, and original notebooks are not republished in this repository.
