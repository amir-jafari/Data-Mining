import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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