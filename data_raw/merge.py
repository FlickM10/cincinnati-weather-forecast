import pandas as pd

hist = pd.read_csv("cincinnati_forecast_valid.csv")
fut = pd.read_csv("cincinnati_forecast_future.csv")

# Ensure same columns
fut = fut[hist.columns]

combined = pd.concat([hist, fut], ignore_index=True)
combined.to_csv("combined.csv", index=False)
