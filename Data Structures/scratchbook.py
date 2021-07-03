import pandas as pd
import yfinance as yf

rain = yf.Ticker("RAIN.NS")

hist = rain.earnings
print(hist)
