import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.datasets import make_classification

# Generate synthetic genomic-like dataset
X, y = make_classification(
    n_samples=200,        # patients
    n_features=200,       # genes
    n_informative=20,     # genes truly affecting disease
    n_redundant=10,       # noisy genes
    random_state=42
)

# Real cancer biomarker names + synthetic genes
real_biomarkers = ["BRCA1", "TP53", "BCR-ABL"]  # real cancer-linked genes
other_genes = [f"Gene_{i}" for i in range(197)]
gene_names = real_biomarkers + other_genes

X = pd.DataFrame(X, columns=gene_names)
y = LabelEncoder().fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Select top 50 genes
selector = SelectKBest(f_classif, k=50)
X_train_sel = selector.fit_transform(X_train, y_train)
X_test_sel = selector.transform(X_test)

# Train Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_sel, y_train)

# Predictions
pred = model.predict(X_test_sel)
proba = model.predict_proba(X_test_sel)[:, 1]

# Evaluation
print("Accuracy:", accuracy_score(y_test, pred))
print("ROC-AUC:", roc_auc_score(y_test, proba))
print("\nClassification Report:\n", classification_report(y_test, pred))

# Top genes contributing to prediction
sel_genes = X.columns[selector.get_support()]
importance = model.feature_importances_
top_idx = importance.argsort()[::-1][:10]

print("\nTop 10 predictive genes:")
print(pd.DataFrame({
    "Gene": sel_genes[top_idx],
    "Importance": importance[top_idx]
}))
