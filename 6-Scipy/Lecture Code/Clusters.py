import numpy
import scipy
import matplotlib.pyplot as plt

from scipy.stats import norm
from numpy import array,vstack
from scipy.cluster.vq import *

data=norm.rvs(0,0.3,size=(10000,2))
inside_ball=numpy.hypot(data[:,0],data[:,1])<1.0
data=data[inside_ball]
data = vstack((data, data+array([1,1]),data+array([-1,1])))


centroids, distortion = kmeans(data,3)
cluster_assignment, distances = vq(data,centroids)

plt.rcParams['figure.figsize'] = (8.0, 6.0)
plt.plot(data[cluster_assignment==0,0], data[cluster_assignment==0,1], 'ro')
plt.plot(data[cluster_assignment==1,0], data[cluster_assignment==1,1], 'b+')
plt.plot(data[cluster_assignment==2,0], data[cluster_assignment==2,1], 'k.')
plt.show()
print('#',50*"-")