from data_loader import get_stock_data
from indicators import add_sma, add_rsi, add_macd

data = get_stock_data("AAPL")

data = add_sma(data)
data = add_rsi(data)
data = add_macd(data)

print(
    data[
        [
            "Close",
            "SMA20",
            "SMA50",
            "RSI",
            "MACD",
            "MACD_SIGNAL"
        ]
    ].tail()
)
