import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/clean_final_dataset.csv")

industry_df = df.groupby('DamodaranIndustry').agg({
    'NetMargin': 'first',
    'PayoutRatio': 'mean',
    'Ticker': 'count'
}).dropna()

filtered_df = industry_df[industry_df['Ticker'] >= 5]

plt.figure(figsize=(12, 8))
sns.regplot(data=filtered_df, x='NetMargin', y='PayoutRatio', scatter_kws={'alpha':0.5})
plt.title('Industry Net Margin vs. Average Payout Ratio')
plt.xlabel('Industry Average Net Margin')
plt.ylabel('Average Company Payout Ratio')

for i, txt in enumerate(filtered_df.index):
    plt.annotate(txt, (filtered_df['NetMargin'].iat[i], filtered_df['PayoutRatio'].iat[i]), fontsize=8, alpha=0.7)

plt.grid(True, linestyle='--', alpha=0.6)
plt.show()