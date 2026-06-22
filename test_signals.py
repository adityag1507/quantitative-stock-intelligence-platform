from data_loader import get_stock_data
from indicators import add_sma
from signals import sma_signal

data = get_stock_data("AAPL")

data = add_sma(data)

signal = sma_signal(data)

print("Signal:", signal)
