import numpy as np
import pandas as pd

# Calculate Relative Strength Index (RSI)
def rsi(data, window=14):
    delta = data['Close'].diff()  
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()  
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()  
    rs = gain / loss  
    return 100 - (100 / (1 + rs))

# Calculate Moving Average Convergence Divergence (MACD)
def macd(data, slow=26, fast=12, signal=9):
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()  
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()  
    data['MACD'] = exp1 - exp2  
    data['Signal'] = data['MACD'].ewm(span=signal, adjust=False).mean()  
    return data

# Calculate Stochastic Oscillator

def stochastic_oscillator(data, window=14):
    low_min = data['Low'].rolling(window=window).min()  
    high_max = data['High'].rolling(window=window).max()  
    data['%K'] = 100 * ((data['Close'] - low_min) / (high_max - low_min))  
    data['%D'] = data['%K'].rolling(window=3).mean()  
    return data