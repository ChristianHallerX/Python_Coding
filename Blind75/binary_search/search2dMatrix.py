"""
74. Search a 2D Matrix (medium)

You are given an 'm' * 'n' integer matrix 'matrix' with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer 'target', return 'True' if 'target' is in matrix or 'False' otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Double binary search:
    Do binary search in which row to search, then regular binary search in row.
    Time complexity: log*m + log*n
    """
    ROWS = len(matrix)
    COLS = len(matrix[0])

    # 1 Binary search on rows. Init row pointers
    topRow = 0
    botRow = ROWS - 1
    while topRow <= botRow:
        middleRow = (topRow + botRow) // 2

        # Target larger than last value in middle row! Move down
        if target > matrix[middleRow][-1]:
            topRow = middleRow + 1
        # Target smaller than first value of middle row! Move up
        elif target < matrix[middleRow][0]:
            botRow = middleRow - 1
        # Target is in middle row
        else:
            break

    # while loop stopped and pointers crossed -> target not found -> return False
    if not (topRow <= botRow):
        return False

    # 2 Binary search inside current row
    row = (topRow + botRow) // 2
    left = 0
    right = COLS - 1

    while left <= right:
        middle = (left + right) // 2
        # Search towards right
        if target > matrix[row][middle]:
            left = middle + 1
        # Search towards left
        elif target < matrix[row][middle]:
            right = middle - 1
        # Target is at middle
        else:
            return True

    # Never found target
    return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target), "expected: True")

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(searchMatrix(matrix, target), "expected: False")


if __name__ == "__main__":
    main()
