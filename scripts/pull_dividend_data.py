import time
from io import StringIO

import pandas as pd
import requests
import yfinance as yf

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

sp500_table = pd.read_html(StringIO(response.text))[0]

tickers = sp500_table["Symbol"].tolist()

tickers = [ticker.replace(".", "-") for ticker in tickers]

print("Number of tickers loaded:", len(tickers))

pd.DataFrame({"Ticker": tickers}).to_csv("data/sp500_tickers.csv", index=False)

rows = []

for ticker_symbol in tickers:
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info

        rows.append({
            "Ticker": ticker_symbol,
            "Company": info.get("shortName"),
            "Industry": info.get("industry"),
            "Sector": info.get("sector"),
            "DividendYield": info.get("dividendYield"),
            "PayoutRatio": info.get("payoutRatio")
        })

        print(f"Done: {ticker_symbol}")
        time.sleep(0.2)

    except Exception as e:
        print(f"Error: {ticker_symbol} - {e}")
        rows.append({
            "Ticker": ticker_symbol,
            "Company": None,
            "Industry": None,
            "Sector": None,
            "DividendYield": None,
            "PayoutRatio": None
        })

result_df = pd.DataFrame(rows)
result_df.to_csv("data/sp500_dividend_data.csv", index=False)

print("Finished!")
print(result_df.head())
print("Rows saved:", len(result_df))