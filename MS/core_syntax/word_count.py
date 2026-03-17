words = ["AAPL", "MSFT", "AAPL", "GOOG", "MSFT", "AAPL"]

freq = {}

for w in words:
    # get current count, default 0 if not exists
    freq[w] = freq.get(w, 0) + 1

print(freq)  # {'AAPL': 3, 'MSFT': 2, 'GOOG': 1}