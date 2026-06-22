def run_backtest(df):

    capital = 10000
    shares = 0

    for _, row in df.iterrows():

        signal = row["Signal"]

        if signal == "BUY" and shares == 0:

            shares = capital / row["Close"]
            capital = 0

        elif signal == "SELL" and shares > 0:

            capital = shares * row["Close"]
            shares = 0

    if shares > 0:
        capital = shares * df.iloc[-1]["Close"]

    return capital
