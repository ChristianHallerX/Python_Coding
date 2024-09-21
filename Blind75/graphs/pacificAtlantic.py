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

# Accept a height map of an island, Return a list of grid coordinates on the island (diagonal crest)
# from which water flows towards both oceans -> have lower heights than cells NW and SE.


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:

    return result


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
