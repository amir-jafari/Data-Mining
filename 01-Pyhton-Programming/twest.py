import numpy as np

a = np.array([1,2,3,4])
print(a)
print(a.shape)

print(a.transpose())

b =a.reshape(-1,1)
print(b.transpose())