import pandas as pd
import sys
import os
import joblib
import time
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
import pickle

def train(hist_csv: str, fut_csv: str, out_model: str):
    # --- Load datasets ---
    hist = pd.read_csv(hist_csv)
    fut = pd.read_csv(fut_csv)

    print("Historical shape:", hist.shape)
    print("Future shape:", fut.shape)

    # --- Clean historical ---
    hist = hist.dropna().reset_index(drop=True)

    # --- Features and target from historical ---
    X = hist.drop(columns=["target", "date"])
    y = hist["target"]

    # --- Train/test split (last 20% as test) ---
    split_idx = int(len(hist) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    # --- Define model ---
    model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    # --- Train ---
    model.fit(X_train, y_train)

    # --- Evaluate ---
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    metrics = {"MAE": mae, "R2": r2}
    print("Evaluation metrics:", metrics)

    # --- Save model (joblib) ---
    os.makedirs(os.path.dirname(out_model), exist_ok=True)
    joblib.dump(model, out_model)
    print(f"Model saved to {out_model}")

    # --- ALSO save pickle copy into model-app ---
    with open("model-app/model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved to model-app/model.pkl")

    # --- Predict on future data (no target column) ---
    if "date" in fut.columns:
        fut_features = fut.drop(columns=["date"])
    else:
        fut_features = fut

    future_preds = model.predict(fut_features)
    fut["prediction"] = future_preds
    fut.to_csv("predictions/future_predictions.csv", index=False)
    print("📈 Future predictions saved to predictions/future_predictions.csv")

    return metrics


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python train.py <historical_csv> <future_csv> <output_model>")
        sys.exit(1)

    hist_csv = sys.argv[1]
    fut_csv = sys.argv[2]
    out_model = sys.argv[3]

    if out_model.lower() in ["auto", "-", ""]:
        ts = int(time.time())
        out_model = f"models/xgb_model_{ts}.joblib"

    metrics = train(hist_csv, fut_csv, out_model)
    print(out_model, metrics)
