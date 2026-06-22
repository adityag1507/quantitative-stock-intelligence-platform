def sma_signal(df):

    latest = df.iloc[-1]

    if latest["SMA20"] > latest["SMA50"]:
        return "BUY"

    elif latest["SMA20"] < latest["SMA50"]:
        return "SELL"

    return "HOLD"
