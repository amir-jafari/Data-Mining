import matplotlib.pyplot as plt
import numpy as np
x6 = []
y6 = []
for line in open('data1.txt', 'r'):
    data = [float(s) for s in line.split()]
    x6.append(data[0])
    y6.append(data[1])
plt.plot(x6, y6)
plt.show()

with open('data1.txt', 'r') as f:
    x7, y7 = zip(*[[float(s) for s in line.split()] for line in f])
plt.plot(x7, y7)
plt.show()

data = np.loadtxt('data1.txt')
plt.plot(data[:,0], data[:,1])
plt.show()
print('#',50*"-")