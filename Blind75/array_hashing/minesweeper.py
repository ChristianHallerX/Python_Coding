"""
529 Minesweeper (medium)

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

- 'M' represents an unrevealed mine,
- 'E' represents an unrevealed empty square,
- 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and
    all 4 diagonals), digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
- 'X' represents a revealed mine.

You are also given an integer array 'click' where click = ['clickr', 'clickc'] represents the next click position among
all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

- If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
- If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its
    adjacent unrevealed squares should be revealed recursively.
- If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
    representing the number of adjacent mines.
- Return the board when no more squares will be revealed.
"""


def countAdjacentMines(board, click):
    x, y = click
    mines = 0

    for row in range(x - 1, x + 2):
        for col in range(y - 1, y + 2):
            # check if position is on the board (click could at edge of board) and is a MINE
            if (
                (row >= 0)
                and (row < len(board))
                and (col >= 0)
                and (col < len(board[0]))
                and (board[row][col] == "M")
            ):
                mines += 1
    return mines


def updateBoard(board, click):
    """
    Do exactly one step, one click!
    Heavy lifting is the recursive revealing of empty fields and giving mine number.
    Time Complexity: O(rows * cols) worst case: no mines -> visit each cell, constant time at each cell
    Space Complexity: O(rows * cols) due to recursion stack
    """
    if not board:
        return board

    x, y = click

    # Case 1. Found mine
    if board[x][y] == "M":
        board[x][y] = "X"

    elif board[x][y] == "E":
        # Count number of adjacent mines
        mines = countAdjacentMines(board, click)

        # Case 2.1 Write number of adjacent mines if >0
        if mines:
            board[x][y] = str(mines)

        # Case 2.2 Found no adjacent mines, search recursively. Simulate clicks. Must be within bounds.
        else:
            board[x][y] = "B"
            for row in range(x - 1, x + 2):
                for col in range(y - 1, y + 2):
                    if (
                        (row >= 0)
                        and (row < len(board))
                        and (col >= 0)
                        and (col < len(board[0]))
                        and (board[row][col] != "B")
                    ):
                        # write to 'board' as a global variable
                        updateBoard(board, [row, col])

    # Case 3. click on any other, nothing happens (can be left away)
    else:
        pass

    return board


def main():
    print("example 1: click Empty field bottom left corner")
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]
    expected = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    print(
        updateBoard(board, click),
        f"\nexpected: \n{expected}\n",
    )
    print("\nexample 2: click on the Mine")
    board = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    click = [1, 2]
    expected = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "X", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    print(updateBoard(board, click), f"\nexpected: \n{expected}")


if __name__ == "__main__":
    main()
