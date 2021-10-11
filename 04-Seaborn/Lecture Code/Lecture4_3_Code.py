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
# -----------------------
sns.set(style="white", palette="muted", color_codes=True)
rs = np.random.RandomState(10)

f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.despine(left=True)

d = rs.normal(size=100)

sns.distplot(d, kde=False, color="b", ax=axes[0, 0])

sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])

sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

sns.distplot(d, color="m", ax=axes[1, 1])
plt.setp(axes, yticks=[])

plt.tight_layout()
plt.show()

print('#',50*"-")
# -----------------------
sns.set()

flights_long = sns.load_dataset("flights")

flights = flights_long.pivot("month", "year", "passengers")


f, ax = plt.subplots(figsize=(9, 6))

sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="whitegrid", palette="pastel", color_codes=True)

tips = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", hue="smoker",
               split=True, inner="quart",
               palette={"Yes": "y", "No": "b"},
               data=tips)

sns.despine(left=True)
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="darkgrid")

df = sns.load_dataset("titanic")

pal = dict(male="#6495ED", female="#F08080")

g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
               palette=pal, y_jitter=.02, logistic=True)

g.set(xlim=(0, 80), ylim=(-.05, 1.05))

plt.show()
print('#',50*"-")
# -----------------------
import pandas as pd
sns.set(style="whitegrid", palette="muted")

iris = sns.load_dataset("iris")

iris = pd.melt(iris, "species", var_name="measurement")

sns.swarmplot(x="measurement", y="value", hue="species",
              palette=["r", "c", "y"], data=iris)
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
m = df.g.map(ord)
df["x"] += m
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, palette=pal)
g.map(sns.kdeplot, "x", clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw=.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
           ha="left", va="center", transform=ax.transAxes)
g.map(label, "x")
g.fig.subplots_adjust(hspace=-.25)
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="whitegrid")

rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

sns.residplot(x, y, lowess=True, color="g")
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="white")

rs = np.random.RandomState(5)
mean = [0, 0]
cov = [(1, .5), (.5, 1)]
x1, x2 = rs.multivariate_normal(mean, cov, 500).T

x1 = pd.Series(x1, name="$X_1$")
x2 = pd.Series(x2, name="$X_2$")


g = sns.jointplot(x1, x2, kind="kde", height=7, space=0)
plt.show()
print('#',50*"-")
# -----------------------
sns.set(style="whitegrid")

diamonds = sns.load_dataset("diamonds")
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

sns.boxplot(x="clarity", y="carat",
              color="b", order=clarity_ranking,
               data=diamonds)
plt.show()
print('#',50*"-")
# -----------------------