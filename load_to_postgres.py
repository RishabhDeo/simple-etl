import os
import pandas as pd
from sqlalchemy import create_engine

# Fetch DB credentials from environment variables
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")  # 👈 This line is what you asked about
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "stocks")

# Create SQLAlchemy engine
db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)


def load_to_postgres(df: pd.DataFrame, symbol: str):
    if df.empty:
        print(f"DataFrame for {symbol} is empty. Skipping load.")
        return

    # Clean column names and add symbol column
    df = df.copy()
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'], utc=True)
    df['symbol'] = symbol

    # Save to Postgres
    try:
        df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)
        print(f"✅ Loaded data for {symbol} into table '{TABLE_NAME}'")
    except Exception as e:
        print(f"❌ Error loading data for {symbol}: {e}")