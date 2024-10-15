"""
1762. Buildings With an Ocean View (medium) META

There are 'n' buildings in a line. You are given an integer array 'heights' of size 'n' that represents the heights of
the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without
obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
"""


def findBuildings(heights: list[int]) -> list[int]:
    maxHeight = 0
    result = []

    # Iterate over heights in reverse (right to left)
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > maxHeight:
            # If the previous height was lower, add the index
            result.append(i)
            # Update the heights variable with the current height
            maxHeight = max(maxHeight, heights[i])

    return result[::-1]


def main():
    heights = [4, 2, 3, 1]
    print(findBuildings(heights), "expected: [0, 2, 3]")

    heights = [4, 3, 2, 1]
    print(findBuildings(heights), "expected: [0, 1, 2, 3]")

    heights = [1, 3, 2, 4]
    print(findBuildings(heights), "expected: [3]")

    heights = [2, 2, 2, 2]
    print(findBuildings(heights), "expected: [3]")


if __name__ == "__main__":
    main()
