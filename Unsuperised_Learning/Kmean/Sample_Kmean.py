import warnings
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

warnings.filterwarnings('ignore')


def loss_function(data, kmeans_model):
    predict1 = kmeans_model.fit_predict(data)
    sum_distance = 0
    for i in range(len(kmeans_model.cluster_centers_)):
        sum_distance += sum(sum((data[predict1 == i] - kmeans_model.cluster_centers_[i]) ** 2))
    return sum_distance


def calculate_kmeans_loss(n_clusters, data):
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans_model.fit(X_train_std)
    return loss_function(data, kmeans_model)


iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
scaler.fit(X_train)
X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

loss_array = [calculate_kmeans_loss(i, X_test_std) for i in range(1, 6)]

plt.figure(1)
plt.scatter([1, 2, 3, 4, 5], loss_array)
plt.show()

kmeans_model = KMeans(n_clusters=5, random_state=0)
kmeans_model.fit(X_train_std)
loss = loss_function(X_test_std, kmeans_model)
print(kmeans_model.cluster_centers_)
print(kmeans_model.fit_predict(X_test_std))
print('loss is : {} when k = 5'.format(loss))