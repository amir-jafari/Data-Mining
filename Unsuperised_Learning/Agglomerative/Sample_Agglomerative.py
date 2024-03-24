from time import time
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering

N_COMPONENTS = 2
N_CLUSTERS = 10


def plot_clustering(X_red, X, labels, title=None):
    x_min, x_max = np.min(X_red, axis=0), np.max(X_red, axis=0)
    X_red = (X_red - x_min) / (x_max - x_min)
    plt.figure(figsize=(6, 4))
    for i in range(X_red.shape[0]):
        plt.text(X_red[i, 0], X_red[i, 1], str(labels[i]),
                 color=plt.cm.Spectral(labels[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    if title is not None:
        plt.title(title, size=17)
    plt.axis('off')
    plt.tight_layout()


digits = datasets.load_digits(n_class=10)
images = digits.data
labels = digits.target
n_samples, n_features = images.shape
np.random.seed(0)


def augment_dataset(images, labels):
    shift = lambda x: ndimage.shift(x.reshape((8, 8)),
                                    .3 * np.random.normal(size=2),
                                    mode='constant',
                                    ).ravel()
    images = np.concatenate([images, np.apply_along_axis(shift, 1, images)])
    labels = np.concatenate([labels, labels], axis=0)
    return images, labels


images, labels = augment_dataset(images, labels)


def embed_data(images):
    print("Computing embedding")
    images_transformed = manifold.SpectralEmbedding(n_components=N_COMPONENTS).fit_transform(images)
    print("Done.")
    return images_transformed


def create_plot_clusters(type, images_transformed, images, labels):
    print(f"{type} linkage")
    clustering = AgglomerativeClustering(linkage=type, n_clusters=N_CLUSTERS)
    t0 = time()
    clustering.fit(images_transformed)
    print(f"{type} : {time() - t0:.2f}s")
    plot_clustering(images_transformed, images, clustering.labels_, f"{type} linkage")


images_transformed = embed_data(images)
for type in ('ward', 'average', 'complete'):
    create_plot_clusters(type, images_transformed, images, labels)

plt.show()