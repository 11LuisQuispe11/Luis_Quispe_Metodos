# Dataset Datasheet — Verified Aggregate Inventory and Synthetic Demonstration

**Dataset name:** Blast-to-Truck-to-Primary-Crusher Research Dataset  
**Version:** Design-stage documentation 0.3  
**Public release:** Synthetic demonstration only

## 1. Motivation

The dataset concept supports a doctoral study of whether blast-design and mine-to-plant traceability data can predict average power, specific energy, and peak-power risk in a primary crusher.

The public repository uses synthetic row-level records because the operational data are confidential and database access is no longer available.

## 2. Composition

Verified non-identifying aggregate evidence:

| Year | Unique fired blasts | Hole records | Range | Mean | Median |
|---:|---:|---:|---:|---:|---:|
| 2024 | 1,070 | 154,821 | 1–907 | 144.69 | 112 |
| 2025 | 1,039 | 180,018 | 4–1,297 | 173.26 | 140 |
| 2026 to 17 June | 516 | 77,704 | 4–779 | 150.59 | 123 |

Total: **2,625 blasts** and **412,543 hole records**.

Planned restricted sources:

- blast and hole table;
- truck-cycle and payload table;
- primary-crusher historian;
- derived processing-window table.

Public synthetic tables:

- `synthetic_blasts.csv`;
- `synthetic_truck_cycles.csv`;
- `synthetic_crusher_signals.csv`.

## 3. Collection process

The verified aggregates were obtained from operational systems before database access ended. The traceability architecture records the source polygon or coordinates, loading equipment, truck and `LOADID`, payload, dumping timestamp, and crusher destination.

The public synthetic rows are generated deterministically from the aggregate configuration and do not reproduce real events.

## 4. Preprocessing, cleaning, and labelling

Planned preprocessing includes:

- classifying designed, loaded, and fired blasts;
- validating unique `blast_name` and hole identifiers;
- excluding stock-origin or ambiguous mixtures from the confirmatory cohort;
- validating payload hierarchy;
- aligning discharge timestamps with crusher-power windows;
- filtering invalid historian quality states;
- splitting chronologically before fitting transformations;
- retaining a complete exclusion log.

Synthetic missingness and quality flags are illustrative, not measured defect rates.

## 5. Uses

Recommended uses:

- reproducibility demonstration;
- protocol and data-governance design;
- traceability logic testing;
- Model Card and Datasheet preparation;
- code and notebook execution tests.

Prohibited uses:

- reporting actual mine KPIs;
- estimating real energy demand;
- identifying the mine or systems;
- production deployment;
- inferring personnel performance.

## 6. Distribution

Code, documentation, and synthetic demonstration files may be shared through GitHub and later archived with a DOI. Raw operational data will not be distributed publicly.

Any controlled-access sharing requires institutional and data-owner authorization, a purpose limitation, access logging, and a data-use agreement.

## 7. Maintenance

The student is responsible for maintaining this datasheet. Updates are required when:

- aggregate evidence changes;
- authorized data access is restored;
- the linked cohort is quantified;
- preprocessing rules change;
- a final model is trained;
- retention or sharing conditions change.

Unknown values must remain explicitly marked as unknown rather than estimated without evidence.
