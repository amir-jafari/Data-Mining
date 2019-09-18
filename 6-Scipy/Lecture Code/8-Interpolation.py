import numpy
import scipy
import matplotlib.pyplot as plt

from scipy.linalg import svd

plt.rcParams['figure.figsize'] = (12.0, 8.0)
img=scipy.misc.ascent()
U,s,Vh=svd(img)
A = numpy.dot( U[:,0:32], numpy.dot( numpy.diag(s[0:32]), Vh[0:32,:]))
plt.subplot(121,aspect='equal');
plt.gray()
plt.imshow(img)
plt.subplot(122,aspect='equal');
plt.imshow(A)
plt.show()

A=numpy.mat(numpy.eye(3,k=1))
print(A)

b=numpy.mat(numpy.arange(3) + 1).T
print(b)

xinfo=scipy.linalg.lstsq(A,b)
print (xinfo[0].T)
print('#',50*"-")