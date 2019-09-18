import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.rand(3, 2))
print(df.pct_change())
s1 = pd.Series(np.random.rand(10))
s2 = pd.Series(np.random.rand(10))
print(s1.cov(s2))

df = pd.DataFrame(np.random.randn(3, 3), columns=['a', 'b', 'c'])
print(df['a'].cov(df['b']))
print(df.cov())

df = pd.DataFrame(np.random.randn(15, 3),
index = pd.date_range('1/1/2019', periods=15),
columns = ['A', 'B', 'C'])

print(df.rolling(window=3).mean())
print('#',50*"-")