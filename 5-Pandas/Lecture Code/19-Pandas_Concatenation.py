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
print(pd.concat([dfl,dfr],keys=['x','y']))
print(pd.concat([dfl,dfr],keys=['x','y'],ignore_index=True))
print(pd.concat([dfl,dfr],keys=['x','y'],axis=1))
print(dfl.append(dfr))
print(dfl.append([dfl,dfl,dfr]))

print(pd.Timestamp(1283447255,unit='s'))
print(pd.date_range("12:00", "15:30", freq="30min").time)
print('#',50*"-")