import numpy as np 
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime 
import matplotlib.pyplot as plt 
import seaborn 

start = datetime(2021, 1, 1)
ticker_list = ['AAPL', 'GME', 'BB', 'NVDA', 'GOOGL']

#store prices 
symbols = []

for ticker in ticker_list:
  r = pdr.DataReader(ticker, 'yahoo', start)
  #column for symbol
  r['Symbol'] = ticker
  symbols.append(r)

#concat into dataframe
df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
df.head()
df_pivot=df.pivot('Date', 'Symbol', 'Close').reset_index() 
df_pivot.head() 


corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
#del corr_df.index.name
corr_df.head(10)

plt.figure(figsize=(13, 8))
seaborn.heatmap(corr_df, annot=True, cmap='RdYlGn')
plt.figure()