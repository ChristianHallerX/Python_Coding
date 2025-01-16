"""
Binary classification with XGboost
"""

import numpy as np
from xgboost import XGBClassifier

# 1 Create Data. Features: Each row has 3 features
X = np.array(
    [
        [1.0, 2.0, 3.0],
        [1.5, 2.5, 3.2],
        [2.0, 2.0, 2.0],
        [3.0, 2.0, 2.2],
        [3.5, 3.5, 4.0],
        [4.0, 3.5, 3.0],
    ]
)
# Create Labels (binary classification)
y = np.array([0, 1, 0, 0, 1, 1])

# 2 Split data and labels into train and test
X_train = X[:4]
y_train = y[:4]

X_test = X[4:]
y_test = y[4:]


# 3 Initialize the XGBClassifier
model = XGBClassifier(
    n_estimators=10,  # number of boosting rounds
    learning_rate=0.1,  # step size shrinkage
    max_depth=3,  # maximum depth of a tree
    # use_label_encoder=False,  # disable automatic label encoding
    eval_metric="logloss",  # evaluation metric
)
# Train the model
model.fit(X_train, y_train)


# 4 Run inference (prediction)
y_pred = model.predict(X_test)

# Predict probabilities for each test sample and class  (prob for class "0" and prob for class "1")
y_pred_proba = model.predict_proba(X_test)

print("Test samples:\n", X_test)
print("True labels: \n", y_test)
print("Predicted labels: \n", y_pred)
print("Predicted probabilities:\n", y_pred_proba)
