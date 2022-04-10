import yfinance as yf
from matplotlib import pyplot as plt
##from matplotlib.ticker import FuncFormatterc
import numpy as np
import pandas as pd
import pandas_datareader as pdr

ticker = yf.Ticker('MSFT')

hist = ticker.history(start='2020-01-01', end='2022-04-01')

hist = hist[['Close']]

hist.plot(figsize=(20, 5))

hist['MA_50'] = hist['Close'].rolling(window=50).mean()

hist['MA_200'] = hist['Close'].rolling(window=200).mean()

hist.plot(figsize=(20, 5))

plt.plot((hist['Close'].ewm(span=26, adjust=False).mean()))
plt.show()
