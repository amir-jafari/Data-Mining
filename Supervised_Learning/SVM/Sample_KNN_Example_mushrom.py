import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


# Function to load and prepare the data
def load_and_prepare_data(filename):
    mushroom_data = pd.read_csv(filename, sep=',', header=None)
    mushroom_data.columns = ['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment',
                             'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root',
                             'stalk-surf-abv-ring', 'stalk-surf-bel-ring', 'stalk-color-abv-ring',
                             'stalk-color-bel-ring',
                             'veil-type', 'veil-color', 'ring-number', 'ring-type',
                             'spore-print-color', 'population', 'habitat']
    mushroom_data.replace('?', np.NaN, inplace=True)
    mushroom_data = mushroom_data.apply(lambda x: x.fillna(x.value_counts().index[0]))
    return mushroom_data


# Function to convert data
def convert_data(mushroom_data):
    X_data = pd.get_dummies(mushroom_data.iloc[:, 1:])
    X = X_data.values
    Y_data = mushroom_data.values[:, 0]
    class_le = LabelEncoder()
    y = class_le.fit_transform(Y_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
    return X_data, X_train, X_test, y_train, y_test


# Function for SVM classification and prediction
def svm_classification(X_train, y_train):
    clf = SVC(kernel="linear")
    clf.fit(X_train, y_train)
    return clf


# Function to visualize important features
def coef_values(coef, names):
    imp = coef
    imp, names = zip(*sorted(zip(imp.ravel(), names)))
    imp_pos_10 = imp[-10:]
    names_pos_10 = names[-10:]
    imp_neg_10 = imp[:10]
    names_neg_10 = names[:10]
    imp_top_20 = imp_neg_10 + imp_pos_10
    names_top_20 = names_neg_10 + names_pos_10
    plt.barh(range(len(names_top_20)), imp_top_20, align='center')
    plt.yticks(range(len(names_top_20)), names_top_20)
    plt.show()


# Function to visualize confusion matrix
def visualize_confusion_matrix(y_test, y_pred, df_cm):
    plt.figure(figsize=(5, 5))
    sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d',
                yticklabels=df_cm.columns, xticklabels=df_cm.columns)
    plt.ylabel('True label', fontsize=20)
    plt.xlabel('Predicted label', fontsize=20)
    plt.tight_layout()
    plt.show()
# Function for visualising ROC curve
def roc_chart(y_test, y_pred_proba):
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc = roc_auc_score(y_test, y_pred_proba)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()


# Main function
def main():
    mushroom_data = load_and_prepare_data("Data/agaricus-lepiota.data.csv")
    X_data, X_train, X_test, y_train, y_test = convert_data(mushroom_data)
    clf = svm_classification(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("Classification Report: ")
    print(classification_report(y_test, y_pred))

    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)

    coef_values(clf.coef_, X_data.columns)

    conf_matrix = confusion_matrix(y_test, y_pred)
    class_names = mushroom_data['class'].unique()
    df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)
    visualize_confusion_matrix(y_test, y_pred, df_cm)

    y_pred_proba = clf.decision_function(X_test)
    roc_chart(y_test, y_pred_proba)


if __name__ == "__main__":
    main()