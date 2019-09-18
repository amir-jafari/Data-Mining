import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import stats #conda remove scipy --force pip install scipy
scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105,
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107,
103, 98, 96, 112, 112, 93])
xmean = scipy.mean(scores)
sigma = scipy.std(scores)

print((xmean, sigma ))
n = scipy.size(scores)

print(xmean, xmean - 2.576*sigma /scipy.sqrt(n), xmean + 2.576*sigma / scipy.sqrt(n))
plt.stem(scores)
plt.show()

result=scipy.stats.bayes_mvs(scores)
help(scipy.stats.bayes_mvs)
print(result[0])

print('#',50*"-")
# -----------------------
import scipy.stats
help(scipy.stats)
help(scipy.stats.bayes_mvs)
help(scipy.stats.kurtosis)
numpy.info('random')
print('#',50*"-")
# -----------------------
import scipy.misc
img=scipy.misc.ascent()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
img=scipy.misc.face()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
print('#',50*"-")
# -----------------------
import scipy.ndimage
import numpy as np
text = scipy.ndimage.imread('image.png')
text = np.mean(text.astype(float)/255,-1)*2-1
letterE = text[37:53,275:291]
corr = scipy.ndimage.correlate(text,letterE)
eLocations = (corr >= 0.95 * corr.max())
CorrLocIndex = np.where(eLocations==True)
x=CorrLocIndex[1]
print(x)
y=CorrLocIndex[0]
print(y)
thefig=plt.figure()
plt.subplot(211)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.subplot(212)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.autoscale(False)
plt.plot(x,y,'wo',markersize=10)
plt.axis('off')
plt.show()
print('#',50*"-")
# -----------------------
A = numpy.array([1,2,3])
print(A)
B = A[::-1].copy()
B[0]=123
print(B)
C = A + B
C = A - B
dotProduct1 = numpy.dot(A, B)
print(dotProduct1)
Product = (A* B)
print(Product)
dotProduct2 = (A* B).sum()
print(dotProduct2)
crossProduct = numpy.cross(A,B)
print(crossProduct)
print('#',50*"-")
# -----------------------
import scipy.sparse
A=numpy.matrix("1,2,3;4,5,6")
print(A)
A=numpy.matrix([[1,2,3],[4,5,6]])
print(A)
A=numpy.matrix([ [0,10,0,0,0], [0,0,20,0,0], [0,0,0,30,0],
                     [0,0,0,0,40], [0,0,0,0,0] ])
print(A)
print(A[0,1],A[1,2],A[2,3],A[3,4])
rows=numpy.array([0,1,2,3])
cols=numpy.array([1,2,3,4])
vals=numpy.array([10,20,30,40])
A=scipy.sparse.coo_matrix( (vals,(rows,cols)) )
print(A)
print(A.todense())
B=numpy.mat(numpy.ones((3,3)))
W=numpy.mat(numpy.zeros((3,3)))
print(numpy.bmat('B,W;W,B'))
a=numpy.array([[1,2],[3,4]]); print(a)
print(a*a)
v = numpy.dot(a,a); print(v)
print('#',50*"-")
# -----------------------
import scipy.linalg
a=numpy.arange(5)
A=numpy.mat(a)
print(a.shape, A.shape, a.transpose().shape, A.transpose().shape)

A=scipy.linalg.hadamard(8)
zero_sum_rows = (numpy.sum(A,0)==0)
B=A[zero_sum_rows,:]
print(B[0:3,:])

mu=1/numpy.sqrt(2)
A=numpy.matrix([[mu,0,mu],[0,1,0],[mu,0,-mu]])
B=scipy.linalg.kron(A,A)

a=numpy.arange(0,2*numpy.pi,1.6)
A = scipy.linalg.toeplitz(a)
print (A)

print (numpy.exp(A))
print (scipy.linalg.expm(A))
print('#',50*"-")
# -----------------------
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
# -----------------------
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
# -----------------------
x=numpy.linspace(0,1,10)
y=numpy.sin(x*numpy.pi/2)
line=numpy.polyfit(x,y,deg=1)
plt.plot(x,y,'.',x,numpy.polyval(line,x),'r')
plt.show()

spline=scipy.interpolate.UnivariateSpline(x,y,k=2)
xn=numpy.linspace(0,1,100)
plt.plot(x,y,'.', xn, spline(xn))
plt.show()

A=18; w=3*numpy.pi; h=0.5
x=numpy.linspace(0,1,100); y=A*numpy.sin(w*x+h)
plot1, = plt.plot(x, y, '-b', label="Data")
yc=None
yc=scipy.copy(y)
yc += 4*((0.5-scipy.rand(100))*numpy.exp(2*scipy.rand(100)**2)) # contamined data
plot2, = plt.plot(x, yc, 'r+', label="Contamined Data")
plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
print('#',50*"-")
# -----------------------
p0=None
p0 = [20, 2*scipy.pi, 1]
target_function = lambda x,AA,ww,hh: AA*scipy.sin(ww*x+hh)
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
# -----------------------
A=18; w=3*numpy.pi; h=0.5

x=None; y=None
x=numpy.linspace(0,1,100); y=A*numpy.sin(w*x+h)
y += 4*((0.5-scipy.rand(100))*numpy.exp(2*scipy.rand(100)**2))

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
# -----------------------
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
# -----------------------
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
# -----------------------
from scipy.stats import norm
from scipy.stats import ttest_1samp

data = numpy.array([[113,105,130,101,138,118,87,116,75,96,
             122,103,116,107,118,103,111,104,111,89,78,100,89,85,88],
         [137,105,133,108,115,170,103,145,78,107,
              84,148,147,87,166,146,123,135,112,93,76,116,78,101,123]])

dataDiff = data[1,:]-data[0,:]
dataDiff.mean(), dataDiff.std()

plt.rcParams['figure.figsize'] = (15.0, 5.0)
plt.hist(dataDiff)
plt.show()

t_stat,p_value=ttest_1samp(dataDiff,0.0)
print (p_value/2.0)

mean,std=norm.fit(dataDiff)
print(mean,std)
print('#',50*"-")
# -----------------------
from scipy.stats import gaussian_kde

plt.hist(dataDiff, normed=1)
x=numpy.linspace(dataDiff.min(),dataDiff.max(),1000)
pdf=norm.pdf(x,mean,std)
plt.plot(x,pdf)


pdf = gaussian_kde(dataDiff)
pdf = pdf.evaluate(x)
plt.hist(dataDiff, normed=1)
plt.plot(x,pdf,'k')
plt.show()

plt.hist(dataDiff, normed=1)
plt.plot(x,pdf,'k.-',label='Kernel fit')
plt.plot(x,norm.pdf(x,mean,std),'r',label='Normal fit')
plt.legend()
plt.show()
print('#',50*"-")
# -----------------------
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
# -----------------------
from scipy.cluster.hierarchy import linkage, dendrogram

file=open("data.dat","r")
lines=file.readlines()
file.close()
mammals=[]
dataset=numpy.zeros((len(lines),8))
for index,line in enumerate(lines):
    mammals.append( line[0:27].rstrip(" ").capitalize() )
    for tooth in range(8):
        dataset[index,tooth]=int(line[27+tooth])

plt.rcParams['figure.figsize'] = (10.0, 20.0)

Z=linkage(dataset)
dendrogram(Z, labels=mammals, orientation="right")
plt.show()