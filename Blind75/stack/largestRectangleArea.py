"""
84. Largest Rectangle in Histogram (hard)

Given an array of integers 'heights' representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
"""


def largestRectangleArea(heights: list[int]) -> int:
    """
    Create index: height stack
    Create maxArea var
    Add new value to stack. Calc max area on single-column.
    Add new value. If new top-of-stack value is lower than bottom value, pop the old value. add old index and new hight.
    Final loop over stack pairs left that end all the way to the end of the histogram.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    maxArea = 0
    # stack will hold pairs (index, height)
    stack = []

    for i, h in enumerate(heights):
        start = i
        # if top stack height is larger than current height
        while stack and stack[-1][1] > h:
            # 1 pop stack
            index, height = stack.pop()
            # 2 check max rectangle between current index i and popped stack's 'index'
            maxArea = max(maxArea, height * (i - index))
            start = index

        # 3 extend current height backwards. Write the modified pair to the stack
        stack.append((start, h))

    # Entries in the stack left, width uses updated widths, subtracted by start value i
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea(heights), "expected: 10")

    heights = [2, 4]
    print(largestRectangleArea(heights), "expected: 4")


if __name__ == "__main__":
    main()
