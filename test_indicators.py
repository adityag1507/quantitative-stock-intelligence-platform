from data_loader import get_stock_data
from indicators import add_sma

data = get_stock_data("AAPL")

data = add_sma(data)

print(
    data[
        ["Close", "SMA20", "SMA50"]
    ].tail()
)

