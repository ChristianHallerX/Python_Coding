"""
994. Rotting Oranges (Medium)

You are given an 'm' * 'n' grid where each cell can have one of three values:

- 0 representing an empty cell
- 1 representing a fresh orange
- 2 representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.
"""

from collections import deque


def orangesRotting(grid: list[list[int]]) -> int:
    """
    BFS with a deque (queue) started from each rotten orange at start.
    Append adjacent oranges to deque on right. Pop starter oranges on left.
    Time Complexity: O(n * m) dim of grid
    Space Complexity: O(n * m) worst queue
    """
    q = deque()
    # init time steps and count of fresh oranges (return -1 if fresh >0)
    time, fresh = 0, 0

    # init grid size
    ROWS, COLS = len(grid), len(grid[0])

    # Single initial survey of fresh and rotten oranges in grid into q
    for row in range(ROWS):
        for col in range(COLS):
            # found a fresh orange
            if grid[row][col] == 1:
                fresh += 1
            # found a rotten orange -> append to q
            if grid[row][col] == 2:
                q.append([row, col])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # Start time steps
    while q and fresh > 0:
        # Iterate over oranges currently on q
        for i in range(len(q)):
            # Get the coordinates of current rotten orange and pop left from q
            row, col = q.popleft()

            # Check four directions around rotten orange
            for diff_row, diff_col in directions:

                # Combine center grid with one of the four direction diffs
                row_, col_ = diff_row + row, diff_col + col

                # Make sure this diff is in bounds of grid and fresh orange
                if (
                    row_ < 0
                    or row_ == len(grid)
                    or col_ < 0
                    or col_ == len(grid[0])
                    or grid[row_][col_] != 1
                ):
                    continue
                # Overwrite fresh orange with rotten orange
                grid[row_][col_] = 2

                # Append rotten orange to q for next time step
                q.append([row_, col_])

                # Decrement count of fresh oranges
                fresh -= 1
        # Increment one time step
        time += 1

    # Return the time steps taken of no fresh oranges remaining
    return time if fresh == 0 else -1


def main():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(orangesRotting(grid), "expected: 4")

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(orangesRotting(grid), "expected: -1")

    grid = [[0, 2]]
    print(orangesRotting(grid), "expected: 0")

    grid = [[1], [2], [1], [2]]
    print(orangesRotting(grid), "expected: 1")


if __name__ == "__main__":
    main()
