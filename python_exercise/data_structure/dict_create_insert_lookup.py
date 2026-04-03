positions = {
    "AAPL": 100,
    "MSFT": 50,
}

# 查询 / lookup: average O(1)
print(positions["AAPL"])    # 100

# 插入 / insert: average O(1)
positions["GOOG"] = 80

# membership test: average O(1)
if "MSFT" in positions:
    print("We have MSFT")

#