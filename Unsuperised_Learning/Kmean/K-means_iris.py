import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#-----------------------------------------------------------------------------

iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
#-----------------------------------------------------------------------------
def loss_function(x,z):
    predict1 = z.fit_predict(x)
    sum_distance = 0
    for i in range(0,len(z.cluster_centers_)):
        sum_distance += sum(sum((x[predict1 == i]-z.cluster_centers_[i])**2))
    return sum_distance
#-----------------------------------------------------------------------------
loss_array = []

for i in range(1,6):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(X_train_std)
    loss_array.append(loss_function(X_test_std,kmeans))
plt.figure(1)
plt.scatter([1,2,3,4,5], loss_array)
plt.show()
#-----------------------------------------------------------------------------
kmeans  = KMeans(n_clusters = 5, random_state= 0)
kmeans.fit(X_train_std)
loss = loss_function(X_test_std,kmeans)
print (kmeans.cluster_centers_ )
print (kmeans.fit_predict(X_test_std))
print('loss is : {} when k = 5'.format(loss))
#-----------------------------------------------------------------------------

