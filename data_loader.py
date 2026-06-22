import yfinance as yf

def get_stock_data(ticker, period="1y"):

    data = yf.download(
        ticker,
        period=period
    )

    # Fix MultiIndex columns
    if data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)

    return data
