import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="whitegrid", palette="pastel", color_codes=True)

tips = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", hue="smoker",
               split=True, inner="quart",
               palette={"Yes": "y", "No": "b"},
               data=tips)

sns.despine(left=True)
plt.show()
print('#',50*"-")