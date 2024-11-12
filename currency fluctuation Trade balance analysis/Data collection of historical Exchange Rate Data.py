# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:22:00 2024

@author: aksha
"""

#pip install yfinance to install the yfinance library

import yfinance as yf

# Euro and USD has been defined as the currency pair
currency_pair = "EURUSD=X"

# Downloading the historical data 
data = yf.download(currency_pair, start="2019-01-01", end="2024-01-01", interval='1mo')

# Displaying the data
print(data.head())

# Saving data to CSV
data.to_csv('currency_data_monthly.csv')
