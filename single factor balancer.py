import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
from datetime import date
##import requests_cache figure out how to cache calls within a class
today = date.today()
yf.pdr_override() ## this allows us to skip the yfinance pull and use pdr.get_data_yahoo("MSFT", start="2021-04-1", end=today.strftime("%Y-%m-%d"))


class Stock:
    def __init__(self, start_date, ticker):
        self.ticker = ticker.upper() ##input("enter a ticker").upper() use this later to make input interactive
        self.start_date = start_date
        self.end_date = today.strftime("%Y-%m-%d") # self.period = period ##input('enter which of the following ranges to consider 1d, 5d, 1mo, 1y, 2y, 5y') use later to make interactive
        self.df = pdr.get_data_yahoo(self.ticker, start = self.start_date, end = self.end_date)
        self.df['Adj_Daily_Change'] = self.df['Adj Close'].pct_change()
        self.df['Raw_Daily_Change'] = self.df['Close'].pct_change()
        self.EWMA_adc = self.df['Adj_Daily_Change'].ewm(span=2, adjust = False).mean() #EWMA_adc => exponential weighted average of adjusted daily change
        self.df['Daily EWMA'] = self.df['Adj_Daily_Change'].ewm(span=2, adjust = False).mean()



MSFT = Stock("2021-05-01", 'msft')
print(MSFT.df.shape)
print(MSFT.df.head())œ
print(MSFT.df['Adj_Daily_Change'])
print(MSFT.EWMA_adc)

startdate = "2021-05-01"
enddate = today.strftime("%Y-%m-%d")

portfolio = pd.DataFrame()
def BuildPortfolio():
    SPX = Stock(startdate, '^SPX')

    for i in list_of_stocks:
        portfolio[i] = Stock(startdate, i).df['Adj_Daily_Change']



list_of_stocks = ['goog', 'msft', 'ccj']

BuildPortfolio()
print(portfolio.shape)
print(portfolio.head())



