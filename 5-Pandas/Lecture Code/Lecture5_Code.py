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
# -----------------------
counts = pd.Series([10, 20, 30, 40])
print(counts)
print(counts.values)
print(counts.index)

stuff = pd.Series([10, 20, 30, 40],
    index=['apple', 'temple', 'maple', 'sample'])

print(stuff)
print(stuff['apple'])
print(stuff[[name.endswith('mple') for name in stuff.index]])
print(stuff[0])

stuff.name = 'MyDataFrame'
stuff.index.name = 'itmes'

print(stuff)
num = np.log10(stuff)
print(num)
print(stuff.isnull())
print('#',50*"-")
# -----------------------
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
# -----------------------
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
# -----------------------

