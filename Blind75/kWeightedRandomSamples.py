"""
Write a function that returns k weighted random samples from a list of items.

items = [a, b, c]
weights_prob = [5, 3, 2]
k = 10

This function implements a weighted random sampling algorithm using a naive linear search approach.
The algorithm works by first calculating cumulative weights for the items. For each sample to be drawn,
a random number is generated, and a linear search is performed over the cumulative weights to find
the corresponding item. This process is repeated until the desired number of samples is obtained.

Time Complexity: O(n + k * n) -> O(k * n)
Space Complexity: O(n) for cumulative weights if we do not regard the k samples output
"""

import random


def weightedRandomSampling(k, items, weights):

    # Initialize the samples list and cumulative weights
    samples = []
    currentSum = 0
    cumulativeWeights = []

    # Calculate cumulative weights
    for weight in weights:
        currentSum += weight
        cumulativeWeights.append(currentSum)

    # Draw k samples
    for i in range(k):

        # Generate random number between 0 and the sum of weights
        randomValue = random.uniform(0, cumulativeWeights[-1])

        # Perform a linear search to find the corresponding item
        for index, cumulativeWeight in enumerate(cumulativeWeights):
            if randomValue < cumulativeWeight:

                # Append the selected item to the samples list
                samples.append(items[index])
                break

    return samples


if __name__ == "__main__":
    print(weightedRandomSampling(k=10, items=["a", "b", "c"], weights=[5, 3, 2]))

    # Test with equal weights
    print(weightedRandomSampling(5, ["a", "b", "c"], [1, 1, 1]))

    # Test with one item having significantly higher weight
    print(weightedRandomSampling(5, ["a", "b", "c"], [10, 1, 1]))

    # Test with zero weight for one item
    print(weightedRandomSampling(5, ["a", "b", "c"], [5, 0, 5]))

    # Test with all weights being zero
    print(weightedRandomSampling(5, ["a", "b", "c"], [0, 0, 0]))

    # Test with negative weights
    print(weightedRandomSampling(5, ["a", "b", "c"], [-1, 2, 3]))

    # Test with large number of samples
    print(weightedRandomSampling(1000, ["a", "b", "c"], [5, 3, 2]))

    # Test with single item
    print(weightedRandomSampling(5, ["a"], [1]))
