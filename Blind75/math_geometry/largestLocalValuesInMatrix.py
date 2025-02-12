"""
2373. Largest Local Values in a Matrix (Easy) should be Medium

You are given an 'n' * 'n' integer matrix 'grid'.

Generate an integer matrix 'maxLocal' of size (n - 2) x (n - 2) such that:

- maxLocal[i][j] is equal to the largest value of the 3 * 3 matrix in grid centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in 'grid'.

Return the generated matrix.
"""


def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    """
    Manually write Computer Vision max pooling.
    Output matrix has one less layer (two fewer rows and cols)
    Each output cell is the largest value of a 3x3 matrix around it (extra layer). Can't go out of bounds.
    Two outer loops (row loop, col loop) to go over output cells,
    Two inner loops (row loop, col loop) to find the largest number in 3x3 matrix surrounding each output cell.

    Time complexity: O(n**2) to go over inner layer grid cells, O(n**2) for 3x3 cells. Total: O(n**4)
    Brute force, no speedup works
    """
    n = len(grid)
    # init an output list of lists
    result = [[0] * (n - 2) for _ in range(n - 2)]

    # 'grid' row
    for i in range(n - 2):
        # 'grid' col
        for j in range(n - 2):
            # 3x3 row
            for row in range(i, i + 3):
                # 3x3 col
                for col in range(j, j + 3):
                    # Write the largest value to the output array.
                    # Compare the current largest value with the current 3x3 grid cell value
                    result[i][j] = max(result[i][j], grid[row][col])
    return result


def main():
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    print(largestLocal(grid), "expected: [[9, 9], [8, 6]]")

    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(largestLocal(grid), "expected: [[2,2,2],[2,2,2],[2,2,2]]")


if __name__ == "__main__":
    main()
