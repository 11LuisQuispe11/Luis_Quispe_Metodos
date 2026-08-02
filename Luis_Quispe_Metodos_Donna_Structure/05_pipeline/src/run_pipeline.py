import subprocess
import sys

for cmd in [
    [sys.executable, "src/generate_data.py", "--config", "params.yaml"],
    [sys.executable, "src/train.py", "--config", "params.yaml"],
    [sys.executable, "src/evaluate.py"]
]:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)

print("Pipeline completed successfully.")
