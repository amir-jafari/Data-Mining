import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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