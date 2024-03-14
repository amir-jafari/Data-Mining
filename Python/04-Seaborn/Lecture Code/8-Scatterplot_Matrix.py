import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
plt.show()
print('#',50*"-")
# ------------------