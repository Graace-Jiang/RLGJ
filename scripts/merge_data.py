import pandas as pd

df_company = pd.read_csv("data/sp500_dividend_data.csv")

df_margin = pd.read_excel(
    "data/marginGlobal.xls",
    sheet_name="Industry Averages",
    header=None
)

df_margin = df_margin.iloc[9:, [0, 3]].copy()
df_margin.columns = ["Industry", "NetMargin"]

df_margin = df_margin.dropna(subset=["Industry", "NetMargin"])
df_margin["NetMargin"] = pd.to_numeric(df_margin["NetMargin"], errors="coerce")

print("Damodaran industries:")
print(sorted(df_margin["Industry"].dropna().unique()))
print()

df_map = pd.read_csv("data/industry_mapping.csv")
mapping_dict = dict(zip(df_map["YahooIndustry"], df_map["DamodaranIndustry"]))

df_company["IndustryMapped"] = df_company["Industry"].replace(mapping_dict)

df_company["IndustryMapped"] = df_company["IndustryMapped"].fillna(df_company["Industry"])

df_merged = pd.merge(
    df_company,
    df_margin,
    left_on="IndustryMapped",
    right_on="Industry",
    how="left"
)

df_merged.to_csv("data/final_dataset.csv", index=False)

unmatched = (
    df_merged[df_merged["NetMargin"].isna()][["Ticker", "Industry_x", "IndustryMapped"]]
    .drop_duplicates()
    .sort_values(["Industry_x", "Ticker"])
)

unmatched.columns = ["Ticker", "YahooIndustry", "IndustryMapped"]

unmatched.to_csv("data/unmatched_industries.csv", index=False)

print("Merged rows:", len(df_merged))
print("Missing NetMargin:", df_merged["NetMargin"].isna().sum())
print()
print("Unmatched industries saved to data/unmatched_industries.csv")
print(unmatched.head(20))