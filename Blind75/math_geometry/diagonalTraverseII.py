"""
1424. Diagonal Traverse II (Medium)

Given a 2D integer array 'nums', return all elements of 'nums' in diagonal order as shown in the below images.
"""


def findDiagonalOrder(nums: list[list[int]]) -> list[int]:
    """
    Hash map with diagonal indices
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    diagonalMap = {}

    # fill the diagonal map with diagIndex: [value1, value2]
    for rowIndex, row in enumerate(nums):
        for colIndex, value in enumerate(row):

            # calculate "diagonal index"
            diagonalIndex = rowIndex + colIndex

            # if diagonal index is not in the hash map, init with empty list as value
            # every grid cell in a diagonal has row+col add up to the same diagonal index. Allows for gaps in grid.
            if diagonalIndex not in diagonalMap:
                diagonalMap[diagonalIndex] = []

            # append the current grid value to the list corresponding to its diag index
            diagonalMap[diagonalIndex].append(value)

    result = []

    # Iterate over sorted keys of the map
    for diagonalIndex in sorted(diagonalMap.keys()):
        # get the values from the value list and append them all (requires 'extend' instead of 'append')
        result.extend(reversed(diagonalMap[diagonalIndex]))
    return result


def main():
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(findDiagonalOrder(nums), "expected: [1,4,2,7,5,3,8,6,9]")

    nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    print(findDiagonalOrder(nums), "expected: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]")


if __name__ == "__main__":
    main()
