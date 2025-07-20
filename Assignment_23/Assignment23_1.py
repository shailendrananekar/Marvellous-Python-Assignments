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

    print("Shape of the DataFrame:")
    print(df.shape)
    print("Columns of the DataFrame:")
    print(df.columns)
    print("Datatypes of the DataFrame:")
    print(df.dtypes)
    print(Line + "Q2:")

    print("Descriptive Statistic :")
    print(df.describe())
    print(Line + "Q3:")

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print("DataFrame after adding Total column:")
    print(df)
    print(Line + "Q4:")

    print("Students whose Science score is greater than or equal to 85:")
    df_filtered = df[df["Science"] >= 85]
    print(df_filtered["Name"].tolist())

    print(Line + "Q5:")
    print("Replace Pooja with Puja")
    df.replace("Pooja", "Puja", inplace=True)
    print(df)

    print(Line + "Q6:")
    print("Sort Dataframe by Total marks in descending order:")
    df.sort_values(by="Total", ascending=False, inplace=True)
    print(df)

    print(Line + "Q7:")
    print("Bar chart of student name vs Total Marks")
    df.plot(x="Name", y=["Total"], kind="bar")
    plt.title("Total Marks of Students")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.show()
    print(Line + "Q8:")

    print("line chart of marks for Amit across all subjects")
    df_amit = df[df["Name"] == "Amit"]
    subjects = ["Math", "Science", "English"]
    marks = df_amit[subjects].values[0]

    plt.plot(subjects, marks, marker="o", linestyle="-", color="blue")
    plt.title("Amit's Marks in Subjects")
    plt.grid(True)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

    print(Line + "Q9:")
    data2 = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 76, 88],
        "Science": [91, np.nan, 85],
    }

    df2 = pandas.DataFrame(data2)
    print("DataFrame with NaN values:")
    print(df2)
    print("DataFrame after filling NaN values with mean() : ")

    df2.fillna(
        {"Math": df2["Math"].mean(), "Science": df2["Science"].mean()}, inplace=True
    )

    print(df2)

    print(Line + "Q10:")
    print("Dataframe with dropping English column:")
    df.drop(columns=["English"], inplace=True)
    print(df)


if __name__ == "__main__":
    main()
