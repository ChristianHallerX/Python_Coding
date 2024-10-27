"""
74. Search a 2D Matrix (medium)

You are given an 'm' * 'n' integer matrix 'matrix' with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer 'target', return 'True' if 'target' is in matrix or 'False' otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    return None


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target), "expected: 3")

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(searchMatrix(matrix, target), "expected: 13")


if __name__ == "__main__":
    main()
