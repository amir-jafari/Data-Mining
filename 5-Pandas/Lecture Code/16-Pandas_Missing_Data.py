import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(15, 3),index = pd.date_range('1/1/2019', periods=15), columns = ['A', 'B', 'C'])

df13 = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
print(df13)
df14 = df13.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df14)
print(df14['one'].isnull())
print(df14['one'].notnull())
print(df14['one'].sum())
print(df14['one'].sum())
print(df.fillna(0))
df15 = df13.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df15.dropna())
df16 = df13.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df16.dropna(axis=1))
print(df.replace({1:0,2:0}))
print('#',50*"-")