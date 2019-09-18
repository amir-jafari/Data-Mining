import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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