import json

with open("marketdata.json", "r") as f:
    md = json.load(f)

print(md["EURUSD"]["spot"])