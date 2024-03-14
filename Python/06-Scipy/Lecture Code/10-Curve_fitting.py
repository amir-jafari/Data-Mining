import numpy
import scipy
import matplotlib.pyplot as plt
A=18; w=3*numpy.pi; h=0.5
x=numpy.linspace(0,1,100); y=A*numpy.sin(w*x+h)

yc=None
yc=numpy.copy(y)
yc += 4*((0.5-numpy.random.rand(100))*numpy.exp(2*numpy.random.rand(100)**2)) # contamined data

p0=None
p0 = [20, 2*scipy.pi, 1]
target_function = lambda x,AA,ww,hh: AA*numpy.sin(ww*x+hh)
import scipy.optimize
pF=None
pVar = None
pF,pVar = scipy.optimize.curve_fit(target_function, x, yc, p0)
print(pF)
yFit=None
yFit=target_function(x,*pF)
plot2, = plt.plot(x, yc, 'r+', label="Contamined Data")
plot3, = plt.plot(x, yFit,'k', label="Fit of contamined Data")
plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
print('#',50*"-")