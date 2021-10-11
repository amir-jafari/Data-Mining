import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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