import pandas as pd

def create_ticker_batches(df, group_col="TICKER", date_col="date", batch_days=5):
    """
    Splits data into 5-day batches for each ticker.
    
    Returns: List of dicts with keys: 'ticker', 'data'
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    batches = []

    for ticker, group in df.groupby(group_col):
        group = group.sort_values(date_col)
        unique_dates = group[date_col].unique()

        for i in range(0, len(unique_dates), batch_days):
            batch_dates = unique_dates[i:i+batch_days]
            batch = group[group[date_col].isin(batch_dates)]

            if not batch.empty:
                batches.append({
                    "ticker": ticker,
                    "data": batch.reset_index(drop=True)
                })

    return batches


# +
import yfinance as yf

def fetch_latest_price(ticker="AAPL", interval="1m", lookback="1d"):
    """
    Fetches recent price data for a given ticker.
    Returns a DataFrame with timestamps as index.
    """
    df = yf.download(ticker, period=lookback, interval=interval, progress=False)
    return df

