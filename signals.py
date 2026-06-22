def add_signal_column(df):

    df["Signal"] = "HOLD"

    df.loc[
        df["SMA20"] > df["SMA50"],
        "Signal"
    ] = "BUY"

    df.loc[
        df["SMA20"] < df["SMA50"],
        "Signal"
    ] = "SELL"

    return df
