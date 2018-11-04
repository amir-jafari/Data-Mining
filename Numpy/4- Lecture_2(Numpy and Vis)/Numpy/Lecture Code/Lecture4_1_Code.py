import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(b)
print(type(b))
print('#',50*"-")
# -----------------------
a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
#a = np.array(1,2,3,4) # WRONG
a = np.array([1,2,3,4])
b = np.array([(1.5,2,3), (4,5,6)])
print(b)
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)
print(np.zeros( (3,4) ))
print(np.ones( (2,3,4), dtype=np.int16 ))
print(np.empty( (2,3) ))
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ) )
from numpy import pi
x = np.linspace( 0, 2*pi, 100 )
f = np.sin(x)
print(f)
print('#',50*"-")
# -----------------------
a = np.arange(6) # 1d array
print(a)
b = np.arange(12).reshape(4,3) # 2d array
print(b)
c = np.arange(24).reshape(2,3,4) # 3d array
print(c)
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))
print('#',50*"-")
# -----------------------
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print(A*B)
print(A.dot(B))
print(np.dot(A, B))
print('#',50*"-")
# -----------------------
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
# -----------------------
a = np.random.random((2,3))
print(a)
print(a.sum())
print(a.min())
print(a.max())
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0)) # sum of each column
print(b.min(axis=1)) # min of each row
print(b.cumsum(axis=1)) # cumulative sum along each row
print('#',50*"-")
# -----------------------
B = np.arange(3)
print(B)
z = np.exp(B); print(z)
z1 = np.sqrt(B); print(z1)
C = np.array([2., -1., 4.])
z2 = np.add(B, C)
print(z2)
print('#',50*"-")
# -----------------------
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
# -----------------------
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)
print(a.ravel())
a.shape = (6, 2)
print(a.T)
print(a.resize((2,6)))
print(a.reshape(3,-1))
print('#',50*"-")
# -----------------------
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
# -----------------------
a = np.floor(10*np.random.random((2,12)))
print(a)
z4 = np.hsplit(a,3) # Split a into 3
print(z4)
# Split a after the third and the fourth column
z5 = np.hsplit(a,(3,4))
print(z5)
print('#',50*"-")
# -----------------------
a = np.arange(12)
b = a
print(b is a)
c = a.view()
print(c is a)
d = a.copy()
print(d is a)
print('#',50*"-")
# -----------------------


























