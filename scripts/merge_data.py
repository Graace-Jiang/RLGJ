import pandas as pd

df_company = pd.read_csv("data/industry_mapped_openrefine.csv")

df_margin = pd.read_excel(
    "data/marginGlobal.xls",
    sheet_name="Industry Averages",
    header=None
)

df_margin = df_margin.iloc[9:, [0, 3]].copy()
df_margin.columns = ["Industry", "NetMargin"]
df_margin = df_margin.dropna(subset=["Industry", "NetMargin"])
df_margin["NetMargin"] = pd.to_numeric(df_margin["NetMargin"], errors="coerce")

df_merged = pd.merge(
    df_company,
    df_margin,
    left_on="DamodaranIndustry",
    right_on="Industry",
    how="left"
)

df_merged.to_csv("data/final_dataset.csv", index=False)

missing = df_merged[df_merged["NetMargin"].isna()].copy()

missing_summary = (
    missing["DamodaranIndustry"]
    .fillna("MISSING_DAMODARAN_INDUSTRY")
    .value_counts()
    .reset_index()
)
missing_summary.columns = ["DamodaranIndustry", "Count"]
missing_summary.to_csv("data/missing_damodaran_industries.csv", index=False)

print("Merged rows:", len(df_merged))
print("Missing NetMargin:", df_merged["NetMargin"].isna().sum())
print()
print("Top missing DamodaranIndustry values:")
print(missing_summary.head(30))
print()
print(df_merged.head())