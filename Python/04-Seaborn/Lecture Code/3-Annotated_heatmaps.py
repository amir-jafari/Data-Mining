import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set()

flights_long = sns.load_dataset("flights")

flights = flights_long.pivot("month", "year", "passengers")


f, ax = plt.subplots(figsize=(9, 6))

sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()
print('#',50*"-")