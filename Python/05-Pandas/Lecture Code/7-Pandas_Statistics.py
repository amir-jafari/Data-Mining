import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = {'Name':pd.Series(['a','b','c','d']),
     'Age':pd.Series([10,15,20,30]),
     'Rating':pd.Series([4,3,2,1])}


df = pd.DataFrame(d)
print(df)
print(df.sum())
print(df.sum(1))

print(df.mean())
print(df.std())
print(df.count())
print(df.min())
print(df.median())
print(df.mode())
print(df.cumsum())
print (df.describe(include='all'))
print('#',50*"-")