import numpy as np
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