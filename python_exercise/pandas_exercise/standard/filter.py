import pandas as pd

df = pd.read_csv("/Users/yingdai/Desktop/2025/MS/python/trades.csv")
print(df)

filtered = df[(df["underlying"] == "AAPL") & (df["qty"] > 0)]
print(filtered)

result = filtered[["trade_id", "underlying", "qty"]]
print(result)

print(type(df))
print(df.dtypes)
