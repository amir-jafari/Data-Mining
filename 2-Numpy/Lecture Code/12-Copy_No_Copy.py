import numpy as np
a = np.arange(12)
b = a
print(b is a)
c = a.view()
print(c is a)
d = a.copy()
print(d is a)
print('#',50*"-")