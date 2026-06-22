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

print("\nBACKTEST RESULTS\n")

print("Initial Capital:", results["initial_capital"])
print("Final Capital:", round(results["final_capital"], 2))
print("Return %:", round(results["return_pct"], 2))
print("Trades:", results["trades"])
