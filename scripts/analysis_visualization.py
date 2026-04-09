import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/clean_final_dataset.csv")


correlation = df['NetMargin'].corr(df['PayoutRatio'])
print(f"Overall Correlation between Net Margin and Payout Ratio: {correlation:.4f}")


X = df['NetMargin']
y = df['PayoutRatio']
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()

print("\n--- Regression Results ---")
print(model.summary())

plt.figure(figsize=(10, 6))
sns.regplot(x='NetMargin', y='PayoutRatio', data=df, 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Impact of Industry Net Margin on S&P 500 Payout Ratios')
plt.xlabel('Industry Net Margin (Aswath Damodaran Benchmark)')
plt.ylabel('Company Payout Ratio (yfinance)')
plt.grid(True, linestyle='--', alpha=0.7)


plt.savefig("analysis/initial_margin_payout_plot.png")
print("\nVisualization saved to analysis/initial_margin_payout_plot.png")
plt.show()