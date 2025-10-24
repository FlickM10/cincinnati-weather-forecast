import pandas as pd
import sys
import os
import joblib

def predict(in_csv: str, model_path: str, out_csv: str):
    # Load dataset
    df = pd.read_csv(in_csv)
    print("Prediction dataset shape:", df.shape)

    # Load trained model
    model = joblib.load(model_path)

    # Define the expected feature order (same as training)
    expected_features = ["temp", "humidity", "wind", "precipitation_mm"]

    # Check for missing features
    missing = [f for f in expected_features if f not in df.columns]
    if missing:
        raise ValueError(f"Missing required features in input: {missing}")

    # Reorder columns to match training
    X = df[expected_features]

    # Run predictions
    preds = model.predict(X)

    # Add predictions to DataFrame
    df["prediction"] = preds

    # Ensure output directory exists
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    # Save predictions
    df.to_csv(out_csv, index=False)
    print(f"Predictions saved to {out_csv} with shape {df.shape}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python predict.py <input_csv> <model_path> <output_csv>")
        sys.exit(1)

    predict(sys.argv[1], sys.argv[2], sys.argv[3])
