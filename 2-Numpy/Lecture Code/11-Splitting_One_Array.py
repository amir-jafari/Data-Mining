import numpy as np
a = np.floor(10*np.random.random((2,12)))
print(a)
z4 = np.hsplit(a,3) # Split a into 3
print(z4)
# Split a after the third and the fourth column
z5 = np.hsplit(a,(3,4))
print(z5)
print('#',50*"-")