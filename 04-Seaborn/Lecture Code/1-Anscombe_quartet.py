import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="ticks")

df = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted",
           scatter_kws={"s": 50, "alpha": 1})

plt.show()
print('#',50*"-")