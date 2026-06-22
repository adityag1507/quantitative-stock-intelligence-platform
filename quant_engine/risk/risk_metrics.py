import numpy as np


def calculate_sharpe_ratio(returns, risk_free_rate=0.02):

    if len(returns) == 0:
        return 0

    excess_returns = returns - (risk_free_rate / 252)

    return np.sqrt(252) * (
        excess_returns.mean() /
        excess_returns.std()
    )


def calculate_max_drawdown(portfolio_values):

    peak = portfolio_values.cummax()

    drawdown = (
        portfolio_values - peak
    ) / peak

    return drawdown.min()


def calculate_win_rate(trades):

    if len(trades) == 0:
        return 0

    wins = len(
        [t for t in trades if t > 0]
    )

    return (
        wins / len(trades)
    ) * 100
