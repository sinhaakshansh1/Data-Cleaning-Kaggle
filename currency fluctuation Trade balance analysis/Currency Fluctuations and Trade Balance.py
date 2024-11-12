# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:11:18 2024

@author: aksha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from datetime import datetime
#importing Datasets
trade_balance_data = pd.read_csv("C:/Users/aksha/Downloads/TradeData_DU_USA.csv")
currency_fluctuations_data = pd.read_csv("C:/Users/aksha/Downloads/currency_data_monthly.csv")
pd.set_option('display.float_format', '{:.2f}'.format)
print(trade_balance_data.head())
print(currency_fluctuations_data.head())

#Converting refPeriodId to date time in Trade balance dataset
trade_balance_data['refPeriodId'] = pd.to_datetime(trade_balance_data['refPeriodId'], format='%Y%m%d')
#print(trade_balance_data['refPeriodId'])

#Converting refPeriodId to date time in Currency exchange dataset
currency_fluctuations_data['Date'] = pd.to_datetime(currency_fluctuations_data['Date']).dt.strftime('%Y-%m-%d')
#print(currency_fluctuations_data['Date'])

#Replacing missing values 
trade_balance_data.ffill(inplace=True)
currency_fluctuations_data.ffill(inplace=True)

#adding new column refYear in Currency exchange dataset to join it with Trade Data dataset
currency_fluctuations_data['Date'] = pd.to_datetime(currency_fluctuations_data['Date'], errors='coerce')

currency_fluctuations_data['refYear'] = currency_fluctuations_data['Date'].dt.year
#print(currency_fluctuations_data['refYear'])

#Merging both data sets on refYear column
merged_data = pd.merge(trade_balance_data, currency_fluctuations_data, on='refYear')
#print(merged_data.head())

# creating differnt Import and Export column for respective values
merged_data['primaryValue'] = merged_data['primaryValue'].round(4)
merged_data['Imports'] = merged_data.apply(lambda x: x['primaryValue'] if x['flowDesc'] == 'Import' else 0, axis=1)
merged_data['Exports'] = merged_data.apply(lambda x: x['primaryValue'] if x['flowDesc'] == 'Export' else 0, axis=1)
merged_data['Imports'] = merged_data['Imports'].round(4)
merged_data['Exports'] = merged_data['Exports'].round(4)
'''print(merged_data['Import'])
print(merged_data['Export'])'''

merged_data['TradeBalance'] = merged_data['Exports'] - merged_data['Imports']
print(merged_data['TradeBalance'])

merged_data.to_csv('merged_data.csv', index=False)


#visualizing the data

plt.figure(figsize=(14, 7))

#Displaying Trade Balance Over Time
plt.plot(merged_data['refPeriodId'], merged_data['TradeBalance'], label='Trade Balance', color='blue')
plt.title('Trade Balance Over Time')

plt.xlabel('refPeriodId')
plt.ylabel('Trade Balance')
plt.legend()
plt.show()

correlation_matrix = merged_data[['TradeBalance', 'Exports', 'Imports', 'Adj Close']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

X = merged_data[['Adj Close', 'Imports', 'Exports']]
y = merged_data['TradeBalance']

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression results
print(model.summary())

# Visualization of regression results
plt.figure(figsize=(14, 7))
plt.scatter(merged_data['Adj Close'], merged_data['TradeBalance'], color='blue', label='Data points')
plt.plot(merged_data['Adj Close'], model.predict(X), color='red', label='Regression line')
plt.title('Trade Balance vs. Exchange Rate')
plt.xlabel('Exchange Rate')
plt.ylabel('Trade Balance')
plt.legend()
plt.show()

# Reporting
# Save the analysis results to a CSV file
summary_df = pd.DataFrame({
    'Date': merged_data['refPeriodId'],
    'TradeBalance': merged_data['TradeBalance'],
    'ExchangeRate': merged_data['Adj Close'],
    'Exports': merged_data['Exports'],
    'Imports': merged_data['Imports']
})

summary_df.to_csv('trade_analysis_summary.csv', index=False)
print("Analysis summary saved to 'trade_analysis_summary.csv'")