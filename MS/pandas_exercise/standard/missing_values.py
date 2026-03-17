import pandas as pd

df = pd.DataFrame({
    "symbol": ["AAPL", "MSFT", "GOOG"],
    "price":  [150.0, None, 2800.0],
})
print(df)

nan_rows = df[df["price"].isna()]
print(nan_rows)

df_copy = df.copy()
df_copy["price"] = df_copy["price"].fillna(0.0)
print(df_copy)

df = df.dropna(subset=["price"])
print(df)