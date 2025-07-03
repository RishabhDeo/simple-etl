import requests
import pandas as pd
import time
from datetime import datetime

API_KEY = 'demo'  # Replace with your Alpha Vantage API key
BASE_URL = 'https://www.alphavantage.co/query'

def fetch_daily_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print(f"Failed to retrieve data for {symbol}: {data.get('Note') or data.get('Error Message')}")
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index', dtype='float')
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.rename(columns=lambda x: x.split('. ')[-1].capitalize(), inplace=True)

    df['Return'] = df['Close'].pct_change()
    df['MA_7'] = df['Close'].rolling(7).mean()
    df['MA_30'] = df['Close'].rolling(30).mean()

    return df

if __name__ == "__main__":
    from scripts.load_to_postgres import load_to_postgres
    
    symbols = ['IBM', 'MSFT']
    
    for symbol in symbols:
        print(f"\nFetching: {symbol}")
        df = fetch_daily_stock_data(symbol)
        load_to_postgres(df, symbol)

