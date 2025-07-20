import pandas
import matplotlib.pyplot as plt
import numpy as np


def main():
    Line = "_" * 70
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
    }

    df = pandas.DataFrame(data)

    print(Line + "Q1:")
    df["normalized_math_score"] = (df["Math"] - df["Math"].mean()) / (
        df["Math"].max() - df["Math"].min()
    )

    print("Normalized Math scores : ")
    print(df)

    print(Line + "Q2:")
    print("After one-hot encoding :")

    df["gender"] = ["Male", "Male", "Female"]
    df_encoded = pandas.get_dummies(df, columns=["gender"])
    print(df_encoded)

    print(Line + "Q3:")
    print("Group Student by gender and calculate average scores:")
    df_avg = df.groupby("gender")[["Math", "Science", "English"]].mean()
    print(df_avg)

    print(Line + "Q4:")
    print("Pie chart for Sagar")
    df_sagar = df[df["Name"] == "Sagar"]
    subjects = ["Math", "Science", "English"]
    scores = df_sagar[subjects].values.flatten()
    plt.pie(scores, labels=subjects, autopct="%1.1f%%")
    plt.title("Sagar's Scores Distribution")
    plt.show()

    print(Line + "Q5:")
    print(" new column status added: ")
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    df["Status"] = np.where(df["Total"] >= 250, "Pass", "Fail")
    print(df)

    print(Line + "Q6:")
    print("Count of students Passed")
    pass_count = df[df["Status"] == "Pass"].shape[0]
    print(f"passed: {pass_count}")

    print(Line + "Q7:")
    print("Export data frame to csv file")
    df.to_csv("students_scores.csv", index=False)

    print(Line + "Q8:")
    print("Plot a histogram of Math marks:")
    plt.hist(
        df["Math"].to_list(), bins=5, color="skyblue", edgecolor="black", density=False
    )
    plt.title("Distribution of Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    plt.show()

    print(Line + "Q9:")
    print("Rename Math column to Mathematics: ")
    df.rename(columns={"Math": "Mathematics"}, inplace=True)
    print(df)

    print(Line + "Q10:")
    print("box plot for English marks: ")
    df.boxplot(column=["English"])
    plt.title("Box Plot of English Marks")
    plt.ylabel("Marks")
    plt.show()


if __name__ == "__main__":
    main()
