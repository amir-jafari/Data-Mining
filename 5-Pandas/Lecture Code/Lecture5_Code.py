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
data = pd.DataFrame({'value':[10, 20, 30, 40],
                     'patient':[1, 1, 1, 2],
                     'disease':['Flu', 'Cancer', 'Infection','Aneurysm']})
print(data)
print(data[['disease', 'value']])
print(data.columns)
print(data.dtypes)
print(data['disease']==data.disease)
print(data.loc[1])
print(data.head())
print(data.tail(3))
print(data.shape)
data['year'] = 2013
print(data)
# data.value[[0,1,3]]=[1,2,3]
print(data)
print('#',50*"-")
# -----------------------
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print (p)

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print(p['Item1'])
print(p.major_xs(1))
print(p.minor_xs(1))
print('#',50*"-")
# -----------------------
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
# -----------------------
def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.rand(2,2),columns=['col1','col2'])
print(df)
df.pipe(adder, 2)
print(df.apply(np.mean))
print(df.apply(np.mean, axis=1))

df['col1'].map(lambda x:x*2)
print(df.apply(np.mean, axis=1))
print('#',50*"-")
# -----------------------
df = pd.DataFrame({
   'A': np.linspace(0,stop=20-1,num=20),
   'B': np.random.rand(20),
   'D': np.random.normal(100, 10, size=(20)).tolist()
                  })
print(df)
df_reindexed = df.reindex(index=[0, 1, 2], columns=['A', 'B', 'C'])
print(df_reindexed)

df1 = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print(df1)
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
       index = {0 : 'apple', 1 : 'banana', 2 : 'orange'}))
print('#',50*"-")
# -----------------------
df = pd.DataFrame({
   'A': np.linspace(0,stop=20-1,num=20),
   'B': np.random.rand(20),
   'D': np.random.normal(100, 10, size=(20)).tolist()
                  })
print(df)
for col in df:
   print(col)

for key,value in df.iteritems():
   print(key,value)

for row_index,row in df.iterrows():
   print (row_index,row)
print('#',50*"-")
# -----------------------
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
# -----------------------
s = pd.Series(['Amir', 'Brian James', 'Luo', '@gmail','1234','AmirJafari'])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print(s.str.strip())
print(s.str.split(' '))
print(s.str.cat(sep='-'))
print(s.str.get_dummies())
print(s.str.contains('@'))
print(s.str.replace('@','-'))
print(s.str.count('m'))
print(s.str. startswith ('A'))
print(s.str.endswith('4'))
print('#',50*"-")
# -----------------------
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
# -----------------------
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
# -----------------------
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
# -----------------------
df13 = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                    'h'],columns=['one', 'two', 'three'])
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
# -----------------------
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
print(df.groupby('Team').groups)
print(df.groupby(['Team','Year']).groups)
grouped = df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)
print(grouped.get_group(2014))
print(grouped['Points'].agg(np.mean))
grouped = df.groupby('Team')
print(grouped.agg(np.size))
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))
print(df.groupby('Team').filter(lambda x: len(x) >= 3))
print('#',50*"-")
# -----------------------
dfl = pd.DataFrame({
         'in':[1,2,3,4],
         'Name': ['Amir', 'Brian', 'James', 'Mike'],
         'id':['id1','id2','id3','id4']})
dfr = pd.DataFrame(
         {'in':[1,2,3,4],
         'Name': ['Li', 'Brian', 'Bran', 'Xu'],
         'id':['id2','id4','id3','id1']})
print(dfl)
print(dfr)
print(pd.merge(dfl,dfr,on='in'))
print(pd.merge(dfl,dfr,on=['in','id']))
print(pd.merge(dfl,dfr,on='id', how='left'))
print(pd.merge(dfl,dfr,on='id', how='right'))
print('#',50*"-")
# -----------------------
dfl = pd.DataFrame({
         'in':[1,2,3,4],
         'Name': ['Amir', 'Brian', 'James', 'Mike'],
         'id':['id1','id2','id3','id4']})
dfr = pd.DataFrame(
         {'in':[1,2,3,4],
         'Name': ['Li', 'Brian', 'Bran', 'Xu'],
         'id':['id2','id4','id3','id1']})
print(pd.concat([dfl,dfr],keys=['x','y']))
print(pd.concat([dfl,dfr],keys=['x','y'],ignore_index=True))
print(pd.concat([dfl,dfr],keys=['x','y'],axis=1))
print(dfl.append(dfr))
print(dfl.append([dfl,dfl,dfr]))

print(pd.Timestamp(1283447255,unit='s'))
print(pd.date_range("12:00", "15:30", freq="30min").time)
print('#',50*"-")
# -----------------------
df = pd.DataFrame(np.random.rand(9,3),index=pd.date_range('1/1/2019',
   periods=9), columns=list('ABC'))
print(df)
df.plot()
plt.show()
df = pd.DataFrame(np.random.rand(9,3),columns=['a','b','c'])
df.plot.bar()
plt.show()
df.plot.barh(stacked=True)
plt.show()
df.plot.hist(bins=20)
plt.show()
df.plot.box()
plt.show()
df.plot.area()
plt.show()
df.plot.scatter(x='a', y='b')
plt.show()
df.plot.pie(subplots=True)
plt.show()
print('#',50*"-")
# -----------------------
mb = pd.read_csv("microbiome.csv")
print(mb)
print(mb.head())
mb = pd.read_csv("microbiome.csv", header=None)
print(mb.head())
mb = pd.read_table("microbiome.csv", sep=',')
print(mb.head())
mb = pd.read_csv("microbiome.csv", index_col=['Patient','Taxon'])
print(mb.head())
pd.read_csv("microbiome.csv", nrows=4)
print(mb.head())
pd.read_csv("microbiome.csv").head(20)
print(mb.head())
print('#',50*"-")
# -----------------------

