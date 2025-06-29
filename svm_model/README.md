# Fraud Detection using SVM (Support Vector Machine)
This module uses **Linear SVM** with class balancing via **SMOTE** to detect fraudulent transactions in credit card data.
## File
fraud_svm.py`: Python file with data preprocessing, model training, evaluation, and plotting.
## Features
- Load and clean the credit card dataset
- Apply feature scaling using StandardScaler
- Handle class imbalance using SMOTE
- Train a Linear SVM model using CalibratedClassifierCV
- Evaluate model performance with:
  - Confusion Matrix
  - Classification Report
  - ROC Curve
  - Precision-Recall Curve
  - AUC Score
## Visualizations
![ROC Curve](../plots/svm_roc.png)
![Precision-Recall](../plots/svm_pr.png)
![Confusion Matrix](../plots/svm_confusion.png)
![Classification Report](../plots/svm_classification.png)

## Tools Used
- Python
- Pandas, NumPy
- Scikit-learn
- imbalanced-learn (SMOTE)
- Matplotlib, Seaborn





