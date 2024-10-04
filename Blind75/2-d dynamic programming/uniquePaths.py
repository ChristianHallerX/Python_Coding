"""
62. Unique Paths (medium)

There is a robot on an 'm' * 'n' grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner marked 'Finish' in the diagram below (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time (no diagonal).

Given the two integers 'm' and 'n', return the number of possible unique paths that the robot can take
to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


def uniquePaths(m: int, n: int) -> int:
    """
    Calculate unique ways to get to finish for each cell and cache.
    Populate the ways for each cell: the further to the left and up, the more ways. Most unique ways at start.
    Robot only moves down or right!! On bottom row, move only right (1), on right, move only down (1).
    Sum of down and right cells at start. ()
    Base case = 1 path
    Time complexity: O(n * m)
    Memory complexity: O(n)
    """

    # Define bottom row (can only move right)
    row = [1] * n

    # Calculate values for new rows above old row (-1 because the first one already exists). Only keep the top row.
    for i in range(m - 1):
        # Initialize row
        newRow = [1] * n

        # Reverse loop over new row values, start at second to last position (remains 1, only down possible)
        for j in range(n - 2, -1, -1):
            # Sum right value and bottom value
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow

    # After looping from bottom to top, the top left  (row[0])is the start value with the unique paths value
    return row[0]


def main():
    m = 3
    n = 7
    print(uniquePaths(m, n), "expected: 28")

    m = 3
    n = 2
    print(uniquePaths(m, n), "expected: 3")


if __name__ == "__main__":
    main()
