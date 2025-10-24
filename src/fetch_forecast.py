import requests
import pandas as pd

# Cincinnati coordinates
lat, lon = 39.1031, -84.5120

# Forecast API endpoint (next 7 days by default)
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={lon}"
    f"&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
    f"&timezone=America/New_York"
)

print("Fetching forecast data from:", url)
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame({
    "date": data["hourly"]["time"],
    "temp": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"],
    "precipitation_mm": data["hourly"]["precipitation"],
    "wind": data["hourly"]["wind_speed_10m"],
})

# Save without target column (we want to predict it!)
df.to_csv("data_raw/cincinnati_forecast_future.csv", index=False)
print("Saved:", df.shape)
