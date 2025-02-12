"""
766. Toeplitz Matrix (Easy)

Given an 'm' * 'n' matrix, return True if the matrix is Toeplitz. Otherwise, return False.

A matrix is Toeplitz if *every* diagonal from *top-left* to *bottom-right* has the same elements.
"""


def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    """
    Params:
        matrix (list of lists with ints)
    Returns:
        Boolean

    Inutition:  Loop over every grid cell, starting second row and second col.
                Check if each value is equal to top left value.
                Stop if unequal.
    Time Complexity:    O(m * n) over each element minus a few
    Space Complexity:   O(1) no extra data written
    """

    rows = len(matrix)
    cols = len(matrix[0])

    # Go through each row, starting from second row
    for row in range(1, rows):
        # Go through each col's values starting from second col
        for col in range(1, cols):
            # Compare the current element with its top-left neighbor
            if matrix[row][col] != matrix[row - 1][col - 1]:
                return False
    # Everything matched, loop not broken
    return True


def main():
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(isToeplitzMatrix(matrix), "expected: True")
    print(
        """
        In the above grid, the diagonals are:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
        In each diagonal all elements are the same, so the answer is True.
        """
    )

    matrix = [[1, 2], [2, 2]]
    print(isToeplitzMatrix(matrix), "expected: False")


if __name__ == "__main__":
    main()
