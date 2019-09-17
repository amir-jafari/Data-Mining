import matplotlib.pyplot as plt
import numpy as np
BMI = np.array([5., 30., 45., 22.])
age = np.array( [5., 25., 50., 20.])
x11 = np.arange(4)
plt.barh(x11, BMI, color = 'r')
plt.barh(x11, -age, color = 'b')
plt.show()
print('#',50*"-")