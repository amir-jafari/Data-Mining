import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(3,4)
x8 = np.arange(4)
plt.bar(x8 + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(x8 + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(x8 + 0.50, data[2], color = 'r', width = 0.25)
plt.show()
print('#',50*"-")