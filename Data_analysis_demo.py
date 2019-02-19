import quantrautil as q
import numpy as np
from sklearn import tree

aapl = q.get_data('aapl','2000-1-1','2019-1-1')
#print(aapl.tail())
# Features construction 
aapl['Open-Close'] = (aapl.Open - aapl.Close)/aapl.Open
aapl['High-Low'] = (aapl.High - aapl.Low)/aapl.Low
aapl['percent_change'] = aapl['Adj Close'].pct_change()
aapl['std_5'] = aapl['percent_change'].rolling(5).std()
aapl['ret_5'] = aapl['percent_change'].rolling(5).mean()
aapl.dropna(inplace=True)

# X is the input variable
X = aapl[['Open-Close', 'High-Low', 'std_5', 'ret_5']]
print(X)
# Y is the target or output variable
y = np.where(aapl['Adj Close'].shift(-1) > aapl['Adj Close'], 1, -1)
print(y)
