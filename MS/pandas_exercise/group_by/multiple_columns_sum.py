import pandas as pd

data = {
    "date":   ["2025-11-01", "2025-11-01", "2025-11-02", "2025-11-02", ],
    "symbol": ["AAPL",       "MSFT",       "AAPL",       "AAPL"],
    "qty":    [100,          50,           30,           20],
}
df = pd.DataFrame(data)
print(df)

result = df.groupby(["date", "symbol"], as_index=False)["qty"].sum().rename(columns={"qty": "total_qty"})
print(result)