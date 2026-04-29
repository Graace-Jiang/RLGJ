import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the updated dataset
df = pd.read_csv("data/clean_final_dataset.csv")

# Change 'IndustryMapped' to 'DamodaranIndustry'
industry_df = df.groupby('DamodaranIndustry').agg({
    'NetMargin': 'first',
    'PayoutRatio': 'mean',
    'Ticker': 'count'
}).dropna()

# Filter and model as before
filtered_data = industry_df[industry_df['Ticker'] >= 5]
X = filtered_data[['NetMargin']]
y = filtered_data['PayoutRatio']

model = LinearRegression().fit(X, y)

print(f"R-Squared: {model.score(X, y)}")
print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")