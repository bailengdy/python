import pandas as pd

trades = pd.read_csv("/Users/yingdai/Desktop/2025/MS/trades.csv")
r1 = pd.read_csv("/Users/yingdai/Desktop/2025/MS/risk_day1.csv")

agg = r1.groupby(["book","underlying"])[["delta","vega"]].sum()
print(agg)

pivot = r1.pivot_table(index="book", columns="tenor_bucket", values="vega", aggfunc="sum")
print(pivot)

