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

    Brute force both pointers with two nested loops, Time Complexity O(n2). Exceeds LeetCode time limit.
    """
    result = 0

    # Brute force both pointers
    for left in range(len(height)):
        for right in range(len(height)):
            # Horizontal distance (distance of left-right) times lower height
            area = (right - left) * min(height[left], height[right])
            # Update max area
            result = max(area, result)
    return result


def maxArea(height: list[int]) -> int:
    """
    Two pointer problem.
    Calculate area, then only shift the pointer with lower height, higher height pointer remains.
    If both heights are equal, we could update either pointer, in this case always left.
    Time complexity O(n).
    """

    result = 0

    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)

        # update pointers
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return result


def main():
    print(maxAreaNsquared(height=[1, 1]), "expected 1")
    print(maxAreaNsquared(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), "expected 49")

    print(maxArea(height=[1, 1]), "expected 1")
    print(maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), "expected 49")


if __name__ == "__main__":
    main()
