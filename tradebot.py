import time
import os
import pandas_ta as ta
from alpaca_trade_api.rest import REST, TimeFrame

# --- CONFIGURATION ---
API_KEY = "PUT_YOUR_KEY_HERE"
SECRET_KEY = "PUT_YOUR_SECRET_HERE"
BASE_URL = "https://paper-api.alpaca.markets"

SYMBOL = "SPY"
QTY = 1
SLEEP_SECONDS = 60

# --- INIT ---
api = REST(API_KEY, SECRET_KEY, BASE_URL)

def get_market_data():
    """Fetches the last 50 hours of data to calculate RSI."""
    try:
        # Fetch hourly bars
        bars = api.get_bars(SYMBOL, TimeFrame.Hour, limit=50).df
        # Calculate RSI (14 period)
        bars['RSI'] = bars.ta.rsi(length=14)
        return bars.iloc[-1] # Return the most recent candle
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None

def has_position():
    """Checks if we currently own the stock."""
    try:
        api.get_position(SYMBOL)
        return True
    except:
        return False

def run_bot():
    print(f"🚀 Omega Lite v0.01 Started on {SYMBOL}...")

    while True:
        # 1. Get Data
        data = get_market_data()
        if data is None:
            time.sleep(10)
            continue

        rsi = data['RSI']
        price = data['close']
        timestamp = data.name

        print(f"[{timestamp}] {SYMBOL} Price: ${price:.2f} | RSI: {rsi:.2f}")

        # 2. Logic (The "Dumb" Strategy)
        # Buy if RSI is Low (< 30) AND we don't have it yet
        if rsi < 30:
            if not has_position():
                print(f"🟢 BUY SIGNAL (RSI {rsi:.2f} < 30). Buying {QTY} shares...")
                api.submit_order(SYMBOL, qty=QTY, side='buy', type='market', time_in_force='day')
            else:
                print("⏸  Buy signal ignored (Already holding).")

        # Sell if RSI is High (> 70) AND we have it
        elif rsi > 70:
            if has_position():
                print(f"🔴 SELL SIGNAL (RSI {rsi:.2f} > 70). Selling all...")
                api.close_position(SYMBOL)
            else:
                print("⏸  Sell signal ignored (Nothing to sell).")

        # 3. Sleep
        time.sleep(SLEEP_SECONDS)

if __name__ == "__main__":
    run_bot()
