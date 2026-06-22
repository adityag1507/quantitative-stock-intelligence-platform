def run_backtest(df):

    initial_capital = 10000
    capital = initial_capital
    shares = 0

    trades = 0

    for _, row in df.iterrows():

        signal = row["Signal"]

        if signal == "BUY" and shares == 0:

            shares = capital / row["Close"]
            capital = 0
            trades += 1

        elif signal == "SELL" and shares > 0:

            capital = shares * row["Close"]
            shares = 0
            trades += 1

    if shares > 0:
        capital = shares * df.iloc[-1]["Close"]

    return {
        "initial_capital": initial_capital,
        "final_capital": capital,
        "return_pct": ((capital - initial_capital) / initial_capital) * 100,
        "trades": trades
    }
