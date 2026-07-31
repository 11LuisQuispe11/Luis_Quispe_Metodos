"""Generate synthetic data calibrated from verified aggregate statistics.

This script does not use raw operational data.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
AGGREGATES = {
    2024: {"blasts": 1070, "holes": 154821, "min": 1, "max": 907, "median": 112},
    2025: {"blasts": 1039, "holes": 180018, "min": 4, "max": 1297, "median": 140},
    2026: {"blasts": 516, "holes": 77704, "min": 4, "max": 779, "median": 123},
}

def allocate_holes_exact(n, total, min_value, max_value, median_hint, rng):
    values = np.clip(np.rint(rng.lognormal(np.log(median_hint), 0.75, n)), min_value, max_value).astype(int)
    values[0] = min_value
    values[1] = max_value
    diff = total - int(values.sum())
    idxs = np.arange(2, n)
    attempts = 0
    while diff != 0 and attempts < 250000:
        attempts += 1
        if diff > 0:
            candidates = idxs[values[idxs] < max_value]
            i = rng.choice(candidates)
            step = min(diff, max_value-values[i], 5)
            values[i] += step
            diff -= step
        else:
            candidates = idxs[values[idxs] > min_value]
            i = rng.choice(candidates)
            step = min(-diff, values[i]-min_value, 5)
            values[i] -= step
            diff += step
    if int(values.sum()) != total:
        raise RuntimeError("Could not match aggregate total")
    return values

def main():
    rng = np.random.default_rng(SEED)
    out = Path('eda/data/synthetic')
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for year, cfg in AGGREGATES.items():
        holes = allocate_holes_exact(cfg['blasts'], cfg['holes'], cfg['min'], cfg['max'], cfg['median'], rng)
        dates = pd.date_range(f'{year}-01-01', '2026-06-17' if year == 2026 else f'{year}-12-31', periods=cfg['blasts'])
        for i, (h, dt) in enumerate(zip(holes, dates), start=1):
            rows.append({'blast_name': f'BLST_{year}_{i:04d}', 'year': year, 'firing_datetime': dt, 'holes_count': int(h), 'bench_anon': int(rng.choice(np.arange(3600,4305,15)))})
    blasts = pd.DataFrame(rows)
    blasts.to_csv(out/'synthetic_blasts.csv', index=False)
    print(blasts.groupby('year').agg(blasts=('blast_name','nunique'), holes=('holes_count','sum'), min_holes=('holes_count','min'), max_holes=('holes_count','max')))

if __name__ == '__main__':
    main()
