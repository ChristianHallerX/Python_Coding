"""
Write a simple python function that takes as input a 4x4 matrix and a 3x3 filter and computes the values
of the output matrix after applying the conv2D function, stride of 1
"""

import numpy as np

# Correct the input matrix to be 4x4 as indicated
A = np.array([[12, 13, 25, 6], [88, 26, 51, 19], [9, 77, 42, 3], [10, 20, 30, 40]])

K = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


def conv2d(matrix, kernel, padding):

    # If padding is specified, pad the matrix with zeros on all sides.
    if padding > 0:
        matrix = np.pad(
            matrix, ((padding, padding), (padding, padding)), mode="constant"
        )

    m_rows, m_cols = matrix.shape
    k_rows, k_cols = kernel.shape

    output_rows = m_rows - k_rows + 1
    output_cols = m_cols - k_cols + 1

    output = np.zeros((output_rows, output_cols))

    for i in range(output_rows):
        for j in range(output_cols):
            # Extract the 3x3 region of interest (ROI)
            roi = matrix[i : i + k_rows, j : j + k_cols]
            # Multiply the ROI element-wise with the kernel and sum all values
            output[i, j] = np.sum(roi * kernel)

    return output


result = conv2d(A, K, 0)
print(result)

print("expected: \n[[-99. 143.],\n[288.  49.]]")
