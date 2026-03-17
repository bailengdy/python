import pandas as pd

data = {
    "symbol": ["AAPL", "AAPL", "MSFT", "AAPL", "MSFT"],
    "qty":    [100,   50,    80,    70,    40],
    "price":  [150,   152,   300,   151,   305],
}
df = pd.DataFrame(data)
#print(df)
df["notional"] = df["price"] * df["qty"]
print(df)

result = df.groupby(["symbol"]).agg(total_price=("price", "sum"), total_notional=("notional", "sum"))
print(result)
result = result.reset_index()
print(result)