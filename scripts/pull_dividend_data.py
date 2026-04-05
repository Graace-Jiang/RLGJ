import pandas as pd
import yfinance as yf
import time

# 读取 ticker 列表
tickers_df = pd.read_csv("data/sp500_tickers.csv")
tickers = tickers_df["Ticker"].dropna().astype(str).tolist()

rows = []

for ticker_symbol in tickers:
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info

        rows.append({
            "Ticker": ticker_symbol,
            "Industry": info.get("industry"),
            "Sector": info.get("sector"),
            "DividendYield": info.get("dividendYield"),
            "PayoutRatio": info.get("payoutRatio")
        })

        print(f"Done: {ticker_symbol}")
        time.sleep(1)

    except Exception as e:
        print(f"Error: {ticker_symbol} - {e}")
        rows.append({
            "Ticker": ticker_symbol,
            "Industry": None,
            "Sector": None,
            "DividendYield": None,
            "PayoutRatio": None
        })

# 保存结果
result_df = pd.DataFrame(rows)
result_df.to_csv("data/sp500_dividend_data.csv", index=False)

print("Finished!")
print(result_df.head())