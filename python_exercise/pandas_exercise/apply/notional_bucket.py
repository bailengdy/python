import pandas as pd

df = pd.read_csv("/Users/yingdai/Desktop/2025/MS/python/trades.csv")
#print(df)

filtered = df[["trade_id", "notional"]].copy()
#print(filtered)

def size_bucket(x):
    if x < 100_000:
        return "small"
    elif x < 1_000_000:
        return "medium"
    else:
        return "large"

filtered["bucket"] = filtered["notional"].apply(size_bucket)
print(filtered)