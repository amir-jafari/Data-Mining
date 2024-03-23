import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


def load_data(file_path):
    data = pd.read_csv(file_path, sep=',', header=0)
    print("Dataset No. of Rows: ", data.shape[0])
    print("Dataset No. of Columns: ", data.shape[1])
    print(data.head(2))
    print(data.info())
    print(data.describe(include='all'))
    return data


def split_data(data):
    X = data.values[:, :-1]
    Y = data.values[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, y_test


def train_model(X, y):
    clf = GaussianNB()
    clf.fit(X, y)
    return clf


def evaluate_model(clf, X, y):
    y_pred = clf.predict(X)
    y_pred_score = clf.predict_proba(X)
    print("Classification Report: ")
    print(classification_report(y, y_pred))
    print("Accuracy : ", accuracy_score(y, y_pred) * 100)
    print("\n")
    print("ROC_AUC : ", roc_auc_score(y, y_pred_score[:, 1]) * 100)
    print("\n")
    return confusion_matrix(y, y_pred)


def confusion_matrix_heatmap(data, cf_matrix):
    class_names = data['Outcome'].unique()
    df_cm = pd.DataFrame(cf_matrix, index=class_names, columns=class_names)

    plt.figure(figsize=(5, 5))
    hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d',
                     annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
    hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
    hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
    plt.ylabel('True label', fontsize=20)
    plt.xlabel('Predicted label', fontsize=20)
    plt.tight_layout()
    plt.show()


data = load_data('Data/pima_diabetes.csv')
X_train, X_test, y_train, y_test = split_data(data)
model = train_model(X_train, y_train)
cf_matrix = evaluate_model(model, X_test, y_test)
confusion_matrix_heatmap(data, cf_matrix)