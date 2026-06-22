from ta.momentum import RSIIndicator
from ta.trend import MACD
import pandas as pd

def add_rsi(df):

    rsi = RSIIndicator(
        close=df["Close"]
    )

    df["RSI"] = rsi.rsi()

    return df

def add_macd(df):

    macd = MACD(
        close=df["Close"]
    )

    df["MACD"] = macd.macd()

    df["MACD_SIGNAL"] = macd.macd_signal()

    return df

def add_sma(df):

    df["SMA20"] = (
        df["Close"]
        .rolling(20)
        .mean()
    )

    df["SMA50"] = (
        df["Close"]
        .rolling(50)
        .mean()
    )

    return df
