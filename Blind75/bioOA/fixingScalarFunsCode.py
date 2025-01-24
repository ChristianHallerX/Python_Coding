"""
Fixing scalar functions

The normalization and standardization functions in the following code are incorrect.

The input parameter 'values' is a list of numerical values and is never empty.

Feel free to use the NumPy library, but pay attention to the type of the returned values: they must be lists.

Please fix the body of the min_max_scaler() and standardize() functions.

Here are examples of one input and the expected results.
"""

from math import sqrt


def min_max_scaler_broken(values):
    minvalue = min(values)
    denominator = sqrt(max(values) - minvalue)
    values_normalized = []

    for value in values:
        values_normalized.append((value - minvalue) / denominator)

    return values_normalized


def standardize_broken(values):
    length_values = len(values)
    diffs = [value - min(values) for value in values]
    std = sqrt(sum([diff**2 for diff in diffs]) / length_values)
    meanvalue = sum(values) / length_values
    values_standardized = []
    for value in values:
        values_standardized.append((value - meanvalue) / std)
    return values_standardized


def min_max_scaler(values):
    min_value = min(values)
    max_value = max(values)
    values_normalized = [
        (value - min_value) / (max_value - min_value) for value in values
    ]
    return values_normalized


def standardize(values):
    mean_value = sum(values) / len(values)
    std = (sum((value - mean_value) ** 2 for value in values) / len(values)) ** 0.5
    values_standardized = [(value - mean_value) / std for value in values]
    return values_standardized


def main():
    # Test
    values = [1, 2, 3, -5, 0]
    print("min_max_scaler:", min_max_scaler(values))
    print("standardize:", standardize(values))


if __name__ == "__main__":
    main()
