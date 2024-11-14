import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


# K-Means implementation
class KMeans:
    def __init__(self, n_clusters, max_iter=300, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        # Randomly initialize centroids
        n_samples, n_features = X.shape
        random_idx = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_idx]

        for i in range(self.max_iter):
            # Assign clusters by calculating distance between X and all cluster centroids
            # (same as predicting cluster labels of completely new X data)
            self.labels = self._assign_clusters(X)

            # Calculate new centroids as the mean coordinates of all points assigned to a cluster
            new_centroids = self._compute_centroids(X)

            # Check for convergence, i.e, break loop early if all distances below tolerance threshold parameter
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
        return self._assign_clusters(X)


# Generate synthetic dataset with x1,x2 coordinates. y labels are not used since kmeans is unsupervised
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Apply K-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Create a DataFrame for data points
data_df = pd.DataFrame(X, columns=["X1", "X2"])
data_df["Cluster"] = kmeans.labels
# Create a DataFrame for centroids
centroids_df = pd.DataFrame(kmeans.centroids, columns=["X1", "X2"])
centroids_df["Cluster"] = range(len(kmeans.centroids))
centroids_df["Centroid"] = "Yes"
# Mark data points as not centroids
data_df["Centroid"] = "No"
# Combine data points and centroids into one DataFrame
results_df = pd.concat([data_df, centroids_df], ignore_index=True)
# Display the table
print(results_df.to_string(index=False))

# Plot the results
# plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels, cmap="viridis", marker="o")
# plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c="red", marker="x")
# plt.title("K-Means Clustering")
# plt.show()
