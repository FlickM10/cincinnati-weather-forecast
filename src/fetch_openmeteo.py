import requests
import pandas as pd

# Cincinnati coordinates
lat, lon = 39.1031, -84.5120

# Choose your time range
start_date = "2020-01-01"
end_date   = "2024-12-31"

# Open-Meteo API endpoint
url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={lat}&longitude={lon}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
    f"&timezone=America/New_York"
)

print("Fetching data from:", url)
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

# Add target column (shifted temp for next hour)
df["target"] = df["temp"].shift(-1)

# Save to CSV
df.to_csv("data_raw/cincinnati_openmeteo.csv", index=False)
print("Saved:", df.shape)
