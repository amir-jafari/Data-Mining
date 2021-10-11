import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(5, 4),
index = ['a','b','c','d','e'], columns = ['A', 'B', 'C', 'D'])

print(df.loc[:,'A'])
print(df.loc[:,['A','C']])
print(df.loc[['a','b','f','h'],['A','C']])
print(df.loc['a':'h'])
print(df.loc['a']>=0)
print(df.iloc[:3])
print(df.iloc[:3])
print(df.iloc[1:3, 2:3])
print(df.iloc[[1, 3, 4], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])
print(df.ix[:4])
print(df.ix[:,'A'])
print(df[['A','B']])
print(df.A)
print('#',50*"-")