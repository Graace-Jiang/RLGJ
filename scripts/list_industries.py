import pandas as pd

df = pd.read_csv("data/sp500_dividend_data.csv")

industry_counts = (
    df["Industry"]
    .fillna("Missing")
    .value_counts()
    .reset_index()
)

industry_counts.columns = ["YahooIndustry", "Count"]

industry_counts.to_csv("data/yahoo_industry_counts.csv", index=False)

print(industry_counts.head(50))
print()
print("Total unique Yahoo industries:", len(industry_counts))