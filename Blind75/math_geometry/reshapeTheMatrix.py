"""
566. Reshape the Matrix (easy)

In MATLAB, there is a handy function called reshape which can reshape an 'm' * 'n' matrix into a new one with
a different size 'r' * 'c' keeping its original data.

You are given an 'm' * 'n' matrix 'mat' and two integers 'r' and 'c' representing the number of rows and the number
of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order
as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.
"""


def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    # m = orig cols, n = orig rows
    m, n = len(mat), len(mat[0])

    # Number of values in old and new matrix have to match. Else return original
    if m * n != r * c:
        return mat

    # Create a flat list version of the original matrix (list of lists) that is easier to slice into new shapes
    flat = [num for row in mat for num in row]

    # Init output matrix
    reshaped = []

    # Cut new rows from the reshaped list and append to output
    for row in range(r):

        # Calc start and end idx of row
        start_idx = row * c
        end_idx = start_idx + c

        # Slice row using the idx and append to output
        reshaped.append(flat[start_idx:end_idx])

    return reshaped


def main():
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(matrixReshape(mat, r, c), "expected: [[1,2,3,4]]")

    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    print(matrixReshape(mat, r, c), "expected: not legal, original [[1,2],[3,4]]")


if __name__ == "__main__":
    main()
