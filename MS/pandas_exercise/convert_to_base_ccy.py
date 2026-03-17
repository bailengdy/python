def convert_to_base_ccy(amount, fx_rate):
    return amount * fx_rate

eur_notional = 1_000_000
eur_usd_rate = 1.08
usd_notional = convert_to_base_ccy(eur_notional, eur_usd_rate)
print(usd_notional)