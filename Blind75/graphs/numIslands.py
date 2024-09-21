"""
200. Number of Islands (medium)

Given an m*n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically (not diagonally).

You may assume all four edges of the grid are all surrounded by water.
"""

import collections


def numIslands(grid: list[list[str]]) -> int:
    """
    Visit each grid cell and if it's an island, run iterative Breadth First Search BFS on surrounding coordinates.
    If the current coordinate hits an island, the whole island's coordinates are mapped and marked as 'visited'.
    Spread the BFS across land with while-loop and a queue (python deque).
    Time complexity: O(n*n * BFS)
    """
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    # Counter for islands
    result = 0

    def bfs(row, col):
        """
        global vars 'visited' and 'ROWS', 'COLS'
        Gets run once per island
        """
        # Set with coordinates, global variable
        visited.add((row, col))

        q = collections.deque()
        # Start q with current grid coordinates
        q.append((row, col))

        # While loop picks coords from q and adds neighbor coords to queue and marks as visited.
        while q:
            row, col = (
                q.popleft()
            )  # regular pop on the right would make it an iterative DFS
            # up, down, right, left
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for drow, dcol in directions:
                if (
                    (row + drow) in range(ROWS)  # Direction in bounds?
                    and (col + dcol) in range(COLS)  # Direction in bounds?
                    and grid[row + drow][col + dcol] == "1"  # Land?
                    and (row + drow, col + dcol) not in visited
                ):
                    q.append((row + drow, col + dcol))
                    visited.add((row + drow, col + dcol))

    # Start BFS from each grid coordinate
    for row in range(ROWS):
        for col in range(COLS):
            # Only proceed if current coordinate is island and NOT already visited in previous iteration
            # i.e., only runs on an island the first visit
            if grid[row][col] == "1" and (row, col) not in visited:
                # BFS adds current island coordinates to 'visited'
                bfs(row, col)
                result += 1

    return result


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(numIslands(grid), "expected: 1")

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(numIslands(grid), "expected: 3")


if __name__ == "__main__":
    main()
