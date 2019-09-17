import matplotlib.pyplot as plt
import numpy as np
data = [5, 10, 30, 8]
plt.bar(range(len(data)), data)
plt.show()
print('#',50*"-")

plt.bar(range(len(data)), data, width = 1.)
plt.show()

plt.barh(range(len(data)), data)
plt.show()
print('#',50*"-")