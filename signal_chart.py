import matplotlib.pyplot as plt

from data_loader import get_stock_data
from indicators import add_sma
from indicators import add_rsi
from indicators import add_macd
from signals import add_signal_column

data = get_stock_data("AAPL")

data = add_sma(data)
data = add_rsi(data)
data = add_macd(data)

data = add_signal_column(data)

buy_signals = data[data["Signal"] == "BUY"]
sell_signals = data[data["Signal"] == "SELL"]

plt.figure(figsize=(14,7))

plt.plot(data.index, data["Close"], label="Close Price")

plt.scatter(
    buy_signals.index,
    buy_signals["Close"],
    marker="^",
    s=100,
    label="BUY"
)

plt.scatter(
    sell_signals.index,
    sell_signals["Close"],
    marker="v",
    s=100,
    label="SELL"
)

plt.title("Trading Signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("buy_sell_signals.png")

print("Signal chart saved!")
