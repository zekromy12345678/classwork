import robin_stocks as r
import pandas as pd
import time

def calculate_indicators(df, period_sma, period_ema, overbought, oversold):
    """Calculates the EMA, SMA, and RSI for the given data and periods."""
    # Calculate the SMA
    df["sma"] = df["close_price"].rolling(window=period_sma).mean()
    # Calculate the EMA
    k = 2 / (period_ema + 1)
    df["ema"] = df["close_price"].ewm(span=period_ema, adjust=False).mean()
    # Calculate the RSI
    delta = df['close_price'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(period_ema).mean()
    roll_down = down.abs().rolling(period_ema).mean()
    rs = roll_up / roll_down
    df['rsi'] = 100.0 - (100.0 / (1.0 + rs))
    return df

def place_trade(symbol, trend, price, trade_amount):
    """Places a trade based on the given trend and price."""
    if trend == "up":
        r.orders.order_sell_crypto_by_price(symbol, trade_amount, price)
    elif trend == "down":
        r.orders.order_buy_crypto_by_price(symbol, trade_amount, price)

def run_strategy(symbol, period_sma, period_ema, overbought, oversold, risk_tolerance):
    """Runs the trading strategy on a loop."""
    while True:
        # Get the data for the cryptocurrency
        data = r.stocks.get_crypto(symbol)
        df = pd.DataFrame.from_dict(data)
        # Calculate the EMA, SMA, and RSI
        df = calculate_indicators(df, period_sma, period_ema, overbought, oversold)
        # Calculate the trade amount based on the risk tolerance
        funds = r.fundamentals.get_crypto(symbol)
        total_funds = float(funds['cash']) + float(funds['unsettled_funds'])
        trade_amount = total_funds * risk_tolerance
                # Place the trade if the EMA is trending upwards and the RSI is below the oversold threshold
        if df["ema"][-1] > df["ema"][-2] and df["rsi"][-1] < oversold:
            place_trade(symbol, "up", df["close_price"][-1], trade_amount)
        # Place the trade if the EMA is trending downwards and the RSI is above the overbought threshold
        elif df["ema"][-1] < df["ema"][-2] and df["rsi"][-1] > overbought:
            place_trade(symbol, "down", df["close_price"][-1], trade_amount)
        # Otherwise, do nothing
        else:
            pass
        # Sleep for 60 seconds before checking again
        time.sleep(60)

# Authenticate with the Robinhood API
r.login()
# Run the trading strategy on a loop
run_strategy("BTC", 20, 10, 70, 30, 0.2)

"""In this example, the run_strategy function takes the following parameters:
symbol: the symbol of the cryptocurrency to trade
period_sma: the period for the simple moving average (SMA)
period_ema: the period for the exponential moving average (EMA)
overbought: the overbought threshold for the relative strength index (RSI)
oversold: the oversold threshold for the RSI
risk_tolerance: the risk tolerance of the user, expressed as a percentage of the total funds"""