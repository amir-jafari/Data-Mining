import matplotlib.pyplot as plt
import numpy as np
a = np.random.standard_normal((100, 2))
a += np.array((-2, -2)) # Center
b = np.random.standard_normal((100, 2))
b += np.array((2, 2)) # Center
plt.scatter(a[:,0], a[:,1], color = 'k', marker = 'x')
plt.scatter(b[:,0], b[:,1], color = 'k', marker = '^')
plt.show()
print('#',50*"-")

X = np.linspace(-6, 6, 1024)
Y1 = np.sinc(X)
Y2 = np.sinc(X) + 1
plt.plot(X, Y1, marker = 'o', color = '.75')
plt.plot(X, Y2, marker = 'o', color = 'k', markevery = 32)
plt.show()

a = np.random.standard_normal((100, 2))
a += np.array((-1, -1))
b = np.random.standard_normal((100, 2))
b += np.array((1, 1))
plt.scatter(b[:,0], b[:,1], c = 'r', s = 100)
plt.scatter(a[:,0], a[:,1], c = 'b', s = 25)
plt.show()
print('#',50*"-")