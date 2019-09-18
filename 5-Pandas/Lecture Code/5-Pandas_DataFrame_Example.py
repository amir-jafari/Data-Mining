import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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