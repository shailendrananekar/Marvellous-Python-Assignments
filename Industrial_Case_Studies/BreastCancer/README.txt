# README.txt

## Project Title: Breast Cancer Logistic Regression Pipeline

### Description:
This project implements a machine learning pipeline to predict breast cancer outcomes using logistic regression. The pipeline includes data preprocessing, model training, evaluation, and exporting predictions. The dataset used is the built-in `load_breast_cancer` dataset from `sklearn`.

---

### Features:
1. **Data Loading**:
   - Reads the breast cancer dataset using `sklearn.datasets.load_breast_cancer`.
   - Converts the dataset into a pandas DataFrame for easier manipulation.

2. **Data Splitting**:
   - Splits the dataset into training and testing sets based on a specified percentage.

3. **Pipeline Construction**:
   - Builds a machine learning pipeline with `StandardScaler` for feature scaling and `LogisticRegression` for classification.

4. **Model Training**:
   - Trains the logistic regression model using the training data.

5. **Model Evaluation**:
   - Calculates metrics such as accuracy, precision, recall, F1 score, and confusion matrix.

6. **Feature Importance Visualization**:
   - Plots feature coefficients for logistic regression.

7. **Model Saving and Loading**:
   - Saves the trained model to a `.pkl` file and loads it for future use.

8. **Prediction Export**:
   - Exports predictions to a CSV file, including actual labels, predicted labels, and mismatches.

---

### File Structure:
- **BreastCancer_LogisticRegression_Pipeline.py**: Main Python script containing all functions and the pipeline implementation.
- **breastcancer_LogisticRegression_model.pkl**: Saved model file.
- **breastcancer_predict_LogisticReg.csv**: Exported predictions file.

---

### Dependencies:
The project requires the following Python packages:
- `numpy`
- `pandas`
- `matplotlib`
- `sklearn`
- `pickle`

---

### How to Run:
1. Ensure all dependencies are installed.
2. Run the script using Python:
   ```
   python BreastCancer_LogisticRegression_Pipeline.py
   ```
3. The script will:
   - Train the logistic regression model.
   - Evaluate the model.
   - Save the trained model to `breastcancer_LogisticRegression_model.pkl`.
   - Export predictions to `breastcancer_predict_LogisticReg.csv`.

---

### Output:
1. **Console Output**:
   - Dataset statistics.
   - Model evaluation metrics (accuracy, precision, recall, F1 score, etc.).
   - Feature importance plot.

2. **Files Generated**:
   - `breastcancer_LogisticRegression_model.pkl`: Saved model file.
   - `breastcancer_predict_LogisticReg.csv`: CSV file containing predictions.

---

### Author:
Shailendra Sopan Nanekar  
Date: August 16, 2025  

---

### Notes:
- Ensure all dependencies are installed before running the script.
- Modify file paths