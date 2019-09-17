import numpy as np
a = np.floor(10*np.random.random((2,2)));print(a)
b = np.floor(10*np.random.random((2,2)));print(b)
z = np.vstack((a,b)); print(z)
z1 = np.hstack((a,b)); print(z1)
from numpy import newaxis
z2 = np.column_stack((a,b))
a = np.array([4.,2.])
b = np.array([2.,8.])
print(a[:,newaxis])
z3= np.column_stack((a[:,newaxis],b[:,newaxis]))
print(z3)
z4= np.vstack((a[:,newaxis],b[:,newaxis])); print(z4)
print('#',50*"-")