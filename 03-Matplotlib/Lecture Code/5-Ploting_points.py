import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(1024, 2)
plt.scatter(data[:,0], data[:,1])
plt.show()
print('#',50*"-")