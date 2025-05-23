"""
48. Rotate Image (medium)

You are given an 'n' * 'n' 2D 'matrix' representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image *in-place*, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
"""


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, Challenge: modify matrix in-place instead.
    Square matrix -> horizontal index is the same as rotated vertical index.
    Rotate outer layer(s) 90 degrees to the right. If odd edge length: Center cell remains in place.
    Pointers: top, bottom, left, right
    Use a single temp. variable to store the first old val before writing to array.
    Do rotation 90° to right, but in counter-clockwise order.

    Time complexity: O(n**2)
    Memory complexity: O(1), no extra matrices, just temp var, in-place
    """
    # Initialize pointers at corners
    left = 0
    right = len(matrix) - 1

    # Pointers will cross over once finished and loop halt. Each while-loop iteration is a matrix layer.
    while left < right:
        # Each For-loop iteration completes an index rotation. Numer of iterations depends on edge-length.
        # After all indices of layer are completed, constrict pointers to next inner layer
        for i in range(right - left):  # 3 - 0 = 3
            # Assign vertical pointers, same as horizontal in an n*n matrix
            top = left
            bottom = right

            # Progress writing in reverse direction (counter-clockwise) which requires only a single temp variable

            # Save top left to temp variable
            topLeft = matrix[top][left + i]

            # Move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top left to top right (from temp)
            matrix[top + i][right] = topLeft

        # Limit pointers to next inner layer
        right -= 1
        left += 1

    return None


def rotate_transposeRotate(matrix: list[list[int]]) -> None:
    """
    The Transpose and Reverse Rows (In-Place) algorithm is used to rotate a square matrix
    by 90 degrees clockwise.
    - First, the matrix is transposed, which means converting rows to columns.
    - Second, each row of the transposed matrix is reversed to achieve the desired rotation.
    This approach modifies the matrix in place, requiring no additional space.
    Time Complexity: O(n**2)
    Memory complexity: O(1), no extra matrices, just temp var, in-place
    """

    # Get the size of the matrix
    n = len(matrix)

    # 1. Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):

            # Swap elements to transpose
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row
    for i in range(n):

        # Reverse the current row
        matrix[i].reverse()


def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    print(matrix1, "expected: [[7, 4, 1],[8, 5, 2],[9, 6, 3]]")

    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_transposeRotate(matrix1)
    print(matrix1, "expected: [[7, 4, 1],[8, 5, 2],[9, 6, 3]]")

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix2)
    print(
        matrix2,
        "expected: [[15, 13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7, 10, 11]]",
    )
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate_transposeRotate(matrix2)
    print(
        matrix2,
        "expected: [[15, 13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7, 10, 11]]",
    )


if __name__ == "__main__":
    main()
