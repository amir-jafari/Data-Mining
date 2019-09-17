import numpy as np
a = np.arange(10)**3; print(a)
print(a[2])
print(a[2:5])
a[:6:2] = -1000
print(a[ : :-1])
a = np.arange(10)**3
for i in a:
    print(np.power(i,1/3))
def f(x,y):
    return 10*x+y
b = np.fromfunction(f,(5,4),dtype=int); print(b)
print(b[2,3])
print(b[0:5, 1])
print(b[ : ,1])
print(b[1:3, : ])
print(b[-1])
print('#',50*"-")