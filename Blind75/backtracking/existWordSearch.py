"""
79. Word Search (Medium)

Given an 'm' *  'n' grid of characters 'board' and a string 'word', return True if 'word' exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or

vertically neighboring. The same letter cell may not be used more than once.
"""


def exist(board: list[list[str]], word: str) -> bool:
    """
    No efficient solution. The brute force is Backtracking Depth First Search DFS.
    We have to start the search from each grid cell and start tracking a path of valid chars.
    Can't re-visit characters - >memorize path coordinates in set.
    We need an index moving through 'word'. and check the neighbors except for current and past characters
    Time complexity: O(n * m * dfs). Apply dfs on each board coord. DFS: 4 directions to power of length of word.
    -> O(n * m * 4^len(word))
    """
    # Dimensions of board, global var
    ROWS, COLS = len(board), len(board[0])
    # Store row/col coord tuple of current path, global var
    path = set()

    def dfs(row, col, i):
        # i = current char in target 'word'. 'row', 'col' are current coordinates on the board

        # Base case good: i reached end of 'word'-> found the word
        if i == len(word):
            return True

        # Base Case bad
        if (
            (row < 0 or col < 0)  # Board index out of bounds
            or (row >= ROWS or col >= COLS)  # Board index out of bounds
            or (
                word[i] != board[row][col]
            )  # Current word char does not match board char
            or ((row, col) in path)
        ):  # Board coordinates are on path
            return False

        # Actions when CORRECT char found on board (above stuff did not trigger)
        # Add coordinates tuple to 'path'
        path.add((row, col))

        # Run DFS in all four adjacent board coordinates with the next 'word' char
        # If any recursive function returns True, then the whole function returns True
        result = (
            dfs(row + 1, col, i + 1)  # down
            or dfs(row - 1, col, i + 1)  # up
            or dfs(row, col + 1, i + 1)  # right
            or dfs(row, col - 1, i + 1)  # left
        )
        return result

    # Brute force DFS function on every coord of grid and start at 'word' index=0
    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col, 0):
                return True
    # At no starting coordinate we made it to the end of the 'word' index. Return False
    return False


def main():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word), "expected: True")

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(exist(board, word), "expected: True")

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(exist(board, word), "expected: False")


if __name__ == "__main__":
    main()
