import matplotlib.pyplot as plt
import numpy as np
x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.sin(x2)
plt.plot(x2, y2)
plt.show()
x3 = np.linspace(1, 3, 100)
y3 = x3 ** 2 - 2 * x3 + 1
plt.plot(x3, y3)
plt.show()
print('#',50*"-")