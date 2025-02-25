"""
289. Game of Life (Medium)

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970."

The board is made up of an 'm' * 'n' grid of cells, where each cell has an initial state:
 - live (represented by a 1) or
 - dead (represented by a 0).

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four
rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in
the current state of the 'm' * 'n' grid 'board'. In this process, births and deaths occur simultaneously.

Given the current state of the 'board', update the 'board' to reflect its next state.

Note that you do not need to return anything.
"""


def gameOfLife(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    1 - remains alive if two or three 1's surrounding it else dies
    0 - comes alive if three 1's surrounding it else remains dead

    Option 1: with extra memory
    Write results to temp board, then overwrite original board.
    Time Complexity: O(n*m) evaluate each cell once
    Memory Complexity: O(n*m) temp board

    Option 2: no extra memory
    How do we remember the original state AND the new state?
    Truth table with vals 0,1,2,3 that maps transitions with unique states.
     - First, map board to truth-table states based on neighbor 1's
     - Second, map truth-table state back to live/dead vals
     Time Complexity: O(2* n*m) -> O(n*m) evaluate each cell twice
     Memory Complexity: O(1)

    ### Truth Table ###
    Original | New | State
        0    |  0  |  0
        1    |  0  |  1
        0    |  1  |  2
        1    |  1  |  3
    """
    ROWS, COLS = len(board), len(board[0])

    # Helper function
    def countNeighbors(row, col):
        """
        Return count of 1's in the surrounding 8 neighbors
        """
        nei = 0
        # Start iterating in top left corner
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                #  Skip center and skip pos/neg out of bounds
                if (i == row and j == col) or i < 0 or j < 0 or i == ROWS or j == COLS:
                    continue
                if board[i][j] in [1, 3]:
                    nei += 1
        return nei

    # Map Original 0,1 to truth-table states
    for row in range(ROWS):
        for col in range(COLS):
            nei = countNeighbors(row, col)

            # Original 1 cell
            if board[row][col]:
                # 1 -> 1 = State 3
                if nei in [2, 3]:
                    board[row][col] = 3
                # 1 -> 0 = State 1, no need to process

            # Original 0 cell
            else:
                # 0 -> 1 state 2
                if nei == 3:
                    board[row][col] = 2
                # 0 -> 0 = State 0, no need to process

    # Map truth-table states to New 0,1
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] in [0, 1]:
                board[row][col] = 0
            elif board[row][col] in [2, 3]:
                board[row][col] = 1

    return None


def main():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    gameOfLife(board)
    print(board, "expected: [[0, 0, 0],[1, 0, 1],[0, 1, 1],[0, 1, 0]]")

    board = [[1, 1], [1, 0]]
    gameOfLife(board)
    print(board, "expected: [[1, 1],[1, 1]]")


if __name__ == "__main__":
    main()
