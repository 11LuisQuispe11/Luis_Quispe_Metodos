from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import yaml

def allocate_exact(n, total, min_value, max_value, median_hint, rng):
    values = rng.lognormal(np.log(max(median_hint, 1)), 0.75, n)
    values = np.clip(np.rint(values), min_value, max_value).astype(int)
    values[0] = min_value
    values[1] = max_value
    diff = int(total - values.sum())
    indices = np.arange(2, n)
    while diff != 0:
        if diff > 0:
            candidates = indices[values[indices] < max_value]
            idx = rng.choice(candidates)
            step = min(diff, max_value - values[idx], 5)
            values[idx] += step
            diff -= step
        else:
            candidates = indices[values[indices] > min_value]
            idx = rng.choice(candidates)
            step = min(-diff, values[idx] - min_value, 5)
            values[idx] -= step
            diff += step
    return values

def main(config_path, output_path):
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    rng = np.random.default_rng(config["data"]["seed"])
    rows = []

    for year, cfg in config["data"]["years"].items():
        year = int(year)
        holes = allocate_exact(cfg["blasts"], cfg["holes"], cfg["min"], cfg["max"], cfg["median"], rng)
        end = config["data"]["study_end"] if year == 2026 else f"{year}-12-31"
        dates = pd.date_range(f"{year}-01-01", end, periods=cfg["blasts"])
        rng.shuffle(holes)

        for i, (date, hole_count) in enumerate(zip(dates, holes), start=1):
            throughput = np.clip(rng.normal(2550, 420), 1200, 3800)
            ucs = np.clip(rng.normal(155, 42), 45, 310)
            rmr = np.clip(rng.normal(58, 13), 20, 90)
            moisture = np.clip(rng.normal(3.2, 1.2), 0.2, 9)
            powder = np.clip(rng.normal(0.45, 0.10), 0.18, 0.85)
            payload = np.clip(rng.normal(350, 20), 290, 420)
            crusher = rng.choice(["CR01", "CR02"], p=[0.56, 0.44])
            trace = rng.choice(["HIGH", "MEDIUM", "LOW"], p=[0.72, 0.18, 0.10])
            crusher_effect = 120 if crusher == "CR01" else 0
            trace_noise = {"HIGH": 0, "MEDIUM": 45, "LOW": 110}[trace]

            average_power = (
                300 + 0.70 * throughput + 2.2 * ucs + 0.70 * hole_count
                + 15 * moisture + 210 * powder + crusher_effect
                + rng.normal(0, 115 + trace_noise)
            )
            specific_energy = average_power / throughput
            peak_power = average_power * np.clip(rng.normal(1.18, 0.06), 1.05, 1.42)

            rows.append({
                "blast_name": f"BLST_{year}_{i:04d}",
                "year": year,
                "firing_datetime": date,
                "holes_count": int(hole_count),
                "bench_anon": int(rng.choice(np.arange(3600, 4305, 15))),
                "powder_factor_kg_t": float(powder),
                "ucs_mpa": float(ucs),
                "rmr": float(rmr),
                "moisture_pct": float(moisture),
                "mean_payload_t": float(payload),
                "throughput_tph": float(throughput),
                "traceability_confidence": trace,
                "crusher_id": crusher,
                "average_power_kw": float(average_power),
                "specific_energy_kwh_t": float(specific_energy),
                "peak_power_kw": float(peak_power),
                "data_status": "SYNTHETIC"
            })

    df = pd.DataFrame(rows).sort_values("firing_datetime").reset_index(drop=True)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Wrote {len(df):,} synthetic records to {out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    parser.add_argument("--output", default="data/processed/synthetic_blast_crusher.csv")
    args = parser.parse_args()
    main(args.config, args.output)
