import matplotlib.pyplot as plt
import numpy as np
a = np.random.rand(4)
b = np.random.rand(4)
x9 = np.arange(4)
plt.bar(x9, a, color = 'b')
plt.bar(x9, b, color = 'r', bottom = a)
plt.show()
print('#',50*"-")