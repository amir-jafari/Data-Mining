import numpy
import scipy
import matplotlib.pyplot as plt
import scipy.interpolate
x=scipy.linspace(-1,1,10)
xn=scipy.linspace(-1,1,1000)
y=scipy.sin(x)
polynomial=scipy.interpolate.lagrange(x, scipy.sin(x))
plt.plot(xn,polynomial(xn),x,y,'or')
plt.show()

x=numpy.array([0,0,1,1,2,2])
y=numpy.array([0,0,1,0,2,0])
interp=scipy.interpolate.KroghInterpolator(x,y)
xn=numpy.linspace(0,2,20)
plt.plot(x,y,'o',xn,interp(xn),'r')
plt.show()
print('#',50*"-")