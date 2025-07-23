import time
from analysis import analyze_market
from bot import send_signal

pairs = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "USDCHF=X", "NZDUSD=X", "USDCAD=X"]

while True:
    for symbol in pairs:
        result = analyze_market(symbol)
        send_signal(result)
    time.sleep(30)
