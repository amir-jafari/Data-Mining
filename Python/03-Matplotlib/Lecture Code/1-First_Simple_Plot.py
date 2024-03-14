import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(0,2*np.pi,0.002)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.draw()
plt.show()
print('#',50*"-")