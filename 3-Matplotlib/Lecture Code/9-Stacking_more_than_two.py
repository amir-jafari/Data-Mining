import matplotlib.pyplot as plt
import numpy as np
a = np.random.rand(4)
b = np.random.rand(4)
c = np.random.rand(4)
x10 = np.arange(4)
plt.bar(x10, a, color = 'b' )
plt.bar(x10, b, color = 'g', bottom = a)
plt.bar(x10, c, color = 'r', bottom = a + b)
plt.show()
print('#',50*"-")

