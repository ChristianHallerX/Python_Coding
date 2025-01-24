"""
Fixing similarity functions

The cosine similarity and euclidean distance functions are incorrect.

Please fix the body of the two functions
"""

import numpy as np


def cosine_broken(vector1, vector2):
    return (np.linalg.norm(vector1) * np.linalg.norm(vector2)) / np.dot(
        vector1, vector2
    )


def euclidean_broken(vector1, vector2):
    return np.sqrt(np.linalg.norm(vector1 - vector2))


# problem: numerator and denominator were flipped
def cosine(vector1, vector2):
    return np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )


# Function to calculate Euclidean distance
def euclidean(vector1, vector2):
    return np.linalg.norm(np.array(vector1) - np.array(vector2))


def main():
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    print(cosine(vector1, vector2), "expected: 0.9746")
    print(euclidean(vector1, vector2), "expected: 5.1962")


if __name__ == "__main__":
    main()
