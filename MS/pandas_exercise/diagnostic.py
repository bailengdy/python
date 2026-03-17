# Simplified Python diagnostic snippet
import math, numpy as np
from scipy.stats import norm

def bs_vega(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*math.sqrt(T))
    return S * norm.pdf(d1) * math.sqrt(T)

print(bs_vega(4500, 4500, 0.5, 0.02, 0.20))

# Simple PnL explain consistency check
import pandas as pd
df["pnl_explained"] = (
    df["delta"]*df["dS"] +
    0.5*df["gamma"]*(df["dS"]**2) +
    df["vega"]*df["dVol"] +
    df["theta"]*df["dT"]
)
df["residual"] = df["pnl_actual"] - df["pnl_explained"]
df.query("abs(residual) > 1e-4")