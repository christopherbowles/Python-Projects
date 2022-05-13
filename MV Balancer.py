import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
from pandas_datareader import data
from pulp import *


assets = ["AAPL", "MSFT","AMZN","GOOGL","FB",'^IXIC']
initial_date = "2020-05-20"
today = datetime.today().strftime('%Y-%m-%d')
df_prices = pd.DataFrame()


def datosYahoo(dataframe,asset_list,start,finish):
    for i in asset_list:
        dataframe[i] = data.DataReader(i,data_source='yahoo',start= start , end=finish)["Adj Close"]
    return dataframe
df = datosYahoo(df_prices,assets,initial_date,today)
df


plt.figure(figsize=(12.2,4.5))
for i in df.columns.values:
    plt.plot( df[i],  label=i)
plt.title('Price of the Stocks')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Price in USD',fontsize=18)
plt.legend(df.columns.values, loc='upper left')
plt.show()

df = np.log(df).diff()
df = df.dropna()
df

plt.figure(figsize=(12.2,4.5))
for i in df.columns.values:
    plt.hist( df[i],  label=i, bins = 200)
plt.title('Returns Histogram')
plt.xlabel('Fecha',fontsize=18)
plt.ylabel('Precio en USD',fontsize=18)
plt.legend(df.columns.values)

retornos1 = expected_returns.capm_return(df_assets, market_prices = df_benchmark1, returns_data= True, risk_free_rate=0.07/100, frequency=252)
retornos1 = expected_returns.capm_return(df_assets, market_prices = df_benchmark1, returns_data= True, risk_free_rate=0.07/100, frequency=252)
def pesosPortafolio(dataframe):
    array = []
    for i in dataframe.columns:
        array.append(1/len(dataframe.columns))
    arrayFinal = np.array(array)
    return arrayFinal
# Pesos are the resulting weights
pesos = pesosPortafolio(df_activos)

df_assets =  df.loc[:, df.columns != '^IXIC']
df_benchmark1 =  df.loc[:, df.columns == '^IXIC']