import pandas as pd

df = pd.read_csv("/Users/yingdai/Desktop/2025/MS/python/trades.csv")
#print(df)

filtered = df[["trade_id", "qty", "strike"]].copy()
#print(filtered)

filtered["notional"] = filtered["qty"] * filtered["strike"]
print(filtered)