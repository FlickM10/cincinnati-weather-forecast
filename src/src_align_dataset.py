import pandas as pd
import sys
import os

def align_dataset(in_csv: str, out_csv: str):
    # Load the raw dataset
    df = pd.read_csv(in_csv)

    # Print original columns for debugging
    print("Original columns:", df.columns.tolist())

    # Rename columns to match pipeline expectations
    df = df.rename(columns={
        "timestamp": "date",
        "temperature_C": "temp",       # <-- fixed here
        "humidity_percent": "humidity",
        "wind_speed_mps": "wind"
        # keep precipitation_mm as is (optional feature)
    })

    # Create target column: next-hour temperature
    if "temp" not in df.columns:
        raise ValueError("Column 'temp' not found after renaming. Check your CSV headers.")

    df["target"] = df["temp"].shift(-1)

    # Drop last row (no target available)
    df = df.dropna()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    # Save aligned dataset
    df.to_csv(out_csv, index=False)
    print(f"Aligned dataset saved to {out_csv} with shape {df.shape}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python src_align_dataset.py <input_csv> <output_csv>")
    else:
        align_dataset(sys.argv[1], sys.argv[2])
