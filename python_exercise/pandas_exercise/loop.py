import pandas as pd

trades = pd.read_csv("/Users/yingdai/Desktop/2025/MS/python/trades_v2.csv", converters={"notional": lambda x: int(str(x))})

for _, trade in trades.iterrows():
    if float(trade["notional"]) >= 500000:
        print("large trade:", trade["trade_id"])
    else:
        print("small trade")