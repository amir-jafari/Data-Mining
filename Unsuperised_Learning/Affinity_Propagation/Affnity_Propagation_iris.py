from sklearn.cluster import AffinityPropagation
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from itertools import cycle

AFFINITY_PROPAGATION_PARAMS = {
    "damping": 0.9,
    "max_iter": 500,
    "convergence_iter": 150,
    "copy": True,
    "preference": -30,
    "affinity": 'euclidean'
}


def preprocess_data(data):
    sc = StandardScaler()
    sc.fit(data)
    return sc.transform(data)


def perform_clustering(data, params):
    af = AffinityPropagation(**params)
    af.fit(data)
    return af.cluster_centers_indices_, af.labels_


def plot_clusters(data, centers_indices, data_labels):
    plt.figure(1)
    plt.clf()
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    n_clusters = len(centers_indices)
    for k, col in zip(range(n_clusters), colors):
        class_members = data_labels == k
        cluster_center = data[centers_indices[k]]
        plt.plot(data[class_members, 0], data[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
        for point in data[class_members]:
            plt.plot([cluster_center[0], point[0]], [cluster_center[1], point[1]], col)
    plt.title('Estimated number of clusters: %d' % n_clusters)
    plt.show()


if __name__ == "__main__":
    iris = datasets.load_iris()
    iris_features = iris.data[:, [2, 3]]
    processed_data = preprocess_data(iris_features)

    cluster_centers_indices, labels = perform_clustering(processed_data, AFFINITY_PROPAGATION_PARAMS)
    print('Estimated number of clusters: %d' % len(cluster_centers_indices))

    plot_clusters(processed_data, cluster_centers_indices, labels)