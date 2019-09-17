import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sns.set(style="whitegrid")

diamonds = sns.load_dataset("diamonds")
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

sns.boxplot(x="clarity", y="carat",
              color="b", order=clarity_ranking,
               data=diamonds)
plt.show()
print('#',50*"-")