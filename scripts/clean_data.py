import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

numeric_cols = ["DividendYield", "PayoutRatio", "NetMargin"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["DividendYield"] = df["DividendYield"].fillna(0)
df["PayoutRatio"] = df["PayoutRatio"].fillna(0)

df = df.dropna(subset=["DamodaranIndustry", "NetMargin"])

df = df[(df["PayoutRatio"] >= 0) & (df["PayoutRatio"] <= 5)]
df = df[(df["DividendYield"] >= 0) & (df["DividendYield"] <= 20)]

df.to_csv("data/clean_final_dataset.csv", index=False)

print("Rows after cleaning:", len(df))
print()
print("Missing values:")
print(df.isna().sum())
print()
print(df.head())