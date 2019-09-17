import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="whitegrid")

rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

sns.residplot(x, y, lowess=True, color="g")
plt.show()
print('#',50*"-")