import numpy as np
y = np.arange(35).reshape(5,7)
print(y[np.array([0,2,4]), np.array([0,1,2])])
#print(y[np.array([0,2,4]), np.array([0,1])])
print(y[np.array([0,2,4]), 1]) # broadcasting
print(y[np.array([0,2,4])])
print('#',50*"-")