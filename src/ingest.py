import pandas as pd
from pydantic import BaseModel, Field
import sys
import os

# Define a schema for validation
class Record(BaseModel):
    date: str = Field(..., description="Timestamp of the record")
    temp: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., description="Humidity percentage")
    wind: float = Field(..., description="Wind speed in m/s")
    precipitation_mm: float = Field(..., description="Precipitation in mm")
    target: float = Field(..., description="Next-hour temperature target")

def ingest(in_csv: str, out_csv: str):
    # Load dataset
    df = pd.read_csv(in_csv)

    # Debug: print columns
    print("Ingesting dataset with columns:", df.columns.tolist())

    # Validate each row with Pydantic
    valid = []
    for _, r in df.iterrows():
        try:
            # ✅ Use .model_dump() instead of .dict()
            rec = Record(**r.to_dict()).model_dump()
            valid.append(rec)
        except Exception as e:
            print("Validation error:", e)

    # Create validated DataFrame
    df_valid = pd.DataFrame(valid)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    # Save validated dataset
    df_valid.to_csv(out_csv, index=False)
    print(f"Ingested dataset saved to {out_csv} with shape {df_valid.shape}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ingest.py <input_csv> <output_csv>")
    else:
        ingest(sys.argv[1], sys.argv[2])
