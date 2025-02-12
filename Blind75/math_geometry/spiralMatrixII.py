"""
59. Spiral Matrix II (medium)

Given a positive integer 'n', generate an 'n' * 'n' matrix filled with elements from 1 to n**2 in spiral order.

123
894
765
"""


def generateMatrix(n):
    """
    Params:
        n (int):    edge length of matrix
    Returns:
        list of lists with integers

    Fill in concentric layer clockwise with while loop.
    Use 4 pointers: left, right, top, bottom.
    While loop to fill in one layer:
        1 left->right, increment left pointer until equal right, manually increment top by one
        2 top->bottom, increment top pointer until equal bottom, manually decrement right by one
        3 right->left, decrement right pointer until equal left, manually decrement bottom by one
        4 bottom->top, decrement bottom pointer until equal top, manually increment left by one
        5 increment left by one (move to inner square) and restart.

    Exit loop when both pointers are over cross (i.e, l<r and t<b)

    Time Complexity: O(n**2), iterating once over n*n matrix.
    Memory Complexity: O(1), matrix output does not count and pointers
    """
    # init matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    left, right = 0, n - 1
    top, bottom = 0, n - 1
    value = 1

    # fill in while not over cross, one iteration = one layer
    while left <= right:
        # fill in top row (left->right)
        for col in range(left, right + 1):
            matrix[top][col] = value  # top is fixed
            value += 1
        top += 1

        # fill in right col (top->bottom)
        for row in range(top, bottom + 1):
            matrix[row][right] = value  # right is fixed
            value += 1
        right -= 1

        # fill in bottom row (right->left), reverse range
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = value  # bottom is fixed
            value += 1
        bottom -= 1

        # fill in left col (bottom->top)
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = value
            value += 1
        left += 1

    return matrix


def main():
    n = 3
    print(generateMatrix(n), "expected: [[1,2,3],[8,9,4],[7,6,5]]")

    n = 1
    print(generateMatrix(n), "expected: [[1]]")


if __name__ == "__main__":
    main()
