import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr



class Stock:
    def __init__(self, start_date, end_date, ticker):
        self.ticker = yf.Ticker(ticker)   ##input("enter a ticker").upper() use this later to make input interactive
        self.start_date = start_date
        self.end_date = end_date
        self.data = pdr.Series
       # self.period = period ##input('enter which of the following ranges to consider 1d, 5d, 1mo, 1y, 2y, 5y') use later to make interactive
    def EWMA(self):
        pass
    def SMA(self):

class Portfolio:
    pass




Stock
