import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import warnings

warnings.filterwarnings("ignore")


def visualize_kmeans(n_clusters, X, ax, title):
    y_pred = KMeans(n_clusters=n_clusters, random_state=random_state).fit_predict(X)
    ax.scatter(X[:, 0], X[:, 1], c=y_pred)
    ax.set_title(title)


plt.figure(figsize=(12, 12))
n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

axes = list(plt.subplots(nrows=2, ncols=2, figsize=(10, 10))[1].flatten())
titles = ["Incorrect number of blobs", "Anisotropicly distributed blobs",
          "Unequal variance", "Unevenly sized blobs"]

# Incorrect number of clusters
visualize_kmeans(2, X, axes[0], titles[0])

# Anisotropicly distributed data
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)
visualize_kmeans(3, X_aniso, axes[1], titles[1])

# Different variance
X_varied, y_varied = make_blobs(n_samples=n_samples, random_state=random_state,
                                cluster_std=[1.0, 2.5, 0.5])
visualize_kmeans(3, X_varied, axes[2], titles[2])

# Unevenly sized blobs
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
visualize_kmeans(3, X_filtered, axes[3], titles[3])

plt.show()