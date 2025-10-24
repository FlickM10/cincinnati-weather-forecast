import pandas as pd, os, time

def add_lags(in_csv: str, out_dir="data/interim"):
    os.makedirs(out_dir, exist_ok=True)
    df = pd.read_csv(in_csv).sort_values("date")
    for col in ["temp","humidity","wind"]:
        df[f"{col}_lag1"] = df[col].shift(1)
        df[f"{col}_roll3"] = df[col].rolling(3).mean()
    df = df.dropna()
    out_path = os.path.join(out_dir, f"lagged_{int(time.time())}.csv")
    df.to_csv(out_path, index=False)
    print(out_path)

if __name__ == "__main__":
    import sys; add_lags(sys.argv[1])
