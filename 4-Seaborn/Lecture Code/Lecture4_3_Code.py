import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# sns.set(style="ticks")
#
# df = sns.load_dataset("anscombe")
#
# sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, palette="muted",
#            scatter_kws={"s": 50, "alpha": 1})
#
# plt.show()
# print('#',50*"-")
# # -----------------------
# sns.set(style="white", palette="muted", color_codes=True)
# rs = np.random.RandomState(10)
#
# f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
# sns.despine(left=True)
#
# d = rs.normal(size=100)
#
# sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
#
# sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
#
# sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
#
# sns.distplot(d, color="m", ax=axes[1, 1])
# plt.setp(axes, yticks=[])
#
# plt.tight_layout()
# plt.show()
#
# print('#',50*"-")
# # -----------------------
# sns.set()
#
# flights_long = sns.load_dataset("flights")
#
# flights = flights_long.pivot("month", "year", "passengers")
#
#
# f, ax = plt.subplots(figsize=(9, 6))
#
# sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
#
# plt.show()
# print('#',50*"-")
# # -----------------------
# sns.set(style="whitegrid", palette="pastel", color_codes=True)
#
# tips = sns.load_dataset("tips")
#
# sns.violinplot(x="day", y="total_bill", hue="smoker",
#                split=True, inner="quart",
#                palette={"Yes": "y", "No": "b"},
#                data=tips)
#
# sns.despine(left=True)
# plt.show()
# print('#',50*"-")
# # -----------------------
sns.set(style="darkgrid")

df = sns.load_dataset("titanic")

pal = dict(male="#6495ED", female="#F08080")

g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
               palette=pal, y_jitter=.02, logistic=True)

g.set(xlim=(0, 80), ylim=(-.05, 1.05))

plt.show()
print('#',50*"-")
# -----------------------