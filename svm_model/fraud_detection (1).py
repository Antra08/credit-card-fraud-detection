# -*- coding: utf-8 -*-
"""Fraud Detection

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W6pcM8ZVuk14c-9ogMqxQwT8UKzMiA8J
"""

from google.colab import drive
drive.mount('/content/drive')

my_folder = "/content/drive/MyDrive/fraud_data"

import pandas as pd

df=pd.read_csv("/content/drive/MyDrive/fraud_data/creditcard.csv")
df.head()

pd.options.display.max_columns = None
df.head()

df.isnull().values.any()

df.duplicated().any()

df.drop_duplicates()

pd.options.display.max_rows = None
df.head()

print(df.info())
print(df['Class'].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

class_counts = df['Class'].value_counts()
print("Class distribution:")
print(class_counts)

sns.barplot(x=class_counts.index, y=class_counts.values)
plt.title('Class Distribution (0 = Non-Fraud, 1 = Fraud)')
plt.xlabel('Class')
plt.ylabel('Number of Transactions')
plt.show()

from sklearn.preprocessing import StandardScaler

X = df.drop('Class', axis=1)
y = df['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

!pip install imblearn

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)

from collections import Counter
print('Original train class distribution:', Counter(y_train))
print('Balanced train class distribution:', Counter(y_train_bal))

from sklearn.svm import SVC

from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_auc_score, RocCurveDisplay, PrecisionRecallDisplay,
                             ConfusionMatrixDisplay)
import matplotlib.pyplot as plt
import seaborn as sns

base_svm = LinearSVC(max_iter=10000, class_weight='balanced', random_state=42)
svm_model = CalibratedClassifierCV(base_svm)

svm_model.fit(X_train_bal, y_train_bal)


y_pred = svm_model.predict(X_test)
y_proba = svm_model.predict_proba(X_test)[:, 1]

#Classification Report
print("📄 Classification Report:\n")
print(classification_report(y_test, y_pred))

#  Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("🧾 Confusion Matrix:\n", cm)

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Step 4.1: Plot Classification Report
# Convert classification report to a dataframe
report_dict = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()

# Select only class 0 and class 1 rows (skip 'accuracy', 'macro avg' if desired)
report_df = report_df.loc[['0', '1']]

# Plot as heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(report_df.iloc[:, :-1], annot=True, cmap='Greens', fmt=".2f")  # exclude 'support'
plt.title("Classification Report - Linear SVM")
plt.ylabel("Class (0=Non-Fraud, 1=Fraud)")
plt.xlabel("Metric")
plt.show()

# Step 5: ROC Curve
RocCurveDisplay.from_estimator(svm_model, X_test, y_test)
plt.title('ROC Curve - Linear SVM')
plt.grid()
plt.show()

# Step 6: Precision-Recall Curve
PrecisionRecallDisplay.from_estimator(svm_model, X_test, y_test)
plt.title('Precision-Recall Curve - Linear SVM')
plt.grid()
plt.show()

# Step 7: AUC Score
auc = roc_auc_score(y_test, y_proba)
print(f"📈 ROC AUC Score: {auc:.4f}")