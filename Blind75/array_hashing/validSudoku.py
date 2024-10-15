"""
36. Valid Sudoku (medium)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

import collections


def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Use hash map for rows, cols, squares.
    Rows/cols index 0-8
    Squares index 0-2 (by integer division modulo by 3). key(row // 3,col // 3): val(set)
    Time complexity: O(9^2) iterate over entire grid
    Space complexity: O(9^2) 3 hash sets
    """
    # Dictionaries with new value automatically contains emtpy set
    # key(row, col, or square index): value(set of board vals)
    colsDict = collections.defaultdict(set)
    rowsDict = collections.defaultdict(set)
    squaresDict = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            # Skip empty values
            if board[row][col] == ".":
                continue
            # Catch the false/duplicates
            # If this grid value is already in the rowDict current row (duplicate), colDict, or squareDict
            if (
                board[row][col] in rowsDict[row]
                or board[row][col] in colsDict[col]
                or board[row][col] in squaresDict[(row // 3, col // 3)]
            ):
                return False
            # Add number to sets in dicts
            colsDict[col].add(board[row][col])
            rowsDict[row].add(board[row][col])
            squaresDict[(row // 3, col // 3)].add(board[row][col])
    # If no False were triggered, return True
    return True


def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(isValidSudoku(board), "expected: True")

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(isValidSudoku(board), "expected: False")


if __name__ == "__main__":
    main()
