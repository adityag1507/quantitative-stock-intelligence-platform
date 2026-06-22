import yfinance as yf

def get_stock_data(ticker, period="1y"):
    data = yf.download(
        ticker,
        period=period
    )

    return data


if __name__ == "__main__":
    data = get_stock_data("AAPL")
    print(data.head())

