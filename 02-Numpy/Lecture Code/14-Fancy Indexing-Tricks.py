import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
i = np.array( [ [0,1],[1,2] ] )
j = np.array( [ [2,1],[3,3] ] )
print(a[i,j]); print(a[i,2]); print(a[:,j])
s = np.array( [i,j] ); print(a[tuple(s)])
time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5,4)
ind = data.argmax(axis=0)
time_max = time[ ind]
data_max = data[ind, range(data.shape[1])]
print(np.all(data_max == data.max(axis=0)))
print('#',50*"-")
a = np.arange(5)
a[[1,3,4]] = 0
print(a)
a[[0,0,2]]+=1
print(a)
print('#',50*"-")