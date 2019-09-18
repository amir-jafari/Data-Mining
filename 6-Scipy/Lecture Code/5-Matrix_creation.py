import numpy
import scipy
import matplotlib.pyplot as plt

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