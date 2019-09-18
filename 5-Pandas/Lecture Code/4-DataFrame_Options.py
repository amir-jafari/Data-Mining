import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df9 = { 'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([3, 2, 1], index=['a', 'b', 'c'])}

df9 = pd.DataFrame(df9)
print(df9)
print(df9 ['one'])
df9['three']=pd.Series([-1,-2,-3],index=['a','b','c'])
df9['four']=df9['one']+df9['three']
print(df9)
del(df9['three'])
print(df9)

print(df9.loc['b'])
print(df9.iloc[1])
print(df9[2:3])

df10 = pd.DataFrame([{'one':5, 'two':6,'four':7}],index = ['e'])
df11 = df9.append(df10)
print(df11)
df12 = df11.drop('e')
print(df12)
print('#',50*"-")