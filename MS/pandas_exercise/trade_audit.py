import pandas as pd
import numpy as np
from pathlib import Path

# === 1) 读取文件 ===
input_path = "/Users/yingdai/Desktop/2025/MS/test.xlsx"  # 改成你的路径
df = pd.read_excel(input_path)

# 列名清洗：去空格，保留原大小写方便导出时显示
clean_cols = df.columns.to_series().apply(lambda c: c.strip())
df.columns = clean_cols

# 自动识别 Trade id 列（兼容 'Trade id' / 'Trade ID' / 'trade_id' / 'TradeId' 等）
def is_trade_id(name: str) -> bool:
    key = name.lower().replace("_", "").replace(" ", "")
    return key in {"tradeid", "trade", "trade-id"}  # 你也可以只保留 "tradeid"

trade_cols = [c for c in df.columns if is_trade_id(c)]
if not trade_cols:
    raise ValueError("未找到 Trade id 列，请检查表头。当前列名：%s" % list(df.columns))
trade_col = trade_cols[0]

# === 2) 计算“同一 Trade id 下值不一致”的单元格掩码 ===
non_key_cols = [c for c in df.columns if c != trade_col]

# 对每个非键列：如果同一 Trade id 分组内 nunique > 1，则该列该组的行标记为 True
diff_mask = pd.DataFrame(False, index=df.index, columns=df.columns)
g = df.groupby(trade_col, dropna=False)

for c in non_key_cols:
    # 针对该列，标记“该 Trade id 组内是否存在多个不同值”
    col_group_varies = g[c].transform(lambda s: s.nunique(dropna=False) > 1)
    diff_mask.loc[col_group_varies, c] = True

# Trade id 列本身不高亮
diff_mask[trade_col] = False

# === 3) 用 Styler 高亮并导出 Excel ===
# 需要：pip install Jinja2 openpyxl
def style_func(_):
    # 返回与 df 同形状的样式 DataFrame
    styles = np.where(diff_mask.values, "background-color: yellow", "")
    return pd.DataFrame(styles, index=df.index, columns=df.columns)

styled = df.style.apply(style_func, axis=None)
out_path = Path(input_path).with_name("highlighted_trades.xlsx")
styled.to_excel(out_path, index=False, engine="openpyxl")
print(f"✅ 已生成: {out_path}")