class Trade:
    DEFAULT_CURRENCY = "USD"  # 类属性 / class attribute
    def __init__(self, symbol, qty, price, side, currency=None):
        self.symbol = symbol
        self.qty = qty
        self.price = price
        self.side = side  # "BUY" or "SELL"
        self.currency = currency or Trade.DEFAULT_CURRENCY

    def pnl(self, current_price):
        if self.side == "BUY":
            return (current_price - self.price) * self.qty
        else:  # SELL
            return (self.price - current_price) * self.qty

    def describe(self):
        return f"{self.qty} shares of {self.symbol}"

t = Trade("AAPL", 100, 150.0, "BUY")
print(t.pnl(155.0))   # (155 - 150) * 100 = 500
print(t.describe())