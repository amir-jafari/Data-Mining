import numpy as np
x = np.arange(5)
print(x[:,np.newaxis])
print(x[np.newaxis,:])
print(x[:,np.newaxis] + x[np.newaxis,:])
z = np.arange(81).reshape(3,3,3,3)
print(z[1,...,2])
print(z[1,:,:,2])
x = np.arange(10)
x[2:7] = 1
x[2:7] = np.arange(5)
x = np.arange(0, 50, 10)
x[np.array([1, 1, 3, 1])] += 1
print(x)
print('#',50*"-")