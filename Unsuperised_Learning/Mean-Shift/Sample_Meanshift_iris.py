from sklearn import datasets
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from sklearn.cluster import MeanShift
from sklearn.preprocessing import StandardScaler


def load_and_transform_data():
    iris = datasets.load_iris()
    input_data = iris.data[:, [2, 3]]
    scaler = StandardScaler()
    scaler.fit(input_data)
    return scaler.transform(input_data)


def apply_meanshift_clustering(input_data):
    ms_clustering_model = MeanShift(bandwidth=None, seeds=None, n_jobs=1)
    ms_clustering_model.fit(input_data)
    labels = ms_clustering_model.labels_
    cluster_centers = ms_clustering_model.cluster_centers_
    unique_labels = np.unique(labels)
    clusters_count = len(unique_labels)
    return labels, cluster_centers, clusters_count


def plot_clusters(input_data, labels, cluster_centers, clusters_count):
    plt.figure(1)
    plt.clf()
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for cluster_idx, color in zip(range(clusters_count), colors):
        cluster_members = labels == cluster_idx
        cluster_center = cluster_centers[cluster_idx]
        plt.plot(input_data[cluster_members, 0], input_data[cluster_members, 1], color + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=color,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % clusters_count)
    plt.show()


input_data = load_and_transform_data()
labels, cluster_centers, clusters_count = apply_meanshift_clustering(input_data)
print(f"number of estimated clusters : {clusters_count}")
plot_clusters(input_data, labels, cluster_centers, clusters_count)