import numpy as np
from collections import Counter

"""
1. Training phase (fit)
KNN is a lazy learner, meaning it does no real “training” and artifact creation: it simply stores the
feature vectors and labels of all X samples in the class.

2. Inference
To classify a new point:
    - Compute distances between the new point and every point in the training set (e.g. Euclidean distance).
    - Select the k nearest points (the ones with the smallest distances).
    - Vote among those k neighbors:
        -- For classification, take the majority class among the neighbors.
        -- (For regression, you’d take the average of their target values.)
    - Return the voted class as the prediction.

3. K = the number of neighbors
    - Small k → more flexible decision boundary (can overfit).
    - Large k → smoother boundary (can underfit).

4. Distance metric
By default Euclidean distance, but can use Manhattan, Minkowski, etc.
"""


class KNNClassifier:
    def __init__(self, k=3, distance_metric="euclidean"):
        """
        k: number of neighbors
        distance_metric: 'Euclidean' or 'manhattan'
        """
        self.k = k
        self.distance_metric = distance_metric
        self._fit_X = None
        self._fit_y = None

    def fit(self, X, y):
        """
        Simply memorize the training data.
        X: numpy array of shape (n_samples, n_features)
        y: numpy array of shape (n_samples,)
        """
        self._fit_X = X
        self._fit_y = y

    def _compute_distance(self, x1, x2):
        """
        Compute distance between two points.
        """
        if self.distance_metric == "euclidean":
            return np.sqrt(np.sum((x1 - x2) ** 2))
        elif self.distance_metric == "manhattan":
            return np.sum(np.abs(x1 - x2))
        else:
            raise ValueError(f"Unsupported distance metric: {self.distance_metric}")

    def predict(self, X):
        """
        Predict class labels for samples in X.
        X: numpy array of shape (m_samples, n_features)
        Returns: numpy array of shape (m_samples,)
        """
        # Ensure we've been fitted
        if self._fit_X is None or self._fit_y is None:
            raise ValueError("Must fit classifier before predicting!")

        predictions = []
        # Iterate over each sample to classify
        for x in X:
            # Compute distances from current point to all other training
            distances = [self._compute_distance(x, x_train) for x_train in self._fit_X]

            # Get indices of the k smallest distances
            k_idx = np.argsort(distances)[: self.k]

            # Get the labels of the k nearest neighbors
            k_neighbor_labels = self._fit_y[k_idx]

            # Majority vote
            most_common = Counter(k_neighbor_labels).most_common(1)
            predictions.append(most_common[0][0])

        return np.array(predictions)

    def score(self, X, y_true):
        """
        Predict y (on train OR test set) and compute accuracy y (train vs test set).
        """
        y_pred = self.predict(X)
        return np.mean(y_pred == y_true)


if __name__ == "__main__":
    # Generate some synthetic data
    from sklearn.datasets import make_blobs

    X_train, y_train = make_blobs(n_samples=200, centers=3, random_state=42)
    X_test, y_test = make_blobs(n_samples=40, centers=3, random_state=24)

    # Create object
    knn = KNNClassifier(k=5)

    # Fit
    knn.fit(X_train, y_train)

    # Accuracy score (includes predict)
    accuracy = knn.score(X_test, y_test)
    print(f"Test accuracy: {accuracy:.2f}")
