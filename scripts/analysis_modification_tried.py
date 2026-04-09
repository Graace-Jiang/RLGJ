import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("data/clean_final_dataset.csv")

industry_df = df.groupby('IndustryMapped').agg({
    'NetMargin': 'first',
    'PayoutRatio': 'mean',
    'Ticker': 'count'
}).rename(columns={'Ticker': 'CompanyCount'})


filtered_df = industry_df[industry_df['CompanyCount'] >= 5].reset_index()

print(f"Running model on {len(filtered_df)} unique industries...\n")

X = filtered_df['NetMargin']
y = filtered_df['PayoutRatio']

# Add constant for the intercept
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())

filtered_df.to_csv("data/industry_level_averages.csv", index=False)