"""
Tetris (CodeSignal 2d Array Demo)

You are given a matrix of integers 'field' of size 'height' × 'width' representing a game field, and also a matrix
of integers 'figure' of size 3 * 3 representing a figure.
Both matrices contain only 0s and 1s, where 1 means that the cell is occupied, and 0 means that the cell is free.

You choose a position at the top of the game field where you put the figure and then drop it down.
The figure falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell,
which blocks it from falling further.
After the 'figure' has stopped falling, some of the rows in the field may become fully occupied.

--> Your task is to find the dropping position such that at least one full row is formed (Tetris).
As a dropping position, you should return the column index of the cell in the game field which matches the top left
corner of the 'figure'’s 3 * 3 matrix.
- If there are multiple dropping positions satisfying the condition, feel free to return any of them.
- If there are no such dropping positions, return -1.

Note: The figure must be dropped so that its entire 3 * 3 matrix fits inside the field, even if part of the matrix
is empty.
"""


def tetris(field, figure):
    """
    Go though columns. Check if figure can be placed at coordinates, then check lower row.
    If loop not broken, then create field copy, write figure into field and check for complete rows.
    Return a column index that fits the figure and has a row with all 1s

    Time Complexity: outer loop O(n),
                    dropping O(m),
                    checking O(1) constant 9 fields,
                    copy field and 1-check O(m*n)
                    -> Total O(m*n2)
    Space Complexity: copy of field O(m * n)
    """
    height = len(field)
    width = len(field[0])

    # Helper checks if figure position can be placed without colliding
    def canPlace(r, c):
        """
        Return false if 'field' and 'figure' are both 1 in once cell (overlap, can't place)
        Return True if only 'field' or 'figure' is 1
        """
        for i in range(3):
            for j in range(3):
                # Only check cells that are part of the figure.
                if figure[i][j] == 1:
                    if field[r + i][c + j] == 1:
                        return False
        return True

    # Loop over columns. The figure's top-left must be max 3 cols from right edge of the field
    for col in range(0, width - 3 + 1):
        r = 0  # init top row for dropping

        # Simulate dropping the figure in this col position using the candidate row
        while True:
            candidate_r = r + 1
            # Break if the figure boundaries are outside the field boundaries
            if candidate_r + 3 > height:
                break
            # Check if we can move the figure down by one row. Else break loop in this column
            if not canPlace(candidate_r, col):
                break
            r = candidate_r  # drop one row

        # Figure can be placed in this column
        # Create a copy of the field
        new_field = [row[:] for row in field]

        # Write the figure into the field
        for i in range(3):
            for j in range(3):
                if figure[i][j] == 1:
                    new_field[r + i][col + j] = 1

        # Check if any row in new_field is completely filled with 1's and return the col index
        for row_line in new_field:
            if all(cell == 1 for cell in row_line):
                return col

    # Fail, no col found
    return -1


def main():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]]
    figure = [[0, 0, 1], [0, 1, 1], [0, 0, 1]]
    print(tetris(field, figure), "expected: 0")

    field = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    figure = [[1, 1, 1], [1, 0, 1], [1, 0, 1]]
    print(tetris(field, figure), "expected: 2")

    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 0, 1]]
    figure = [[1, 1, 0], [1, 0, 0], [1, 0, 0]]
    print(tetris(field, figure), "expected: -1")


if __name__ == "__main__":
    main()
