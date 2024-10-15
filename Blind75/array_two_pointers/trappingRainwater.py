"""
42. Trapping Rain Water (Hard)

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""


def trapSpaceN(height: list[int]) -> int:
    """
    Calculate for each index how much vertical water can be trapped vertically above it. Sum up all volume.
    A water trap requires boundaries on both sides.
    Starting from a center index, find peaks left/right -> max(left), max(right).
    Get minimum height of the two peaks (bottleneck) and subtract current index
    height = water vol. min(left, right) - index_height
    Negative volume = no water.
    Time complexity: O(n)
    Space complexity: O(3n) store max height and min(l,r) in lists
    """
    maxLeft = []
    maxRight = []

    return 6


def trapSpace1(height: list[int]) -> int:
    """
    Trick: Pre-computing max height is not needed and the corresponding max on the opposite side is good.
    Start pointers on left and right ends.
    Shift the pointer with smaller max value. If equal, shift left.
    Take the minimum of the two pointers and subtract index height.
    Time complexity: O(n)
    Space complexity: O(1) two pointers, two max, and result
    """
    if not height:
        return 0

    # Init pointers and max heights
    leftPointer = 0
    rightPointer = len(height) - 1
    leftMax = height[0]
    rightMax = height[-1]
    # Water volume summed up
    result = 0

    # While they do not cross, shift pointers from outside to inside
    while leftPointer < rightPointer:
        # Shift pointer with smaller height and update max height
        if leftMax < rightMax:
            leftPointer += 1
            # Doing max first, avoids adding negatives to result
            leftMax = max(leftMax, height[leftPointer])
            # Calc volume@ pointer and add to result
            result += leftMax - height[leftPointer]
        else:
            # Shift right pointer toward left
            rightPointer -= 1
            # Doing max first, avoids adding negatives to result
            rightMax = max(rightMax, height[rightPointer])
            # Calc volume@ pointer and add to result
            result += rightMax - height[rightPointer]

    return result


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapSpace1(height), "expected: 6")

    height = [4, 2, 0, 3, 2, 5]
    print(trapSpace1(height), "expected: 9")


if __name__ == "__main__":
    main()
