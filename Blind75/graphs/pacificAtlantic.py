"""
417. Pacific Atlantic Water Flow (medium)

There is an 'm' * 'n' rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and
bottom edges.

The island is partitioned into a grid of square cells. You are given an 'm' * 'n' integer matrix heights where
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and
west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell
(ri, ci) to both the Pacific and Atlantic oceans.
"""


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    """
    Accept a height map of an island, Return a list of grid coordinates on the island (diagonal crest)
    from which water flows towards both oceans -> crest neighbors have lower heights than NW and SE.

    Brute force: for each grid cell, start a DFS search (which is repeated for each starting point)
    and if successful, add to results set.
    Time complexity: O(n*m)^2

    Smarter solution: Every cell bordering Pacific can flow to Pacific. Every cell bordering Atlantic flows to Atlantic.
    Find all non-coast cells that flow to Pacific edge. Find increasing heights and maintain a set to avoid duplicates.
    Find all non-coast cells that flow to Atlantic edge. Find increasing heights and maintain a set to avoid duplicates.
    Find overlap both sets of cells that can reach both.
    Time complexity: O(n*m)
    """
    # Init global vars
    ROWS, COLS = len(heights), len(heights[0])
    # Init sets for coordinate results, global vars
    pacset, atlset = set(), set()

    # Define DFS recursive function
    def dfs(row, col, visitSet, prevHeight):
        """
        Marking cell coordinates in visitSet moving uphill
        """

        # Do not write to visitSet when....
        if (
            ((row, col) in visitSet)  # Previously visited
            or (row < 0 or col < 0)  # Out of bounds negative
            or (row == ROWS or col == COLS)  # Out of bounds positive
            or (heights[row][col] < prevHeight)
        ):  # Height smaller, i.e., not equal or higher (we move from coast upwards)
            return None

        # Coordinates passed the if statement, add coordinates to visitSet
        visitSet.add((row, col))

        # Recursive call on four coordinate directions
        dfs(row=row + 1, col=col, visitSet=visitSet, prevHeight=heights[row][col])  # up
        dfs(row=row - 1, col=col, visitSet=visitSet, prevHeight=heights[row][col])  # do
        dfs(row=row, col=col - 1, visitSet=visitSet, prevHeight=heights[row][col])  # lf
        dfs(row=row, col=col + 1, visitSet=visitSet, prevHeight=heights[row][col])  # ri

    # Run DFS on top edge row=0's cells (Pacific) and last row's cells (Atlantic), move left/right
    # Initial 'prevHeight' coordinates are the same as starting coordinate
    for col in range(COLS):
        dfs(
            row=0, col=col, visitSet=pacset, prevHeight=heights[0][col]
        )  # top row fixed
        dfs(
            row=ROWS - 1, col=col, visitSet=atlset, prevHeight=heights[ROWS - 1][col]
        )  # bottom row fixed

    # Run DFS on left edge col=0' cells (Pacific) and right edge cells (Atlantic), move up/down
    # Initial 'prevHeight' coordinates are the same as starting coordinate
    for row in range(ROWS):
        dfs(
            row=row, col=0, visitSet=pacset, prevHeight=heights[row][0]
        )  # left col fixed
        dfs(
            row=row, col=COLS - 1, visitSet=atlset, prevHeight=heights[row][COLS - 1]
        )  # right col fixed

    # Return overlap between pacset and atlset as list.
    # The individual coordinate pairs are tuples instead of lists, which is also accepted.
    # Order of coordinates also does not matter.
    return list(pacset & atlset)


def main():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(
        pacificAtlantic(heights),
        "expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]",
    )

    heights = [[1]]
    print(pacificAtlantic(heights), "expected: [[0, 0]]")


if __name__ == "__main__":
    main()
