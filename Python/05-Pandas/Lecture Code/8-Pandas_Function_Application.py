import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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