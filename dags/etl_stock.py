import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="AAPL", period="1mo", interval="1d", progress=False):
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    df.to_csv(f"data/{ticker}_raw.csv", index=True)

if __name__ == "__main__":
    fetch_stock_data()

import yfinance as yf

# Download historical data for a stock (e.g., Apple Inc.)
data = yf.download("RELIANCE.NS", start="2015-01-01", end="2023-12-31")

# Display the first few rows
print(data.head())

# List of Indian stock tickers
tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]  # Reliance, TCS, Infosys

# Download data
data = yf.download(tickers, start="2015-01-01", end="2023-12-31")

# Display the first few rows
print(data.head())

ticker = yf.Ticker("TCS.NS")
current_price = ticker.history(period="1d")['Close'].iloc[-1]
print(f"Current price of TCS: {current_price}")

info = yf.Ticker("TATAMOTORS.NS").info
for key, value in info.items():
    print(f"{key}: {value}")