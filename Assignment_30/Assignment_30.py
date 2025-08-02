import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
import pickle


def MarvellousBankRandomForestClassifier(datapath):

    Line = "_" * 70

    df = pandas.read_csv(datapath, sep=";")

    df.replace("unknown", pandas.NA, inplace=True)

    print(Line)
    print("Missing values :")
    print(df.isna().sum())

    cat_cols = df.select_dtypes(include="object").columns.tolist()
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    print(Line)
    print("Statistical Information: ")
    print(df.describe())

    print(Line)
    print("Distribution graph : ")
    seaborn.countplot(data=df, x="y")
    plt.title("Class Distribution")
    plt.show()

    # Identify categorical columns (excluding target 'y')
    cat_cols = df.select_dtypes(include="object").drop(columns=["y"]).columns.tolist()

    # Apply One-Hot Encoding
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    encoded_array = encoder.fit_transform(df[cat_cols])

    # Convert to DataFrame
    encoded_df = pandas.DataFrame(
        encoded_array, columns=encoder.get_feature_names_out(cat_cols)
    )

    # Concatenate with original DataFrame
    df = pandas.concat([df.drop(columns=cat_cols), encoded_df], axis=1)

    print(Line)
    print("First few records of dataset are :")
    print(df.head())
    print("Dimension of dataset is: ", df.shape)
    print(Line)

    # Identify numeric columns (excluding target 'y')
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    (
        numeric_cols.remove("duration") if "duration" in numeric_cols else None
    )  # Optional: exclude if it's target

    # Scale numeric features
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    X = df.drop(columns=["y"])
    y = df["y"]

    print("Dimension of target :", X.shape)
    print("Dimension of Labels :", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)

    print(Line)
    print("Feature importance graph ! ")
    importance = pandas.Series(model.feature_importances_, index=X.columns)
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

    y_test_binary = (y_test == "yes").astype(int)
    y_predict_proba = model.predict_proba(X_test)[:, 1]
    rocaucreport = roc_auc_score(y_test_binary, y_predict_proba)
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
    fpr, tpr, thresholds = roc_curve(y_test_binary, y_predict_proba)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f"AUC = {rocaucreport:.2f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()


def main():
    MarvellousBankRandomForestClassifier("bank-full.csv")


if __name__ == "__main__":
    main()
