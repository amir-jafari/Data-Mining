import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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