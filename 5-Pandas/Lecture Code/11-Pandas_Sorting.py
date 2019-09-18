import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.DataFrame(np.random.rand(3, 2), index=[1,6,4],columns=['col2', 'col1'])
print(df1)

df2 = df1.sort_index()
df3 = df1.sort_index(ascending=False)
df4 = df1.sort_index(axis=1)
df5 = df1.sort_values(by='col1')
df5 = df1.sort_values(by=['col1', 'col2'])
df6 = df1.sort_values(by='col1', kind='mergesort')

print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print('#',50*"-")