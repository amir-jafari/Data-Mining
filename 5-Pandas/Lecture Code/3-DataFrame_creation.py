import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.DataFrame()
print (df1)

data = [1,2,3,4,5]
df2 = pd.DataFrame(data)
print (df2)

data = [['apples',10],['orange',20],['Bananas',30]]
df3 = pd.DataFrame(data,columns=['Name','Count'], dtype=float)
print(df3)

data = {'Name':['apples', 'orange', 'Bananas'],'Count':[10, 20, 30]}
df4 = pd.DataFrame(data)
df5 = pd.DataFrame(data, index=['In1','In2','In3'])
print(df4)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df6 = pd.DataFrame(data, index=['first', 'second'])
df7 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df8 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'bb'])
print(df6); print(df7); print(df8)
print('#',50*"-")