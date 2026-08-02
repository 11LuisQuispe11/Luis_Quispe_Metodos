from pathlib import Path
import argparse
import json
import joblib
import numpy as np
import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calc(y_true, y_pred):
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred) ** 0.5),
        "r2": float(r2_score(y_true, y_pred))
    }

def main(config_path, data_path, model_path, predictions_path, metrics_path, comparison_path):
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    df = pd.read_csv(data_path, parse_dates=["firing_datetime"])
    train = df[df["year"].isin(config["split"]["train_years"])].copy()
    test = df[df["year"].isin(config["split"]["test_years"])].copy()

    features = [
        "holes_count", "bench_anon", "powder_factor_kg_t", "ucs_mpa",
        "rmr", "moisture_pct", "mean_payload_t", "throughput_tph",
        "traceability_confidence", "crusher_id"
    ]
    numeric = features[:-2]
    categorical = features[-2:]
    target = "average_power_kw"

    preprocessing = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical)
    ])

    cfg = config["model"]
    proposed = Pipeline([
        ("preprocess", preprocessing),
        ("model", HistGradientBoostingRegressor(
            learning_rate=cfg["learning_rate"],
            max_iter=cfg["max_iter"],
            max_leaf_nodes=cfg["max_leaf_nodes"],
            l2_regularization=cfg["l2_regularization"],
            random_state=cfg["random_state"]
        ))
    ])
    linear = Pipeline([
        ("preprocess", preprocessing),
        ("model", LinearRegression())
    ])

    X_train, y_train = train[features], train[target]
    X_test, y_test = test[features], test[target]

    proposed.fit(X_train, y_train)
    linear.fit(X_train, y_train)

    p_hgb = proposed.predict(X_test)
    p_lin = linear.predict(X_test)
    p_mean = np.repeat(y_train.mean(), len(y_test))

    results = {
        "scientific_status": "synthetic demonstration only",
        "train_rows": int(len(train)),
        "test_rows": int(len(test)),
        "train_years": config["split"]["train_years"],
        "test_years": config["split"]["test_years"],
        "target": target,
        "models": {
            "historical_mean": calc(y_test, p_mean),
            "linear_regression": calc(y_test, p_lin),
            "hist_gradient_boosting": calc(y_test, p_hgb)
        }
    }

    pred = test[["blast_name", "year", "firing_datetime", target]].copy()
    pred["prediction_hgb_kw"] = p_hgb
    pred["prediction_linear_kw"] = p_lin
    pred["prediction_mean_kw"] = p_mean
    pred["absolute_error_hgb_kw"] = np.abs(y_test.to_numpy() - p_hgb)

    comparison = pd.DataFrame([
        {"model": name, **values} for name, values in results["models"].items()
    ]).sort_values("mae")

    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(proposed, model_path)
    pred.to_csv(predictions_path, index=False)
    Path(metrics_path).write_text(json.dumps(results, indent=2), encoding="utf-8")
    comparison.to_csv(comparison_path, index=False)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="params.yaml")
    parser.add_argument("--data", default="data/processed/synthetic_blast_crusher.csv")
    parser.add_argument("--model", default="results/model.joblib")
    parser.add_argument("--predictions", default="results/predictions.csv")
    parser.add_argument("--metrics", default="results/metrics.json")
    parser.add_argument("--comparison", default="results/model_comparison.csv")
    args = parser.parse_args()
    main(args.config, args.data, args.model, args.predictions, args.metrics, args.comparison)
