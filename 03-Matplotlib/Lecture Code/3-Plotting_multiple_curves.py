import matplotlib.pyplot as plt
import numpy as np
x4 = np.linspace(0, 2 * np.pi, 100)
ya = np.sin(x4)
yb = np.cos(x4)
plt.plot(x4, ya)
plt.plot(x4, yb)
plt.show()
print('#',50*"-")