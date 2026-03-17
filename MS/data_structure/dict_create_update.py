def create_order(symbol, qty, **kwargs):
    order = {
        "symbol": symbol,
        "qty": qty,
    }
    # merge extra fields from kwargs
    order.update(kwargs)
    return order

o = create_order("AAPL", 100, side="BUY", price=150.0, tif="DAY")
print(o)
# {'symbol': 'AAPL', 'qty': 100, 'side': 'BUY', 'price': 150.0, 'tif': 'DAY'}

# *args collects extra positional arguments into a tuple,
# **kwargs collects keyword arguments into a dict.