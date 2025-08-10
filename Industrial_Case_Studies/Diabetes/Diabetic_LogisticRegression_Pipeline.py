########################################################
# Required Python Packages
########################################################

import numpy
import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

########################################################
# File Paths
########################################################

FILE_DATA_PATH = "diabetes.csv"
MODEL_PATH = "diabetic_LogisticRegression_model.pkl"
EXPORT_PREDICTIONS_PATH = "diabetic_predict_LogisticReg.csv"
Line = "_" * 80

########################################################
# Function name :  read_data
# Description :    Read the data into pandas dataframe
# Inpt :           path of CSV file
# Output :         Gives the data
# Author :         Shailendra Sopan Nanekar
# Date :           10/08/2025
########################################################


def read_data(path):
    """
    Reads the CSV file from the given path and returns a pandas DataFrame.

    :param path: str, path to the CSV file
    :return: pandas DataFrame containing the data
    """
    try:
        df = pandas.read_csv(path)
        return df
    except Exception as e:
        print(f"Error reading data from {path}: {e}")
        return None


########################################################
# Function name :    dataset_statistics
# Description :       Display the statistics
# Author :            Shailendra Sopan Nanekar
# Date :              10/08/2025
########################################################


def dataset_statistics(dataset):
    """
    Displays the first few records, dimensions, and statistical information of the dataset.

    :param dataset: pandas DataFrame containing the dataset
    """
    if dataset is not None:
        print(Line)
        print("First few records of dataset are:")
        print(dataset.head())
        print(Line)
        print("Dimension of dataset is:", dataset.shape)
        print(Line)
        print("Statistical Information:")
        print(dataset.describe())
    else:
        print("Dataset is empty or not loaded.")


########################################################
# Function name :    split_dataset
# Description :       Split the dataset with train_percentage
# Input :             Dataset with related information
# Output :            Dataset after splitting
# Author :            Shailendra Sopan Nanekar
# Date :              10/08/2025
########################################################


def split_dataset(dataset, train_percentage, feature_headers, target_headers):
    """
    Splits the dataset into training and testing sets based on the given train percentage.

    :param dataset: pandas DataFrame containing the dataset
    :param train_percentage: float, percentage of data to be used for training
    :param feature_headers: list of feature column names
    :param target_headers: list of target column names
    :return: tuple of training and testing sets (X_train, X_test, y_train, y_test)
    """
    X = dataset[feature_headers]
    y = dataset[target_headers]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=train_percentage, random_state=42
    )

    return X_train, X_test, y_train, y_test


########################################################
# Function name :    build_pipeline
#  Description :      Build a Pipeline:
#  SimpleImputer:    replace missing with median
#                     RandomForestClassifier: robust baseline
# Author :            Shailendra Sopan Nanekar
# Date :              10/08/2025
########################################################


def build_pipeline():
    """
    Builds a machine learning pipeline with a StandardScaler and LogisticRegression.

    :return: sklearn Pipeline object
    """
    pipe = Pipeline(
        [("scaler", StandardScaler()), ("classifier", LogisticRegression())]
    )
    return pipe


########################################################
# Function name :    train_pipeline
#  Description :     Train a Pipeline:
# Author :           Shailendra Sopan Nanekar
# Date :             10/08/2025
########################################################


def train_pipeline(pipeline, X_train, y_train):
    """
    Trains the given pipeline with the training data.

    :param pipeline: sklearn Pipeline object
    :param X_train: pandas DataFrame, training features
    :param y_train: pandas Series, training labels
    :return: trained sklearn Pipeline object
    """
    try:
        pipeline.fit(X_train, y_train)
        print(Line)
        print("Pipeline trained successfully.")
        return pipeline
    except Exception as e:
        print(f"Error during training: {e}")
        return None


########################################################
# Function name :    plot_feature_importances
# Description :      Display the feture importance
# Author :           Shailendra Sopan Nanekar
# Date :             10/08/2025
#########################################


def plot_feature_importances(model, feature_names):
    print(Line)
    """
    Plots the feature importances of the trained model.

    :param model: trained sklearn model
    :param feature_names: list of feature names
    """
    if hasattr(model, "feature_importances_"):
        print("Feature importances found, plotting feature importances.")
        importances = model.feature_importances_
        indices = numpy.argsort(importances)[::-1]

        plt.figure(figsize=(10, 6))
        plt.title("Feature Importances")
        plt.bar(range(len(importances)), importances[indices], align="center")
        plt.xticks(
            range(len(importances)), [feature_names[i] for i in indices], rotation=90
        )
        plt.xlim([-1, len(importances)])
        plt.show()
    elif hasattr(model, "coef_"):
        print("Model coefficients found, plotting feature importances based on coefficients.")
        coefficients = model.coef_[0]
        indices = numpy.argsort(numpy.abs(coefficients))[::-1]

        plt.figure(figsize=(10, 6))
        plt.title("Feature Coefficients")
        plt.bar(range(len(coefficients)), coefficients[indices], align="center")
        plt.xticks(
            range(len(coefficients)), [feature_names[i] for i in indices], rotation=90
        )
        plt.xlim([-1, len(coefficients)])
        plt.show()
    else:
        print("Model does not have feature importances.")


########################################################
# Function name :   save_model
#  Description :    Save the model
# Author :          Shailendra Sopan Nanekar
# Date :            10/08/2025
########################################################


def save_model(model, path):
    print(Line)
    """
    Saves the trained model to a file.

    :param model: trained sklearn model
    :param path: str, path where the model will be saved
    """
    try:
        with open(path, "wb") as file:
            pickle.dump(model, file)
        print(f"Model saved successfully to {path}.")
    except Exception as e:
        print(f"Error saving model: {e}")


########################################################
# Function name :    load_model
#  Description :     Load the trained model
# Author :           Shailendra Sopan Nanekar
# Date :             10/08/2025
########################################################


def load_model(path):
    print(Line)
    """
    Loads a trained model from a file.

    :param path: str, path to the model file
    :return: loaded sklearn model
    """
    try:
        with open(path, "rb") as file:
            model = pickle.load(file)
        print(f"Model loaded successfully from {path}.")
        return model
    except Exception as e:
        print(f"Error loading model from {path}: {e}")
        return None


########################################################
# Function name :    export_predictions
#  Description :     Export predictions to a CSV file
# Author :           Shailendra Sopan Nanekar
# Date :             10/08/2025
########################################################


def export_predictions(X_test, y_test, predictions, output_file):
    print(Line)
    """
    Exports the predictions to a CSV file.

    :param X_test: pandas DataFrame, test features
    :param y_test: pandas Series, actual labels
    :param predictions: numpy array, predicted labels
    :param output_file: str, path to the output CSV file
    """
    df_predictions = pandas.DataFrame(X_test, columns=X_test.columns)
    df_predictions["Actual"] = y_test.values
    df_predictions["Predicted"] = predictions
    df_predictions["Mismatch"] = df_predictions["Actual"] != df_predictions["Predicted"]

    try:
        df_predictions.to_csv(output_file, index=False)
        print(f"Predictions exported successfully to {output_file}.")
    except Exception as e:
        print(f"Error exporting predictions: {e}")



def main():
    

    # Read the dataset
    dataset = read_data(FILE_DATA_PATH)

    #  Display dataset statistics
    dataset_statistics(dataset)

    # Prepare feature and target headers
    feature_headers = list(dataset.columns.drop("Outcome"))
    target_headers = "Outcome"

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(
        dataset, 0.7, feature_headers, target_headers
    )

    #  Build and train the pipeline
    pipeline = build_pipeline()
    trained_model = train_pipeline(pipeline, X_train, y_train)

    # predictions
    predictions = trained_model.predict(X_test)

    # Metrics
    print(Line)
    print("Train Accuracy :: ", accuracy_score(y_train, trained_model.predict(X_train)))
    print("Test Accuracy  :: ", accuracy_score(y_test, predictions))
    print("Classification Report:\n", classification_report(y_test, predictions))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("Precision Score:", precision_score(y_test, predictions))
    print("Recall Score:", recall_score(y_test, predictions))
    print("F1 Score:", f1_score(y_test, predictions))

    # Plot feature importances
    plot_feature_importances(trained_model.named_steps["classifier"], feature_headers)

    # Save the trained model
    save_model(trained_model, MODEL_PATH)

    # Load model and test a sample
    loaded = load_model(MODEL_PATH)
    prediction_loaded = loaded.predict(X_test)
    print(Line)
    print("Loaded model prediction for first test sample:", prediction_loaded)

    # Exporting prediction t oa CSV file
    export_predictions(X_test, y_test, prediction_loaded, EXPORT_PREDICTIONS_PATH)


########################################################
# Application starter
########################################################

if __name__ == "__main__":
    main()

