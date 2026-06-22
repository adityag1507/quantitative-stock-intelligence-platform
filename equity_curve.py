import matplotlib.pyplot as plt
from data_loader import get_stock_data
from indicators import add_sma
from indicators import add_rsi
from indicators import add_macd
from signals import add_signal_column
from backtester import run_backtest

data = get_stock_data("AAPL")

data = add_sma(data)
data = add_rsi(data)
data = add_macd(data)

data = add_signal_column(data)

results = run_backtest(data)

plt.figure(figsize=(12, 6))

plt.plot(results["portfolio_values"])

plt.title("Portfolio Growth During Backtest")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value")
plt.grid(True)

plt.savefig("equity_curve.png")

print("Chart Saved!")
