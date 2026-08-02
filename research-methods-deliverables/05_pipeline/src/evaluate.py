from pathlib import Path
import argparse
import json
import pandas as pd
import matplotlib.pyplot as plt

def main(predictions_path, metrics_path, chart_path, summary_path):
    predictions = pd.read_csv(predictions_path, parse_dates=["firing_datetime"])
    metrics = json.loads(Path(metrics_path).read_text(encoding="utf-8"))

    sample = predictions.sort_values("firing_datetime").iloc[::max(1, len(predictions)//150)]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(sample["firing_datetime"], sample["average_power_kw"], label="Synthetic actual")
    ax.plot(sample["firing_datetime"], sample["prediction_hgb_kw"], label="HGB prediction")
    ax.set_title("Temporal holdout: synthetic primary-crusher average power")
    ax.set_xlabel("Date")
    ax.set_ylabel("Power (kW)")
    ax.legend()
    fig.autofmt_xdate()
    fig.tight_layout()
    Path(chart_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=160)
    plt.close(fig)

    best = metrics["models"]["hist_gradient_boosting"]
    linear = metrics["models"]["linear_regression"]
    mean = metrics["models"]["historical_mean"]
    summary = f"""# Synthetic Pipeline Result Summary

**Scientific status:** Synthetic demonstration only. These are not real mine-performance results.

## Temporal split

- Training: {metrics['train_years']} ({metrics['train_rows']:,} rows)
- Test: {metrics['test_years']} ({metrics['test_rows']:,} rows)

## Model comparison

| Model | MAE (kW) | RMSE (kW) | R2 |
|---|---:|---:|---:|
| Historical mean | {mean['mae']:.2f} | {mean['rmse']:.2f} | {mean['r2']:.3f} |
| Linear regression | {linear['mae']:.2f} | {linear['rmse']:.2f} | {linear['r2']:.3f} |
| HistGradientBoosting | {best['mae']:.2f} | {best['rmse']:.2f} | {best['r2']:.3f} |

The pipeline demonstrates temporal splitting, consistent preprocessing, comparable baselines, artifact serialization, and traceable outputs. It does not demonstrate operational validity because all row-level records and target values are synthetic.
"""
    Path(summary_path).write_text(summary, encoding="utf-8")
    print(f"Wrote {chart_path} and {summary_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", default="results/predictions.csv")
    parser.add_argument("--metrics", default="results/metrics.json")
    parser.add_argument("--chart", default="results/temporal_holdout_chart.png")
    parser.add_argument("--summary", default="results/result_summary.md")
    args = parser.parse_args()
    main(args.predictions, args.metrics, args.chart, args.summary)
