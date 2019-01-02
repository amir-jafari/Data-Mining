import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(10)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.draw()
plt.show()
print('#',50*"-")
# -----------------------
x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.sin(x2)
plt.plot(x2, y2)
plt.show()
x3 = np.linspace(1, 3, 100)
y3 = x3 ** 2 - 2 * x3 + 1
plt.plot(x3, y3)
plt.show()
print('#',50*"-")
# -----------------------
x4 = np.linspace(0, 2 * np.pi, 100)
ya = np.sin(x4)
yb = np.cos(x4)
plt.plot(x4, ya)
plt.plot(x4, yb)
plt.show()
print('#',50*"-")
# -----------------------
x5 = np.linspace(-3, 3, 100)
y5 = np.exp(-x5 ** 2)
plt.plot(x5, y5)
plt.show()