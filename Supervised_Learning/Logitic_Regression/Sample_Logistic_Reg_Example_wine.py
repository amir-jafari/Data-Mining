import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

DATA_PATH = "Data/winequality-red.csv"
CSV_DELIMITER = ';'
RANDOM_STATE = 100
TEST_SIZE = 0.3


def load_and_prepare_data():
    wine_data = pd.read_csv(DATA_PATH, sep=CSV_DELIMITER)
    wine_data['quality'] = wine_data['quality'].apply(lambda x: 0 if x <= 5 else 1)

    X = wine_data.values[:, :-1]
    Y = wine_data.values[:, -1]

    return train_test_split(X, Y, test_size=TEST_SIZE, random_state=RANDOM_STATE), wine_data


def perform_training(X_train, y_train):
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    return clf


def evaluate_model(clf, X_test, y_test, wine_data):
    y_pred = clf.predict(X_test)
    y_pred_score = clf.predict_proba(X_test)

    print("Classification Report: ")
    print(classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    print("ROC_AUC : ", roc_auc_score(y_test, y_pred_score[:, 1]) * 100)

    display_confusion_matrix(y_test, y_pred, wine_data)


def display_confusion_matrix(y_test, y_pred, wine_data):
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_names = wine_data['quality'].unique()
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


def main():
    (X_train, X_test, y_train, y_test), wine_data = load_and_prepare_data()
    clf = perform_training(X_train, y_train)
    evaluate_model(clf, X_test, y_test, wine_data)


if __name__ == "__main__":
    main()