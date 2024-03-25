import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score

# Constants
TEST_SIZE = 0.3
ESTIMATORS = 100
FEATURES_COUNT = 15


def load_data():
    return pd.read_csv('Data/breast_cancer_data.csv', sep=',', header=0)


def explore_data(data):
    print("Dataset No. of Rows: ", data.shape[0])
    print("Dataset No. of Columns: ", data.shape[1])
    print("Dataset first few rows:\n ")
    print(data.head(2))
    print("Dataset info:\n ")
    print(data.info())
    print(data.describe(include='all'))
    print("Sum of NULL values in each column. ")
    print(data.isnull().sum())


def preprocess_data(data):
    data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data


def train_model(X_train, y_train, estimator_count):
    model = RandomForestClassifier(n_estimators=estimator_count)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_pred_score = model.predict_proba(X_test)
    print("Classification Report: ")
    print(classification_report(y_test, y_pred))
    print("\n")
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    print("\n")
    print("ROC_AUC : ", roc_auc_score(y_test, y_pred_score[:, 1]) * 100)


def heatmap(conf_matrix, class_names):
    df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)
    plt.figure(figsize=(5, 5))
    hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20},
                     yticklabels=df_cm.columns, xticklabels=df_cm.columns)
    hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
    hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
    plt.ylabel('True label', fontsize=20)
    plt.xlabel('Predicted label', fontsize=20)
    plt.tight_layout()
    plt.show()


# Loading the data
data = load_data()
explore_data(data)

# Preprocessing the data
data = preprocess_data(data)
X = data.values[:, 1:]
Y = data.values[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=TEST_SIZE, random_state=100)

# Training models and evaluating
random_forest_all = train_model(X_train, y_train, ESTIMATORS)
evaluate_model(random_forest_all, X_test, y_test)

newX_train = X_train[:, random_forest_all.feature_importances_.argsort()[::-1][:FEATURES_COUNT]]
newX_test = X_test[:, random_forest_all.feature_importances_.argsort()[::-1][:FEATURES_COUNT]]
random_forest_k = train_model(newX_train, y_train, ESTIMATORS)
evaluate_model(random_forest_k, newX_test, y_test)

heatmap(confusion_matrix(y_test, random_forest_all.predict(X_test)), data['diagnosis'].unique())
heatmap(confusion_matrix(y_test, random_forest_k.predict(newX_test)), data['diagnosis'].unique())