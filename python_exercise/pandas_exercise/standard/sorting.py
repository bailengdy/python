import pandas as pd

df = pd.DataFrame({
    "symbol":  ["AAPL", "AAPL", "MSFT", "MSFT"],
    "account": ["ACC1", "ACC2", "ACC1", "ACC2"],
    "pnl":     [ 100.0, -50.0,  20.0,  -5.0],
})
print(df)

print(df.sort_values(by=["symbol", "pnl"], ascending=[True, False]))