import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
DATA_PATH = "Data/iris.data.csv"


def load_dataset():
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    data = pd.read_csv(DATA_PATH, header=None, names=col_names)
    X = data.values[:, :-1]
    Y = data.values[:, -1]
    return X, Y, data['class'].unique()


def train_model(X, Y):
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_std = scaler.transform(X_train)
    X_test_std = scaler.transform(X_test)

    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X_train_std, y_train)

    y_pred = knn_classifier.predict(X_test_std)
    print("Classification Report: ")
    print(classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)

    return y_test, y_pred


def show_matrix(y_test, y_pred, class_names):
    conf_matrix = confusion_matrix(y_test, y_pred)
    df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)

    plt.figure(figsize=(5, 5))
    hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20},
                     yticklabels=df_cm.columns, xticklabels=df_cm.columns)
    hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=45, ha='right', fontsize=10)
    hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=10)
    plt.ylabel('True label', fontsize=20)
    plt.xlabel('Predicted label', fontsize=20)
    plt.tight_layout()
    plt.show()


X, Y, class_names = load_dataset()
y_test, y_pred = train_model(X, Y)
show_matrix(y_test, y_pred, class_names)