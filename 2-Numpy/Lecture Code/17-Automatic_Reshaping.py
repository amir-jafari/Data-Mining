import numpy as np
a = np.arange(30)
a.shape = 2,-1,5 # -1 means "whatever size"
print(a.shape)
print(a)
a.shape = 6,5
print(a.shape)
print(a)
x = np.arange(0,10,2)
y = np.arange(5)
m = np.vstack([x,y])
n = np.hstack([x,y])
print(m)
print(n)
print('#',50*"-")