import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.preprocessing import StandardScaler
import pickle


def MarvellousDiabeticDecisionTreeClassifier(datapath):

    Line = "_" * 70

    df = pandas.read_csv(datapath)

    print(Line)
    print("First few records of dataset are :")
    print(df.head())
    print("Dimension of dataset is: ", df.shape)

    print(Line)
    print("Statistical Information: ")
    print(df.describe())

    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]

    print(Line)
    print("Dimension of target :", X.shape)
    print("Dimension of Labels :", y.shape)

    print(Line)
    print("Histogram of diabetic outcome")
    figure()
    df["Glucose"].plot.hist().set_title("Glucose Histogram report")
    show()

    print(Line)
    print("Box plot of diabetic outcome")
    figure()
    df["Glucose"].plot.box().set_title("Glucose Box plot report")
    show()

    print(Line)
    print("Pair plot of diabetic outcome")
    seaborn.pairplot(df, hue="Outcome", diag_kind="kde")
    plt.title("Pair plot of diabetic outcome")
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    print(Line)
    accuracy = accuracy_score(y_test, y_predict)
    cm = confusion_matrix(y_test, y_predict)
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)
    f1 = f1_score(y_test, y_predict)
    print("Accuracy : ", accuracy)
    print("Confusion matrix:")
    print(cm)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1 Score: ", f1)
    seaborn.heatmap(
        confusion_matrix(y_test, y_predict), annot=True, fmt="d", cmap="Blues"
    )
    plt.title("Confusion Matrix Heatmap")
    plt.show()

    print(Line)
    print("Exporting model to pickle file")
    file = open("diabetic_DecisionTree_model.pkl", "wb")
    pickle.dump(model, file)
    file.close()
    print("Model exported successfully!")
    print(Line)
    saved_model = pickle.load(open("diabetic_DecisionTree_model.pkl", "rb"))
    new_predict = saved_model.predict(X_test)
    print("Test data size: ", X_test.shape)
    print("Predictions based on X_test data : ")
    print(new_predict)

    print(Line)
    df = pandas.DataFrame(X_test, columns=X.columns)
    df["Outcome"] = y_test.values
    df["Predicted"] = new_predict
    print(df.head())

    print(Line)
    print("Exporting predictions to CSV file")
    df["Mismatch"] = df["Outcome"] != df["Predicted"]
    df.to_csv("diabetic_predict_DecisionTree.csv", index=False)
    print("Predictions exported successfully!")


def main():
    MarvellousDiabeticDecisionTreeClassifier("diabetes.csv")


if __name__ == "__main__":
    main()
