import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
X = np.linspace(-15, 15, 1000)
Y = np.sinc(X)
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.grid(True, which='both')
plt.plot(X, Y)
plt.show()
print('#',50*"-")