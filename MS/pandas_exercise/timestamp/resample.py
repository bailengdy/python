import pandas as pd

data = {
    "timestamp": [
        "2025-11-01 09:30",
        "2025-11-01 09:31",
        "2025-11-01 09:32",
        "2025-11-01 10:00",
    ],
    "price": [100.0, 100.5, 101.0, 102.0],
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)

df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df)
print(df.dtypes)

df = df.set_index("timestamp")
print(df)

hourly = df.resample("1h")["price"].mean()
print(hourly)