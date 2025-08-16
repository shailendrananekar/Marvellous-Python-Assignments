import pandas
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn
import matplotlib.pyplot as plt



def ArticleFakeorReal():
    fake_df = pandas.read_csv("Fake.csv")
    real_df = pandas.read_csv("True.csv")
    fake_df["label"] = 0
    real_df["label"] = 1
    df = pandas.concat([fake_df, real_df], ignore_index=True)

    df = df.dropna(subset=["title", "text"])
    df["content"] = df["title"] + " " + df["text"]

    X = df["content"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier(random_state=42)

    hard_voting = VotingClassifier(
        estimators=[("Logistic", lr), ("DecisionTree", dt)],
        voting="hard",
    )

    soft_voting = VotingClassifier(
        estimators=[("Logistic", lr), ("DecisionTree", dt)],
        voting="soft",
    )

    models = {
        "Logistic Regression": lr,
        "Decision Tree": dt,
        "Hard Voting": hard_voting,
        "Soft Voting": soft_voting,
    }

    for name, model in models.items():
        model.fit(X_train_tfidf, y_train)
        y_pred = model.predict(X_test_tfidf)

        print(f"Model: {name}")
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
        print(classification_report(y_test, y_pred))
        print(confusion_matrix(y_test, y_pred))

        seaborn.heatmap(
            confusion_matrix(y_test, y_pred),
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["Fake", "Real"],
            yticklabels=["Fake", "Real"],
        )
        plt.title(f"Confusion Matrix - {name}")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()
        

def main():
    ArticleFakeorReal()


if __name__ == "__main__":
    main()
