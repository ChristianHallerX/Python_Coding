import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

"""
KMeans clustering (unsupervised)
Intuition:
More similar points have shorter distances between each other. Group similar data points together in a
specified number of clusters.

1. pick random data points as starting cluster centers

Iterate calculating until convergence (distances below tolerance) or max. iterations reached:
2. distances from each point to each cluster centroid. Assign each point closest cluster centroid as label.
3. Move cluster centroids to the mean of the cluster coordinates
"""


# K-Means implementation
class KMeans:
    def __init__(self, n_clusters, max_iter=300, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        # 1. Randomly initialize centroids
        n_samples, n_features = X.shape
        random_idx = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_idx]

        for i in range(self.max_iter):
            # 2. Assign clusters by calculating distance between X and all cluster centroids, assign min distance
            # cluster (same as predicting cluster labels of completely new X data)
            self.labels = self._assign_clusters(X)

            # 3. Calculate new centroids as the mean coordinates of all points assigned to a cluster
            new_centroids = self._compute_centroids(X)

            # 4. Check for convergence, i.e, break loop early if all distances below tolerance threshold parameter
            # Stop iterating once the centroids stabilize
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break

            self.centroids = new_centroids

    # Helper functions
    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def _compute_centroids(self, X):
        return np.array(
            [X[self.labels == i].mean(axis=0) for i in range(self.n_clusters)]
        )

    def predict(self, X):
        """predict() is a wrapper for '_assign_clusters()"""
        return self._assign_clusters(X)


if __name__ == "__main__":
    # Generate synthetic dataset with x1,x2 coordinates and 4 clobs. y labels are not used since kmeans is unsupervised
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

    # Apply K-Means with n=4
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)

    # Create DF for nicer printing
    data_df = pd.DataFrame(X, columns=["X1", "X2"])
    data_df["Cluster"] = kmeans.labels
    print(data_df.to_string())
