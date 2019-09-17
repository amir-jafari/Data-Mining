import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
N = 256
angle = np.linspace(0, 8 * 2 * np.pi, N)
radius = np.linspace(.5, 1., N)
X = radius * np.cos(angle)
Y = radius * np.sin(angle)
plt.scatter(X, Y, c = angle, cmap = cm.hsv)
plt.show()
print('#',50*"-")

import matplotlib.colors as col
values = np.random.random_integers(99, size = 50)
cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)
plt.bar(np.arange(len(values)), values, color = cmap.to_rgba(values))
plt.show()
print('#',50*"-")