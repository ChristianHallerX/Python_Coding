"""
73. Set Matrix Zeroes (Medium)

Given an 'm' * 'n' integer matrix 'matrix', if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    return None


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    print(matrix, "expected: [[1, 0, 1],[0, 0, 0],[1, 0, 1]]")

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix)
    print(matrix, "expected: [[0, 0, 0, 0],[0, 4, 5, 0],[0, 3, 1, 0]]")


if __name__ == "__main__":
    main()
