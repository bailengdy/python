import numpy as np
import matplotlib.pyplot as plt

# Strike prices
K = np.linspace(80, 120, 100)

# 构造两种常见波动率曲线
vol_smile = 0.15 + 0.0008 * (K - 100) ** 2               # 对称微笑（外汇市场常见）
vol_skew = 0.15 + 0.0006 * (K - 100) ** 2 + 0.0008 * (K - 100)  # 左偏微笑（股票市场常见）

plt.figure(figsize=(8,5))
plt.plot(K, vol_smile, label="FX-style Smile (Symmetric)", color='blue')
plt.plot(K, vol_skew, label="Equity-style Skew (Left-leaning)", color='red')
plt.xlabel("Strike Price (K)")
plt.ylabel("Implied Volatility")
plt.title("Volatility Smile and Skew")
plt.legend()
plt.grid(True)
plt.show()