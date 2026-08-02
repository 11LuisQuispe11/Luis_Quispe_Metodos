# Model Information Sheet

## Claim boundary

The pipeline makes no scientific claim about actual mine performance. It demonstrates a leakage-aware and reproducible workflow.

## Data split

- Training: 2024-2025.
- Test: 2026.
- No random row-level shuffle across years.

## Leakage controls

- Preprocessing is fitted inside the training pipeline.
- No target-derived feature is used.
- The final test period is not used for fitting.
- The unit is a blast-level synthetic record, not a second-level historian row.

## Reproduction command

```bash
python src/run_pipeline.py
```

## Limitations

- All row-level variables and targets are synthetic.
- The real linked-cohort size is unknown.
- Historian extraction semantics remain to be verified.
- The demonstration predicts average power only.
