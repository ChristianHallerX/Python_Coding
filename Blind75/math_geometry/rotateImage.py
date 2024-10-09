"""
48. Rotate Image (medium)

You are given an 'n' * 'n' 2D 'matrix' representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
"""


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, Challenge: modify matrix in-place instead.
    Square matrix -> horizontal index is the same as rotated vertical index.
    Rotate outer layer(s) 90 degrees to the right. If odd edge length: Center cell remains in place.
    Pointers: top, bottom, left, right
    Use temporary variable to write to before writing
    Time complexity: O(n^2)
    Memory complexity: O(1), no extra matrices, in-place
    """
    # Initialize pointers at corners
    left = 0
    right = len(matrix) - 1

    # Pointers will cross over once finished
    while left < right:
        # Complete a layer of rotation. Number of iterations depends on edge length.
        # In edge length 4 we have 3 rotations (both corners are the same rotation)
        for i in range(right - left):  # 3 - 0 = 3
            # assign vertical pointers, same as horizontal
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

        right -= 1
        left += 1

    return None


def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    print(matrix1, "expected: [[7, 4, 1],[8, 5, 2],[9, 6, 3]]")

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix2)
    print(
        matrix2,
        "expected: [[15, 13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7, 10, 11]]",
    )


if __name__ == "__main__":
    main()
