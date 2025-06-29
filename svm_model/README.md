# Fraud Detection using SVM (Support Vector Machine)
This module uses **Linear SVM with SMOTE** to detect fraudulent transactions in credit card data.
## File
fraud_svm.py`: Python file with code for data loading, preprocessing, training, and evaluating the SVM model.
## Features
- Load and clean credit card transaction data
- Scale features using StandardScaler
- Handle imbalanced classes using SMOTE
- Train a Linear SVM model with CalibratedClassifierCV
- Evaluate model using:
  - Confusion Matrix
  - Classification Report
  - ROC Curve
  - Precision-Recall Curve
  - AUC Score
## Visualizations
### Confusion Matrix
![Confusion Matrix](../plots/svm_confusion.png)
### Classification Report
![Classification Report](../plots/svm_classification.png)
### ROC Curve
![ROC Curve](../plots/svm_roc.png)
### Precision-Recall Curve
![Precision-Recall](../plots/svm_pr.png)
## Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- imbalanced-learn (SMOTE)
- Matplotlib, Seaborn


