"""
73. Set Matrix Zeroes (Medium)

Given an 'm' * 'n' integer matrix 'matrix', if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    Do not iterate through all grid cells O(n * m) * 3.
    Challenge: Time complexity is fixed, but reduce space complexity.
    Bad Solution:
        Time comp O(n * m)
        Memory: O(n * m) copy of matrix
        Operate on a copy of the matrix -> uses memory, read from the original. Iterate over all cells individually.
    Good Solution:
        Time comp O(n + m) * 3
        Memory comp: O(n + m) two lists
        Use list of cols, list of rows. Mark in these lists if there is a 0 and the row/col needs to be set to 0.
        Next, loop through note lists and write whole rows/cols to 0.
    Best Solution
        Time comp: O(n * m) * 3
        Memory comp: constant O(1) mark in first row col, and use extra var for [0][0]
        Only one single extra variable needed.
        Iterate though cells, mark the left column and top row 0 if a 0 was detected in the row/col.
        Use extra space for row/col overlap in top left corner.
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    # Extra bool variable to avoid overlap of markings at [0][0].
    # Stands as extension for col one as marker if first row needs to be zeroed.
    # The cell [0][0] itself will be used for row one and mark for col one
    rowZero = False

    # Determine which rows and cols need to be zeroed, read all cells and mark first row/col
    for r in range(ROWS):
        for c in range(COLS):
            # Iterate through all positions
            if matrix[r][c] == 0:
                # Mark row 0 cells to zero if detected
                matrix[0][c] = 0

                # Mark col 0 cells to zero if detected, but spare row 0 to avoid overlap/overwrite (use var rowZero)
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    # Loop through second and onward rows and cols, Read markings in first col/row and write zero in matrix
    for r in range(1, ROWS):
        for c in range(1, COLS):
            #  Read from first col/row by manually indexing into first and set 0
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # Read [0][0] markings and write first col zero
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    # Read bool and write first row zero
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0

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
