from data_loader import get_stock_data
from indicators import add_sma
from indicators import add_rsi
from indicators import add_macd

from signals import add_signal_column

from backtester import run_backtest

from quant_engine.risk.risk_metrics import (
    calculate_sharpe_ratio,
    calculate_max_drawdown,
    calculate_win_rate
)

data = get_stock_data("AAPL")

data = add_sma(data)
data = add_rsi(data)
data = add_macd(data)

data = add_signal_column(data)

results = run_backtest(data)

sharpe = calculate_sharpe_ratio(
    results["returns"]
)

max_drawdown = calculate_max_drawdown(
    results["portfolio_values"]
)

win_rate = calculate_win_rate(
    results["trade_profits"]
)

print("\nBACKTEST RESULTS\n")

print("Initial Capital:", results["initial_capital"])
print("Final Capital:", round(results["final_capital"], 2))
print("Return %:", round(results["return_pct"], 2))
print("Trades:", results["trades"])

print("Sharpe Ratio:", round(sharpe, 2))
print("Max Drawdown:", round(max_drawdown * 100, 2), "%")
print("Win Rate:", round(win_rate, 2), "%")
