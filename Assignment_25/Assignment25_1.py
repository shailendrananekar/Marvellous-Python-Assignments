import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def main():
    Line = "_" * 70
    data = {"Salary": [25000, 27000, 29000, 31000, 50000, 100000]}

    df = pandas.DataFrame(data)

    print(Line + "Q1:")
    print("Outlier detection using IQR method:")
    Q1 = df["Salary"].quantile(0.25)
    Q3 = df["Salary"].quantile(0.75)

    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df["Outlier"] = (df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)
    print(df)

    print(Line + "Q2:")
    print("Detect column data type and convert Age: ")
    data2 = {"Name": ["A", "B", "C"], "Age": [21.0, 22.0, 23.0]}
    df2 = pandas.DataFrame(data2)
    print(df2)
    df2["Age"] = df2["Age"].astype(int)
    print("Data types after conversion:")
    print(df2.dtypes)
    print(df2)

    print(Line + "Q3:")
    print("Label encoding to city column: ")
    data3 = {"City": ["Pune", "Mumbai", "Delhi", "Pune", "Delhi"]}
    df3 = pandas.DataFrame(data3)
    label_encoder = LabelEncoder()
    df3["City_Encoded"] = label_encoder.fit_transform(df3["City"])
    print("After label encoding:")
    print(df3["City"].unique())
    print(df3)

    print(Line + "Q4:")
    print("One-hot Encoding to Department column: ")
    data4 = {"Department": ["HR", "IT", "Finance", "HR", "IT"]}
    df4 = pandas.DataFrame(data4)
    df4_encoded = pandas.get_dummies(df4, columns=["Department"], prefix="Dept")
    df4_combined = pandas.concat([df4, df4_encoded], axis=1)
    print("After one-hot encoding:")
    print(df4_combined)

    print(Line + "Q5:")
    print("Split into train/test sets:")
    data5 = {"Age": [22, 25, 47, 52, 46, 56], "Purchased": [0, 1, 1, 0, 1, 0]}
    df5 = pandas.DataFrame(data5)
    X = df5[["Age"]]
    y = df5["Purchased"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("Train set:")
    print(X_train)
    print("Test set:")
    print(X_test)
    print("Train labels:")
    print(y_train)
    print("Test labels:")
    print(y_test)

    print(Line + "Q6:")
    print("Replace multiple vlaues in a column:")
    data6 = {"Grade": ["A+", "B", "A", "C", "B+"]}
    df6 = pandas.DataFrame(data6)
    df6.replace(
        {
            "A+": "Excellent",
            "A": "Very Good",
            "B+": "Good",
            "B": "Average",
            "C": "Poor",
        },
        inplace=True,
    )
    print("After replacing values:")
    print(df6)

    print(Line + "Q7:")
    print("Normalize age column using Min-Max scaling:")
    data7 = {"Age": [18, 22, 25, 30, 35]}
    df7 = pandas.DataFrame(data7)
    df7["Normalized_Age"] = (df7["Age"] - df7["Age"].min()) / (
        df7["Age"].max() - df7["Age"].min()
    )
    print("After normalization:")
    print(df7)

    print(Line + "Q8:")
    print("Fill missing values using interpolation:")
    data8 = {"Marks": [85, np.nan, 90, np.nan, 95]}
    df8 = pandas.DataFrame(data8)
    df8.interpolate(method="linear", inplace=True)
    print("After filling missing values:")
    print(df8)

    print(Line + "Q9:")
    print("Replace values in marks less then 50 with Fail: ")
    data9 = {"Marks": [45, 67, 88, 32, 76]}
    df9 = pandas.DataFrame(data9)
    df9["Status"] = np.where(df9["Marks"] < 50, "Fail", "Pass")
    print("After replacing values:")
    print(df9)

    print(Line + "Q10:")
    print("split with multiple feature into train/test for supervised:")
    data10 = {
        "Age": [25, 30, 45, 35, 22],
        "Salary": [50000, 60000, 80000, 65000, 45000],
        "Purchased": [1, 0, 1, 0, 1],
    }
    df10 = pandas.DataFrame(data10)
    X = df10[["Age", "Salary"]]
    y = df10["Purchased"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("Train set features:")
    print(X_train)
    print("Test set features:")
    print(X_test)
    print("Train set labels:")
    print(y_train)
    print("Test set labels:")
    print(y_test)


if __name__ == "__main__":
    main()
