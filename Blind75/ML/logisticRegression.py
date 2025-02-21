import numpy as np


# Define sigmoid activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Train using gradient descent, return weights + bias
def train_logistic_regression(X, y, lr=0.1, epochs=1000):
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights to zeros
    bias = 0  # Initialize bias to zero

    for epoch in range(epochs):
        # Compute the linear combination
        z = np.dot(X, weights) + bias
        # Compute predictions using the sigmoid function
        predictions = sigmoid(z)

        # Calculate gradients for weights and bias
        dw = (1 / m) * np.dot(X.T, (predictions - y))
        db = (1 / m) * np.sum(predictions - y)

        # Update weights and bias
        weights -= lr * dw
        bias -= lr * db

        # print epoch + cost
        if epoch % 100 == 0:
            cost = -(1 / m) * np.sum(
                y * np.log(predictions + 1e-15)
                + (1 - y) * np.log(1 - predictions + 1e-15)
            )
            print(f"Epoch {epoch}, Cost: {cost:.4f}")

    return weights, bias


# Make predictions on new data using weights + bias
def predict(X, weights, bias, threshold=0.5):
    z = np.dot(X, weights) + bias
    probabilities = sigmoid(z)
    return probabilities >= threshold


# Generate a dummy dataset
def generate_dummy_data(num_samples=1000):
    np.random.seed(42)  # For reproducibility

    # Create two clusters (Gaussian blobs) for binary classification
    X0 = np.random.randn(num_samples // 2, 2) + np.array([-2, -2])
    X1 = np.random.randn(num_samples // 2, 2) + np.array([2, 2])
    X = np.vstack((X0, X1))

    # Labels: 0 for the first cluster, 1 for the second
    y = np.hstack((np.zeros(num_samples // 2), np.ones(num_samples // 2)))
    return X, y


def train_test_split(X, y, test_size=0.2):
    m = X.shape[0]
    indices = np.random.permutation(m)
    test_size = int(m * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]


if __name__ == "__main__":
    # Generate the dummy data
    X, y = generate_dummy_data(1000)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the logistic regression model
    weights, bias = train_logistic_regression(X_train, y_train, lr=0.1, epochs=1000)

    # Perform inference on the test set
    y_pred = predict(X_test, weights, bias)

    # Calculate and print the accuracy
    accuracy = np.mean(y_pred == y_test)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")
