import pandas as pd

hist = pd.read_csv("data_raw/historical.csv")
fut = pd.read_csv("data_raw/future.csv")

# Ensure same columns
fut = fut[hist.columns]

combined = pd.concat([hist, fut], ignore_index=True)
combined.to_csv("data_raw/combined.csv", index=False)
