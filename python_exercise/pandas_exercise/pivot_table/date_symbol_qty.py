import pandas as pd

data = {
    "date":   ["2025-11-01", "2025-11-01", "2025-11-02", "2025-11-02"],
    "symbol": ["AAPL",       "MSFT",       "AAPL",       "MSFT"],
    "qty":    [100,          50,           80,           70],
}
df = pd.DataFrame(data)
pivot = df.pivot(index="date", columns="symbol", values="qty")
print(pivot)

data = {
    "date":   ["2025-11-01", "2025-11-01", "2025-11-02", "2025-11-02", "2025-11-01", "2025-11-01", "2025-11-02", "2025-11-02"],
    "symbol": ["AAPL","MSFT","AAPL","MSFT","AAPL","MSFT","AAPL","MSFT"],
    "qty":    [100,50,80,70,100,50,80,70],
}
df = pd.DataFrame(data)

pivot = df.pivot_table(index="date", columns="symbol", values="qty", aggfunc="sum", fill_value=0)
print(pivot)