import pandas as pd
from datetime import date

EXCEL_PATH = "/Users/yingdai/Desktop/2025/MS/python/strat_practice_v2.xlsx"
#VALUATION_DATE = "2025-11-10"   # change to try different dates

def bucket_tenor(days):
    if days <= 30:  return "1M"
    if days <= 90:  return "3M"
    if days <= 180: return "6M"
    if days <= 365: return "1Y"
    return "2Y+"

# Load raw (not bucketed) risk
risk = pd.read_excel(EXCEL_PATH, sheet_name="risk_day1_raw", parse_dates=["maturity_date","as_of"])
#val_date = pd.Timestamp(VALUATION_DATE)
val_date = pd.Timestamp(date.today())
risk["days_to_maturity"] = (risk["maturity_date"] - val_date).dt.days
risk["tenor_bucket"] = risk["days_to_maturity"].apply(bucket_tenor)

# 1) Aggregate by book × underlying (Delta/Vega)
agg1 = risk.groupby(["book","underlying"])[["delta","vega"]].sum().reset_index()
#agg1.to_csv("agg_book_underlying.csv", index=False)

# 2) Vega by tenor (pivot)
agg2 = risk.pivot_table(index="underlying", columns="tenor_bucket", values="vega", aggfunc="sum").fillna(0)
#agg2.to_csv("vega_by_tenor.csv")

# 3) Quick printouts
print("== Book × Underlying (Delta/Vega) ==")
print(agg1.head())
print("\n== Vega by Tenor ==")
print(agg2)
print("\nWrote: agg_book_underlying.csv, vega_by_tenor.csv")
