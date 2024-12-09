import numpy as np


class LinearRegression:
    def __init__(self):
        self.theta = None  # Parameters (weights) of the model

    def fit(self, X, y):
        """
        Fit the linear regression model to the training data using the normal equation.

        Parameters:
        X : numpy.ndarray
            Feature matrix of shape (n_samples, n_features).
        y : numpy.ndarray
            Target vector of shape (n_samples, 1).
        """
        # Add a b (bias intercept) term to the feature matrix
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # Compute the optimal parameter theta using the "normal equation". @ = matrix multiplication in numpy
        # equivalent do np.dot() or np.matmul()
        self.theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

    def predict(self, X):
        """
        Predict target values using the linear regression model.

        Parameters:
        X : numpy.ndarray
            Feature matrix of shape (n_samples, n_features).

        Returns:
        y_pred : numpy.ndarray
            Predicted target vector of shape (n_samples, 1).
        """
        # Add a b (bias intercept) term to the feature matrix, concat X with ones
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # Compute predictions y_pred, @ = matrix multiplication in numpy
        return X_b @ self.theta


# Generate synthetic linear data
np.random.seed(42)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # 100 samples, 1 feature
true_slope = 3.5
true_intercept = 1.2
noise = np.random.randn(100, 1)
y = true_intercept + true_slope * X + noise  # y = 1.2 + 3.5 * x + noise

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_new = np.array([[0], [2]])  # New x1,x2 data for prediction
y_pred = model.predict(X_new)
print(y_pred)
