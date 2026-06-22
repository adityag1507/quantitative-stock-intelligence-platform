from data_loader import get_stock_data
from indicators import add_sma
from signals import add_signal_column
from backtester import run_backtest

data = get_stock_data("AAPL")

data = add_sma(data)

data = add_signal_column(data)

final_capital = run_backtest(data)

print("Final Capital:", final_capital)
print("Return %:", ((final_capital - 10000) / 10000) * 100)
