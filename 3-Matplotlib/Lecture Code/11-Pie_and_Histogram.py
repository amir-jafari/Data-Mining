import matplotlib.pyplot as plt
import numpy as np
data = np.array([5, 25, 50, 20])
plt.pie(data)
plt.show()

x12 = np.random.randn(1000)
plt.hist(x12, bins = 20)
plt.show()
print('#',50*"-")