import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sns.set(style="whitegrid", palette="muted")

iris = sns.load_dataset("iris")

iris = pd.melt(iris, "species", var_name="measurement")

sns.swarmplot(x="measurement", y="value", hue="species",
              palette=["r", "c", "y"], data=iris)
plt.show()
print('#',50*"-")