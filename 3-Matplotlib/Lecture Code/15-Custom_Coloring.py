import matplotlib.pyplot as plt
import numpy as np
a = np.random.standard_normal((100, 2))
a += np.array((-2, -2)) # Center
b = np.random.standard_normal((100, 2))
b += np.array((2, 2)) # Center
plt.scatter(a[:,0], a[:,1], color = '.2')
plt.scatter(b[:,0], b[:,1], color = '.8')
plt.show()
print('#',50*"-")

data = np.random.standard_normal((100, 2))
plt.scatter(data[:,0], data[:,1], color = '1.0', edgecolor='0.0')
plt.show()
print('#',50*"-")