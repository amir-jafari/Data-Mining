import numpy
import scipy
import matplotlib.pyplot as plt

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