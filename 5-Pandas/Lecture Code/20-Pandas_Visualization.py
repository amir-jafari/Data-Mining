import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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