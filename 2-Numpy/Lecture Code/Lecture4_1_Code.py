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
a= print('#',50*"-")
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
a = np.arange(12)**2
i = np.array( [ 1,1,3,8,5 ] )
print(a[i])
j = np.array( [ [ 3, 4], [ 9, 7 ] ] )
print(a[j])
palette = np.array( [ [0, 0, 0 ],# black
                     [255,0, 0 ],# red
                     [0,255, 0 ], # green
                     [0,0, 255 ], # blue
                    [255,255,255]])# white
image = np.array( [ [ 0, 1, 2, 0 ],
                    [ 0, 3, 4, 0 ] ] )
# each value corresponds to a color in the palette
print(palette[image])
print('#',50*"-")
# -----------------------
a = np.arange(12).reshape(3,4)
print(a)
i = np.array( [ [0,1],[1,2] ] )
j = np.array( [ [2,1],[3,3] ] )
print(a[i,j]); print(a[i,2]); print(a[:,j])
s = np.array( [i,j] ); print(a[tuple(s)])
time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5,4)
ind = data.argmax(axis=0)
time_max = time[ ind]
data_max = data[ind, range(data.shape[1])]
print(np.all(data_max == data.max(axis=0)))
print('#',50*"-")
# -----------------------
a = np.arange(5)
a[[1,3,4]] = 0
print(a)
a[[0,0,2]]+=1
print(a)
print('#',50*"-")
# -----------------------
a = np.arange(12).reshape(3,4)
b = a > 4; print(b)
print(a[b])
a[b] = 0 ; print(a)
a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
print(a[b1,:]); print(a[b1])
print(a[:,b2]); print(a[b1,b2])
print('#',50*"-")
# -----------------------
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
print(ax); print(bx);print(cx)
print(ax.shape, bx.shape, cx.shape)
result = ax+bx*cx
print(result)
print(result[3,2,4])
print(a[3]+b[2]*c[4])
# Automatic Reshaping
a = np.arange(30)
a.shape = 2,-1,3
print(a.shape); print(a)
# Vector Stacking
x = np.arange(0,10,2)
y = np.arange(5)
m = np.vstack([x,y])
xy = np.hstack([x,y])
print(xy)
print('#',50*"-")
# -----------------------
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
# -----------------------
x1 = np.float32(1.0)
x2 = np.int_([1,2,4])
x3 = np.arange(3, dtype=np.uint8)
x4 = np.array([1, 2, 3], dtype='f')
print(x1, x2, x3, x4)
x5 = x3.astype(float)
print(x5)
print(x5.dtype)
x6 = np.dtype(int)
x7 = np.array([2,3,1,0])
x8 = np.array([2, 3, 1, 0])
x9 = np.array([[1,2.0],[0,0],(1+1j,3.)])
print('#',50*"-")
# -----------------------
a1 = np.zeros((2, 3))
a2 = np.arange(10)
print(a1); print(a2)
a3= np.arange(2, 10, dtype=np.float)
a4 = np.arange(2, 3, 0.1)
print(a3); print(a4)
a5 = np.linspace(1., 4., 6)
a6 = np.indices((3,3))
print(a5); print(a6)
print('#',50*"-")
# -----------------------
x = np.arange(10)
print(x[1])
print(x[-2])
x.shape = (2, 5)
print(x[1, 3])
print(x[1,-1])
print(x[0])
print(x[0][2])
print(x[2:5])
print(x[:-7])
print(x[1:7:2])
y = np.arange(35).reshape(5,7)
print(y[1:5:2,::3])
v = np.arange(10,1,-1)
print(v[np.array([3, 3, 1, 8])])
print('#',50*"-")
# -----------------------
y = np.arange(35).reshape(5,7)
print(y[np.array([0,2,4]), np.array([0,1,2])])
#print(y[np.array([0,2,4]), np.array([0,1])])
print(y[np.array([0,2,4]), 1]) # broadcasting
print(y[np.array([0,2,4])])
print('#',50*"-")
# -----------------------
n = np.arange(35)
b = n>20
print(n[b])
x = np.arange(30).reshape(2,3,5)
print(x)
b = np.array([[True, True, False], [False, True, True]])
print(x[b])
print('#',50*"-")
# -----------------------
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
# -----------------------
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
print(a * b)
a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a * b)
x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))
print(x.shape)
print(y.shape)
print(xx.shape)
print(y.shape)
print((xx + y).shape)
print(xx + y)
print((x + z).shape)
print(x + z)






