import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Convert labels to one-hot encoded vectors
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Build a simple feed-forward model
model = Sequential(
    [
        Flatten(
            input_shape=(28, 28)
        ),  # Convert each 28x28 image into a 784-dimension vector
        Dense(128, activation="relu"),  # Hidden layer with ReLU activation
        Dense(
            10, activation="softmax"
        ),  # Output layer for 10 classes with softmax activation
    ]
)

# Compile the model with an optimizer, loss function, and evaluation metric
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Train the model for 5 epochs with a batch size of 64 and validate using the test set
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Evaluate the model on the test dataset
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest accuracy: {test_accuracy * 100:.2f}%")
