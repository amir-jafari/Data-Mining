import matplotlib.pyplot as plt
import numpy as np
values = np.random.random_integers(99, size = 50)
color_set = ('.00', '.25', '.50', '.75')
color_list = [color_set[(len(color_set) * val) // 100] for val in
values]
plt.bar(np.arange(len(values)), values, color = color_list)
plt.show()
print('#',50*"-")