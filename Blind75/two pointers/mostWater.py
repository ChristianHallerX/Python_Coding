"""
11. Container With Most Water (medium)

You are given an integer array height of length 'n'. There are 'n' vertical lines drawn such that the two endpoints

of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def maxAreaNsquared(height: list[int]) -> int:
    """
    Find the largest product of index-distance (x) * height (y).
    The lower/min height of two heights is used, since the difference between lower and upper height spills over.
    Loop through all heights and keep the max.

    Brute force by looping through both heights, O(n2) - exceeds time limit
    """
    result = 0

    for index_i, i in enumerate(height):
        for index_j, j in enumerate(height):
            # lower height times distance measured in index
            this_area = min(i, j) * abs(index_i - index_j)
            # update max area
            result = max(this_area, result)
    return result


def maxArea(height: list[int]) -> int:
    """
    Find the largest product of index-distance (x) * height (y).
    The lower/min height of two heights is used, since the difference between lower and upper height spills over.
    Move two pointers once from outside to inside and keep the max. Linear time O(n).

    Do NOT sort the height list, because that would mess up the index distance.
    """
    result = 0
    left_pointer, right_pointer = 0, len(height) - 1

    # do not cross over pointers
    while left_pointer < right_pointer:
        this_area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
        result = max(this_area, result)

        # update pointers towards middle, always shift pointer with shorter height
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        elif height[right_pointer] <= height[left_pointer]:
            right_pointer -= 1

    return result


def main():
    print(maxAreaNsquared(height=[1, 1]), 'expected 1')
    print(maxAreaNsquared(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), 'expected 49')

    print(maxArea(height=[1, 1]), 'expected 1')
    print(maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), 'expected 49')


if __name__ == '__main__':
    main()
