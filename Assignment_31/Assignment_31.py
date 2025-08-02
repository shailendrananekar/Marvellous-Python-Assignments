import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn

import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    VotingClassifier,
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
)
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permutation_importance


def Marvellous_BreastCancer_ensemble():

    Line = "_" * 70

    df = datasets.load_breast_cancer(as_frame=True).frame

    print(Line)
    print("Missing values :")
    print(df.isna().sum())

    print(Line)
    print("Statistical Information: ")
    print(df.describe())

    print(Line)
    print("Distribution graph : ")
    seaborn.countplot(data=df, x="target")
    plt.title("Class Distribution")
    plt.show()

    print(Line)
    print("First few records of dataset are :")
    print(df.head())
    print("Dimension of dataset is: ", df.shape)
    print(Line)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    (numeric_cols.remove("target") if "target" in numeric_cols else None)

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    X = df.drop(columns=["target"])
    y = df["target"]

    print("Dimension of target :", X.shape)
    print("Dimension of Labels :", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model3 = DecisionTreeClassifier(random_state=42)
    model = VotingClassifier(
        estimators=[
            ("rf", model1),
            ("gb", model2),
            ("dt", model3),
        ],
        voting="soft",
    )

    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    print(Line)
    print("Feature importance graph ! ")
    result = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)

    importance = pandas.Series(result.importances_mean, index=X.columns)
    importance = importance.sort_values(ascending=False)
    importance.plot(kind="bar", figsize=(10, 6), title="Feature importance")
    plt.show()

    print(Line)
    accuracy = accuracy_score(y_test, y_predict)
    cm = confusion_matrix(y_test, y_predict)
    classificationreport = classification_report(y_test, y_predict)
    print("Accuracy => ")
    print(accuracy)
    print("Confusion matrix =>")
    print(cm)
    print("classificationreport => ")
    print(classificationreport)

    y_predict_proba = model.predict_proba(X_test)[:, 1]
    rocaucreport = roc_auc_score(y_test, y_predict_proba)
    print("rocaucreport: ", rocaucreport)
    print(Line)

    print("Confution Matrix Graph ! ")
    plt.figure(figsize=(10, 7))
    seaborn.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["No", "Yes"],
        yticklabels=["No", "Yes"],
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
    print(Line)

    print("ROC Curve Graph ! ")
    fpr, tpr, thresholds = roc_curve(y_test, y_predict_proba)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f"AUC = {rocaucreport:.2f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()


def main():
    Marvellous_BreastCancer_ensemble()


if __name__ == "__main__":
    main()
