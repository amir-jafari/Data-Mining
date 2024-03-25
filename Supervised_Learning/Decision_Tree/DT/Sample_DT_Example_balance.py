import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
import warnings
warnings.filterwarnings("ignore")
# -------------------------------------------------------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
# -------------------------------------------------------------------------------------------------------------------
data = pd.read_csv('Data/balance-scale.data.csv', sep=',', header=None)
data.columns = ['Class_Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance']
print("Dataset No. of Rows: ", data.shape[0])
print("Dataset No. of Columns: ", data.shape[1])
print("Dataset first few rows:\n ")
print(data.head())
print("Dataset info:\n ")
print(data.info())
print(data.describe(include='all'))


X = data.values[:, 1:5]
y = data.values[:, 0]
# ------------------------------------------------------------------------------------------------------------------
class_le = LabelEncoder()
y = class_le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
# -------------------------------------------------------------------------------------------------------------------
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
# -------------------------------------------------------------------------------------------------------------------
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
# -------------------------------------------------------------------------------------------------------------------
y_pred_gini = clf_gini.predict(X_test)
y_pred_entropy = clf_entropy.predict(X_test)
# -------------------------------------------------------------------------------------------------------------------
print("Results Using Gini Index: \n")
print("Classification Report: ")
print(classification_report(y_test,y_pred_gini))
print("Accuracy : ", accuracy_score(y_test, y_pred_gini) * 100)
print("Results Using Entropy: \n")
print("Classification Report: ")
print(classification_report(y_test,y_pred_entropy))
print("Accuracy : ", accuracy_score(y_test, y_pred_entropy) * 100)
# -------------------------------------------------------------------------------------------------------------------
conf_matrix = confusion_matrix(y_test, y_pred_gini)
class_names = data.Class_Name.unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )
# -------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.tight_layout()
plt.show()
# -------------------------------------------------------------------------------------------------------------------
conf_matrix = confusion_matrix(y_test, y_pred_entropy)
class_names = data.Class_Name.unique()
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------------------------------
dot_data = export_graphviz(clf_gini, filled=True, rounded=True, class_names=class_names, feature_names=data.iloc[:, 1:5].columns, out_file=None)
graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_gini.pdf")
webbrowser.open_new(r'decision_tree_gini.pdf')
# -------------------------------------------------------------------------------------------------------------------
dot_data = export_graphviz(clf_entropy, filled=True, rounded=True, class_names=class_names, feature_names=data.iloc[:, 1:5].columns, out_file=None)
graph = graph_from_dot_data(dot_data)
graph.write_pdf("decision_tree_entropy.pdf")
webbrowser.open_new(r'decision_tree_entropy.pdf')
