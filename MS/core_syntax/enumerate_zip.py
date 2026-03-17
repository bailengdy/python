prices = [100.0, 101.5, 99.8]

for i, p in enumerate(prices):
    print(i, p)

# 输出:
# 0 100.0
# 1 101.5
# 2 99.8

dates = ["2025-11-01", "2025-11-02", "2025-11-03"]
pnl   = [100.5, -20.0, 35.2]

for d, p in zip(dates, pnl):
    print(f"{d}: PnL = {p}")