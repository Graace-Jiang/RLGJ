import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSummary:\n", df.describe())