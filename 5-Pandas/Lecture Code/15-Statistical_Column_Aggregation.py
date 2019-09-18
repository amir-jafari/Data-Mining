import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(15, 3),
index = pd.date_range('1/1/2019', periods=15),
columns = ['A', 'B', 'C'])

R = df.rolling(window=3,min_periods=1)
print(R)
print(R.aggregate(np.sum))
print(R['A'].aggregate(np.sum))
print(R[['A','B']].aggregate([np.mean,np.std]))
print(R.aggregate({'A' : np.sum,'B' : np.count_nonzero}))
print('#',50*"-")
# ---------------------