"""
498. Diagonal Traverse (medium)

Given an 'm' * 'n' matrix 'mat', return an array of all the elements of the array in a diagonal order.
"""


def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    """
    Params:
        mat (list of lists of ints)
    Returns:
        list of ints


    Use a directional flag and an upward direction and downward direction logic.
    Special cases when hitting the upper and lower boundaries of the matrix.
    Update row/col pointers and append value to result list.

    Time complexity: O(n*m) Loop over every grid cell of the matrix once
    Space complexity: O(1), 2 pointers, one flag, and result matrix (does not count)
    """
    # Check if the matrix is empty
    if not mat or not mat[0]:
        return []

    rows, cols = len(mat), len(mat[0])  # Get the number of rows and columns
    result = []  # Init output list
    row, col = 0, 0  # Init pointers
    direction = 1  # Init direction flag as upward. 1=upward, -1=downward

    # Iterate over all matrix cells (don't need index from loop)
    for _ in range(rows * cols):

        # Append element at pointer location (first was initialized)
        result.append(mat[row][col])

        # Up/right diagonal
        if direction == 1:
            # Edge case: If we're at the last column, we can't move right; move down instead and change direction
            if col == cols - 1:
                row += 1
                # Change dir to downward
                direction = -1
            # Edge case: If we're at the top row, we can't move upward; move right instead and change direction
            elif row == 0:
                col += 1
                # Change dir to downward
                direction = -1
            # Normal case: Move diagonally upward (up one row and right one column)
            else:
                row -= 1
                col += 1

        # Down/left diagonal
        else:
            # Edge case: If we're at the bottom row, we can't move down; move right instead and change direction
            if row == rows - 1:
                col += 1
                # Change dir to upward
                direction = 1
            # Edge case: If we're at the first column, we can't move left; move down instead
            elif col == 0:
                row += 1
                # Change dir to upward
                direction = 1
            # Normal case: Move diagonally downward (down one row and left one column)
            else:
                row += 1
                col -= 1

    return result


def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(findDiagonalOrder(mat), "expected: [1,2,4,7,5,3,6,8,9]")

    mat = [[1, 2], [3, 4]]
    print(findDiagonalOrder(mat), "expected; [1,2,3,4]")


if __name__ == "__main__":
    main()
