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

industry_mapping = {
    "Consumer Electronics": "Electronics (Consumer & Office)",
    "Software - Infrastructure": "Computer Services",
    "Internet Content & Information": "Advertising",
    "Internet Retail": "Retail (General)",  
    "Auto Manufacturers": "Auto & Truck"
}

df_company["IndustryMapped"] = df_company["Industry"].replace(industry_mapping)

df_merged = pd.merge(
    df_company,
    df_margin,
    left_on="IndustryMapped",
    right_on="Industry",
    how="left"
)

df_merged = df_merged[[
    "Ticker",
    "Industry_x",
    "IndustryMapped",
    "Sector",
    "DividendYield",
    "PayoutRatio",
    "NetMargin"
]]

df_merged = df_merged.rename(columns={
    "Industry_x": "YahooIndustry"
})

df_merged.to_csv("data/final_dataset.csv", index=False)

print("Merged data:")
print(df_merged.head())
print()
print("Missing NetMargin after mapping:", df_merged["NetMargin"].isna().sum())