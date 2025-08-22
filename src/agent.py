import requests, yaml, os, schedule, time
from datetime import datetime
import pytz
from alerts import send_telegram

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def fetch_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url)
    return float(r.json()["price"])

def generate_signal(symbol, price, thresholds):
    if price < thresholds["buy_below"]:
        return f"BUY {symbol} at {price}"
    elif price > thresholds["sell_above"]:
        return f"SELL {symbol} at {price}"
    else:
        return f"HOLD {symbol} at {price}"

def run_once():
    cfg = load_config()
    signals = []
    for c in cfg["coins"]:
        price = fetch_price(c["pair"])
        signal = generate_signal(c["pair"], price, c["thresholds"])
        signals.append(signal)
    msg = "\n".join(signals)
    send_telegram(msg)

if __name__ == "__main__":
    tz = pytz.timezone("Africa/Lagos")
    schedule.every().day.at("08:00").do(run_once)
    while True:
        schedule.run_pending()
        time.sleep(60)
