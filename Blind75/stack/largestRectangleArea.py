"""
84. Largest Rectangle in Histogram (hard)

Given an array of integers 'heights' representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
"""


def largestRectangleArea(heights: list[int]) -> int:
    return None


def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(largestRectangleArea(heights), "expected: 10")

    heights = [2, 4]
    print(largestRectangleArea(heights), "expected: 4")


if __name__ == "__main__":
    main()
