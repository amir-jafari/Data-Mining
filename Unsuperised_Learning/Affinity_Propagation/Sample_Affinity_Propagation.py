import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets import make_blobs


def generate_sample_data():
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5,
                                random_state=0)
    return X, labels_true


def compute_affinity_propagation(X):
    clustering_model = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = clustering_model.cluster_centers_indices_
    labels = clustering_model.labels_
    num_clusters = len(cluster_centers_indices)
    return num_clusters, cluster_centers_indices, labels


def print_cluster_evaluation_scores(labels_true, labels):
    print('Estimated number of clusters: %d' % len(set(labels)))
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels, metric='sqeuclidean'))


def plot_clusters(X, cluster_centers_indices, labels, num_clusters):
    plt.close('all')
    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(num_clusters), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
        for x in X[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % num_clusters)
    plt.show()


X, labels_true = generate_sample_data()
num_clusters, cluster_centers_indices, labels = compute_affinity_propagation(X)
print_cluster_evaluation_scores(labels_true, labels)
plot_clusters(X, cluster_centers_indices, labels, num_clusters)