import numpy
import scipy
import matplotlib.pyplot as plt

from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sigma=10.0
b=8.0/3.0
r=28.0
f = lambda x,t: [sigma*(x[1]-x[0]),
                 r*x[0]-x[1]-x[0]*x[2],
                 x[0]*x[1]-b*x[2]]

t=linspace(0,20,2000); y0=[5.0,5.0,5.0]
solution=odeint(f,y0,t)
X=solution[:,0]; Y=solution[:,1]; Z=solution[:,2]

import matplotlib.pyplot as plt
plt.gca(projection='3d'); plt.plot(X,Y,Z)
plt.show()
print('#',50*"-")