import pandas as pd

from quant_engine.risk.risk_metrics import (
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

portfolio = pd.Series(
    [10000, 10100, 9900, 10300, 10500, 11000]
)

returns = portfolio.pct_change().dropna()

print(
    "Sharpe:",
    round(
        calculate_sharpe_ratio(returns),
        2
    )
)

print(
"Markdown:",
    round(
        calculate_max_drawdown(portfolio),
        4
    )
)

