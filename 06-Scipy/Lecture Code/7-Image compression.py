import numpy
import scipy
import matplotlib.pyplot as plt
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