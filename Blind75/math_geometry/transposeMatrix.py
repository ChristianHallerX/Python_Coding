"""
867. Transpose Matrix (Easy)

Given a 2D integer array 'matrix', return the transpose of 'matrix'.

The *transpose* of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.
"""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Params:
        matrix (list of lists with ints)
    Returns:
        list of lists with ints

    A non-hard coded solution will require extra space and can't operate in-place
    Row and column indices get swapped.
    Time Complexity: O(n*m) rows*cols
    Space Complexity: O(n*m) same size as matrix, just different shape. But result space may not count -> O(1)
    """
    rows_input = len(matrix)
    cols_input = len(matrix[0])
    result = [[0] * rows_input for _ in range(cols_input)]

    for row in range(rows_input):
        for col in range(cols_input):
            # result is indices reversed
            result[col][row] = matrix[row][col]
    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(m), "expected: [[1,4,7],[2,5,8],[3,6,9]]")

    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m), "expected: [[1,4],[2,5],[3,6]]")


if __name__ == "__main__":
    main()
