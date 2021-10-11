import numpy as np
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print(a)
b += a
print(b)
# print(a += b)
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a+b; print(c)
print(c.dtype.name)
d = np.exp(c*1j); print(d)
print(d.dtype.name)
print('#',50*"-")