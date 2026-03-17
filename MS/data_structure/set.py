symbols = ["AAPL", "MSFT", "AAPL", "GOOG", "MSFT"]

unique_symbols = set(symbols)   # 去重 / deduplicate
print(unique_symbols)           # {'AAPL', 'MSFT', 'GOOG'}

# membership check
if "AAPL" in unique_symbols:
    print("We have AAPL")