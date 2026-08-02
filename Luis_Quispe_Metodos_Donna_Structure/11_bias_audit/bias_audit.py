from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "bias_audit_splits.csv")
gaps = df[df["metric"].isin([
    "Statistical parity difference",
    "Equal opportunity difference",
    "Average odds difference"
])].copy()

x = range(len(gaps))
width = 0.35
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar([i - width/2 for i in x], gaps["before"], width, label="Before")
ax.bar([i + width/2 for i in x], gaps["after"], width, label="After")
ax.axhline(0, linewidth=1)
ax.set_xticks(list(x))
ax.set_xticklabels(gaps["metric"], rotation=15, ha="right")
ax.set_ylabel("Difference; 0 = parity")
ax.set_title("COMPAS course calibration: fairness gaps before and after Reweighing")
ax.legend()
fig.tight_layout()
fig.savefig(ROOT / "before_after_chart.png", dpi=170)
print("Wrote before_after_chart.png")
