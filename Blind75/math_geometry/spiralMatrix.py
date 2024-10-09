"""
54. Spiral Matrix (medium)

Given an 'm' * 'n' 'matrix', return all elements of the 'matrix' in spiral order.
"""


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """
    Similar to rotate matrix, but directly updating boundaries. Layers are updated automatically
    Kind of unraveling 2-d matrix to 1-d list.
    Left, right, bottom, top pointers need updating after each corner.
    Update boundaries for top/bottom/left/right and chop off to make matrix smaller
    Time complexity: O(m*n) visit each grid cell once
    Space complexity: O(1) no extra variables beyond output
    """
    # Pointers are dimensions of matrix for iteration with range()
    left = 0
    # Define index right outside of bounds, which is convenient for the range(), but need to adjust when slicing value
    right = len(matrix[0])
    top = 0
    # Define index below outside of bounds, which is convenient for range()
    bottom = len(matrix)

    result = []

    while left < right and top < bottom:
        # Get every i in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        # Shift top row down
        top += 1

        # Get every i in the right column. Remember to adjust right pointer
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        # Pointer check at bottom right. Unsure why.
        if not (left < right and top < bottom):
            break

        # Get every i in the bottom row. Remember to adjust bottom pointer
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # Get every i in the left column, iterate reverse
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
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
