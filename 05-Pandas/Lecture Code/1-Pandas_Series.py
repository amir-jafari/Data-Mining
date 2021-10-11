import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s1 = pd.Series(); print(s1)

data = np.array(['a','b','c','d'])
s2 = pd.Series(data)
print(s2)

s3 = pd.Series(data, index=[3,2,1,0])
print(s3)

data = {'0' : 'a', '1' : 'b', '2' : 'c', '3': 'd'}
s4 = pd.Series(data)
print(s4)

s5 = pd.Series(data,index=['a','b','c','d'])
print(s5)

s6 = pd.Series(0, index=[0, 1, 2, 3])
print(s6)

s7 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s7[3]) ;print (s7[3:]);print (s7[:3])
print('#',50*"-")