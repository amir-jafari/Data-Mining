# =================================================================
# Class_Ex1:
# Use numpy a anf find the unique numbers in array A.
# ----------------------------------------------------------------
import numpy
A = numpy.array([5,1,1,2,1,1,2,2,10,3,3,4,5])


print('#',50*"-")

# =================================================================
# Class_Ex2:
# Find the number of counts of each unique digits.
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex3:
# Why there is warning for C array , Explain it.
# ----------------------------------------------------------------
B = numpy.fromfunction((lambda i,j: (i+1)*(-1)**(i*j)), (4,4))
print(B)
C = numpy.log2(B)




# =================================================================
# Class_Ex4:
# Interpolate the following array using UnivariateSpline method
# ----------------------------------------------------------------
x=numpy.arange(5)
y=numpy.sin(x)
xn=numpy.linspace(0,4,40)






# =================================================================
# Class_Ex5:
# Create a numpy array that has all the values of DataFrame.
# ----------------------------------------------------------------





# =================================================================
# Class_Ex6:
# Read baseball data into a DataFrame and check the first and last
# 10 rows
# ----------------------------------------------------------------






# =================================================================
# Class_Ex7:
# Create  a unique index by specifying the id column as the index
# Check the new df and verify it is unique
# ----------------------------------------------------------------
