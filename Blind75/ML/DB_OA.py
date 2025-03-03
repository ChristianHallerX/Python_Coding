import numpy as np


def kMeans(x, initial_centroids, k):
    """
    Performs k-means clustering using a while loop until convergence.

    Parameters:
        x (np.ndarray): Data points of shape (n_samples, n_features).
        initial_centroids (np.ndarray): Starting centroids of shape (k, n_features).
        k (int): Number of clusters.

    Returns:
        centroids (np.ndarray): Final centroids.
        labels (np.ndarray): Cluster assignment for each data point.
    """
    centroids = initial_centroids.copy()

    while True:
        # Compute Euclidean distances from each point to each centroid
        distances = np.linalg.norm(x[:, np.newaxis] - centroids, axis=2)
        # Assign each point to the nearest centroid
        labels = np.argmin(distances, axis=1)

        # Compute new centroids as the mean of the points assigned to each cluster
        new_centroids = np.empty_like(centroids)
        for i in range(k):
            points = x[labels == i]
            if len(points) > 0:
                new_centroids[i] = points.mean(axis=0)
            else:
                # Retain the old centroid if no points are assigned to this cluster
                new_centroids[i] = centroids[i]

        # Convergence check: break if centroids have not changed
        if np.array_equal(new_centroids, centroids):
            break

        centroids = new_centroids

    return centroids, labels


def kMeansPlusPlusCentroids(x, k):
    """
    Initializes centroids using the K-Means++ algorithm.

    This function selects k centroids from the dataset x in a way that:
    - The first centroid is chosen uniformly at random from x.
    - Each subsequent centroid is chosen from the remaining data points with a probability proportional to the square
      of the distance to the nearest existing centroid.
    This helps in selecting initial centroids that are well spread out, leading to faster convergence and often better
    clustering results.

    Parameters:
        x (np.ndarray): Data points of shape (n_samples, n_features).
        k (int): Number of centroids to initialize.
    Returns:
        centroids (np.ndarray): Initialized centroids with shape (k, n_features).
    """
    # Set a random seed for reproducibility; ensures that the same centroids are chosen every time.
    np.random.seed(42)

    # Total number of data points
    numDataPoints = x.shape[0]

    # Initialize an empty array to store the centroids.
    # It has k rows (one for each centroid) and the same number of columns as features in x.
    centroids = np.empty((k, x.shape[1]))

    # Randomly select the first centroid from the dataset.
    first_index = np.random.choice(numDataPoints)
    centroids[0] = x[first_index]

    # Compute the squared Euclidean distances from every point in x to the first centroid.
    # These distances serve as the initial values for the probability distribution.
    distances = np.sum((x - centroids[0]) ** 2, axis=1)

    # Loop to select the remaining centroids (from index 1 to k-1)
    for i in range(1, k):
        # Calculate the probability of choosing each point as the next centroid.
        # Each point's probability is proportional to its squared distance from the nearest centroid.
        probabilities = distances / distances.sum()

        # Generate a random number between 0 and 1 to decide which point to select.
        r = np.random.rand()

        # Compute the cumulative sum of probabilities.
        # This cumulative distribution allows us to select a point based on the random number.
        next_index = np.searchsorted(np.cumsum(probabilities), r)

        # Set the selected point as the next centroid.
        centroids[i] = x[next_index]

        # For every point in the dataset, compute the squared Euclidean distance to the new centroid.
        new_distances = np.sum((x - centroids[i]) ** 2, axis=1)

        # Update the distances: for each point, store the smallest distance to any of the centroids selected so far.
        distances = np.minimum(distances, new_distances)

    return centroids


# --------------- Testing and Printing Outputs ---------------


def test_kMeans():
    # Create a data
    x = np.array(
        [[0, 0], [0, 1], [1, 0], [1, 1], [10, 10], [10, 11], [11, 10], [11, 11]],
        dtype=float,
    )

    # Use two starting centroids taken from the data
    initial_centroids = np.array([[0, 0], [10, 10]], dtype=float)

    # Run function
    centroids, labels = kMeans(x, initial_centroids, k=2)

    expected = np.array([[0.5, 0.5], [10.5, 10.5]])

    # Since the order of clusters is arbitrary, sort by the first coordinate.
    centroids_sorted = centroids[np.argsort(centroids[:, 0])]
    expected_sorted = expected[np.argsort(expected[:, 0])]

    print("\nkMeans output centroids:")
    print(centroids_sorted)
    print("Expected centroids:")
    print(expected_sorted)


def test_kMeansPlusPlusCentroids():
    # Create data
    x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    k = 2

    # Run function
    centroids = kMeansPlusPlusCentroids(x, k)

    expected = np.array([[7, 8], [1, 2]])

    print("kMeansPlusPlusCentroids output:")
    print(centroids)
    print("Expected centroids (order may vary):")
    print(expected)


if __name__ == "__main__":

    print("Testing kMeans...")
    test_kMeans()
    print("\nTesting kMeansPlusPlusCentroids...")
    test_kMeansPlusPlusCentroids()
