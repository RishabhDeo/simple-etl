#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import sys

# Install yfinance
subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])


# In[3]:



# In[5]:


import yfinance as yf
print("yfinance installed and ready to use!")


# In[9]:


import yfinance as yf

# Download historical data for a stock (e.g., Apple Inc.)
data = yf.download("RELIANCE.NS", start="2015-01-01", end="2023-12-31")

# Display the first few rows
print(data.head())


# In[11]:


# List of Indian stock tickers
tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]  # Reliance, TCS, Infosys

# Download data
data = yf.download(tickers, start="2015-01-01", end="2023-12-31")

# Display the first few rows
print(data.head())


# In[15]:


# Fetch current price for TCS (NSE)
ticker = yf.Ticker("TCS.NS")
# current_price = ticker.history(period="1d")['Close'].iloc[-1]

hist_data = ticker.history(period="1d")

if not hist_data.empty and 'Close' in hist_data.columns:
    current_price = hist_data['Close'].iloc[-1]
    print("Current Price:", current_price)
else:
    print("No data returned for the specified period.")

print(f"Current price of TCS: {current_price}")


# In[21]:


# Fetch details about the stock
info = yf.Ticker("TATAMOTORS.NS").info
for key, value in info.items():
    print(f"{key}: {value}")


# In[23]:


import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


# In[44]:


# Download stock data for Reliance Industries (NSE)
data = yf.download("TATAMOTORS.NS", start="2023-01-01", end="2024-11-25")

# Feature Engineering: Add Moving Average and Price Change
data['SMA_10'] = data['Close'].rolling(window=10).mean()
data['Price_Change'] = data['Close'].pct_change()

# Target: 1 if price goes up next day, 0 otherwise
data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

# Drop rows with NaN values (e.g., due to rolling mean or shift)
data = data.dropna()

# Features and target variable
features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_10', 'Price_Change']
target = 'Target'

X = data[features]
y = data[target]


# In[46]:


# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[48]:


# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# In[50]:


# Compare Actual vs Predicted for a subset
comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
}, index=y_test.index)

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.plot(comparison.index, comparison["Actual"], label="Actual", alpha=0.7)
plt.plot(comparison.index, comparison["Predicted"], label="Predicted", alpha=0.7)
plt.xlabel("Date")
plt.ylabel("Movement (1=Up, 0=Down)")
plt.legend()
plt.title("Actual vs Predicted Stock Movement")
plt.show()


# In[ ]:





# In[ ]:




