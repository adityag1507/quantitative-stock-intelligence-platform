import pandas as pd


def run_backtest(df):

    initial_capital = 10000
    capital = initial_capital
    shares = 0

    trades = 0

    portfolio_values = []
    trade_profits = []

    buy_price = None

    for _, row in df.iterrows():

        signal = row["Signal"]

        if signal == "BUY" and shares == 0:

            buy_price = row["Close"]

            shares = capital / buy_price
            capital = 0

            trades += 1

        elif signal == "SELL" and shares > 0:

            sell_price = row["Close"]

            profit_pct = (
                (sell_price - buy_price)
                / buy_price
            ) * 100

            trade_profits.append(profit_pct)

            capital = shares * sell_price
            shares = 0

            trades += 1

        current_value = capital

        if shares > 0:
            current_value = shares * row["Close"]

        portfolio_values.append(current_value)

    if shares > 0:
        capital = shares * df.iloc[-1]["Close"]

    portfolio_series = pd.Series(
        portfolio_values
    )

    returns = (
        portfolio_series
        .pct_change()
        .dropna()
    )

    return {
        "initial_capital": initial_capital,
        "final_capital": capital,
        "return_pct": (
            (capital - initial_capital)
            / initial_capital
        ) * 100,
        "trades": trades,
        "portfolio_values": portfolio_series,
        "returns": returns,
        "trade_profits": trade_profits
    }
