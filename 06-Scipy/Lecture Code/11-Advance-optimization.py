import numpy
import scipy
import matplotlib.pyplot as plt

A=18; w=3*numpy.pi; h=0.5

x=None; y=None
x=numpy.linspace(0,1,100); y=A*numpy.sin(w*x+h)
y += 4*((0.5-numpy.random.rand(100))*numpy.exp(2*numpy.random.rand(100)**2))

import scipy.optimize
p0 = [20, 2*numpy.pi, 1]
target_function = lambda x,AA,ww,hh: AA*numpy.sin(ww*x+hh)

#pF,pVar = scipy.optimize.curve_fit(target_function, x, y, p0)
#print (pF)

error_function = lambda p,x,y: target_function(x,p[0],p[1],p[2])-y
lpF,lpVar = scipy.optimize.leastsq(error_function,p0,args=(x,y))
print (lpF)

import scipy.optimize
scipy.optimize.fmin(scipy.optimize.rosen,[0,0])
help(scipy.optimize.minimize)
print('#',50*"-")


f=lambda x: [x[0]**2 - 2*x[0] - x[1] + 0.5, x[0]**2 + 4*x[1]**2 - 4]
x,y=numpy.mgrid[-0.5:2.5:24j,-0.5:2.5:24j]
U,V=f([x,y])
plt.quiver(x,y,U,V,color='r', \
         linewidths=(0.2,), edgecolors=('k'), \
         headaxislength=5)
plt.show()


import scipy.optimize
f=lambda x: [x[0]**2 - 2*x[0] - x[1] + 0.5, x[0]**2 + 4*x[1]**2 - 4]

scipy.optimize.root(f,[0,1])

scipy.optimize.root(f,[2,0])
print('#',50*"-")