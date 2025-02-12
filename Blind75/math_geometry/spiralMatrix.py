"""
54. Spiral Matrix I (medium)

Given an 'm' * 'n' 'matrix', return all elements of the 'matrix' in spiral order.
"""


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """
    Params:
        matrix (list of lists with ints)    contains random values
    Returns:
        matrix (list with ints)    spiral ordered values appended to single list

    Clip the values out of the input matrix and append them to a flat output list

    Similar to rotate matrix, but directly updating boundaries. Layers are updated automatically
    Left, right, bottom, top pointers need updating after each corner.
    Update boundaries for top/bottom/left/right and chop off to make matrix smaller

    Time complexity: O(m * n) visit each grid cell once
    Space complexity: O(1), no extra variables beyond output
    """
    # Initialize pointers
    left = 0
    # Define index right outside of bounds, which is convenient for the range(), but need to adjust when slicing value
    right = len(matrix[0])
    top = 0
    # Define bottom outside of bounds, which is convenient for range()
    bottom = len(matrix)

    result = []

    while left < right and top < bottom:
        # Loop through columns in the top row
        for col in range(left, right):
            result.append(matrix[top][col])  # top row pointer fixed
        # Shift top row down to avoid overwriting
        top += 1

        # Loop through rows. Remember to adjust right pointer
        for row in range(top, bottom):
            result.append(matrix[row][right - 1])  # right col pointer fixed
        # Shift row to the left to avoid overwriting
        right -= 1

        # Pointer check at bottom right. Unsure why.
        if not (left < right and top < bottom):
            break

        # Loop through cols in the bottom row.
        for col in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][col])  # bottom row pointer fixed
        bottom -= 1

        # Get every i in the left column, iterate reverse
        for row in range(bottom - 1, top - 1, -1):
            result.append(matrix[row][left])  # left col pointer fixed
        left += 1

    return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix), "expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]")

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralOrder(matrix), "expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]")

    matrix = [[2, 5, 8], [4, 0, -1]]
    print(spiralOrder(matrix), "expected: [2, 5, 8, -1, 0, 4]")


if __name__ == "__main__":
    main()
