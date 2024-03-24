import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift, estimate_bandwidth

CYCLE_COLORS = 'bgrcmykbgrcmykbgrcmykbgrcmyk'
BLOB_CENTERS = [[1, 1], [-1, -1], [1, -1]]
BLOB_SAMPLES = 10000
BLOB_STD_DEVIATION = 0.6
BANDWIDTH_QUANTILE = 0.2
SAMPLE_BANDWIDTH = 500
PLOT_MARKER_SIZE = 14


def generate_data() -> np.array:
    data, _ = make_blobs(n_samples=BLOB_SAMPLES, centers=BLOB_CENTERS, cluster_std=BLOB_STD_DEVIATION)
    return data


def mean_shift_clustering(data: np.array) -> tuple:
    bandwidth = estimate_bandwidth(data, quantile=BANDWIDTH_QUANTILE, n_samples=SAMPLE_BANDWIDTH)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    cluster_labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    unique_labels = np.unique(cluster_labels)
    return cluster_labels, cluster_centers, unique_labels


def plot_data(data: np.array, labels: np.array, centers: np.array, unique_labels: np.array):
    plt.figure(1)
    plt.clf()
    colors = cycle(CYCLE_COLORS)
    num_clusters = len(unique_labels)
    for cluster_id, color in zip(range(num_clusters), colors):
        members_of_cluster = labels == cluster_id
        cluster_center = centers[cluster_id]
        plt.plot(data[members_of_cluster, 0], data[members_of_cluster, 1], color + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=color,
                 markeredgecolor='k', markersize=PLOT_MARKER_SIZE)
    plt.title(f'Estimated number of clusters: {num_clusters}')
    plt.show()


sample_data = generate_data()
labels, centers, unique_labels = mean_shift_clustering(sample_data)
plot_data(sample_data, labels, centers, unique_labels)