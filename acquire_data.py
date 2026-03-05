import requests
import pandas as pd
import matplotlib.pyplot as plt
import hashlib

# 1. Read API key
with open("fred_apikey.txt", "r") as f:
    api_key = f.read().strip()

# 2. Request data from FRED API
url = "https://api.stlouisfed.org/fred/series/observations"

params = {
    "series_id": "SP500",
    "api_key": api_key,
    "file_type": "json",
    "observation_start": "2019-01-01",
    "observation_end": "2024-01-01"
}

response = requests.get(url, params=params)
data = response.json()

# 3. Convert to dataframe
df = pd.DataFrame(data["observations"])

# 4. Keep only necessary columns
df = df[["date", "value"]]

# 5. Convert data types
df["date"] = pd.to_datetime(df["date"])
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# 6. Drop missing values
df = df.dropna()

# 7. Save CSV
df.to_csv("sp500.csv", index=False)

# 8. Plot figure
plt.figure(figsize=(8,5))
plt.plot(df["date"], df["value"])
plt.xlabel("Date")
plt.ylabel("Index Value")
plt.title("S&P 500 (2019-2024)")
plt.tight_layout()

plt.savefig("sp500.png")

# 9. Compute SHA-256
with open("sp500.csv","rb") as f:
    file_bytes = f.read()
    sha = hashlib.sha256(file_bytes).hexdigest()

with open("sp500.sha","w") as f:
    f.write(sha)

