"""
Standardize 2d Array

We often need to standardize data prior to using it in any ML or DS tasks.
Complete the function that which standardizes data stored in NumPy arrays.
"""

import numpy as np


def standardize_data(arr):
    # Compute the mean and standard deviation for each row
    mean = np.mean(arr, axis=1, keepdims=True)
    std = np.std(arr, axis=1, keepdims=True)

    # Standardize each row
    standardized_data = (arr - mean) / std
    return standardized_data


arr = np.array([[1.2, -0.3, 1.3], [1.2, 2.0, 0.3]])
result = standardize_data(arr)

print(
    "expected:\n[[ 0.63786253 -1.41201131  0.77414878]\n[ 0.64806154  1.20008344 -1.24883994]]\n"
)
print(result)
