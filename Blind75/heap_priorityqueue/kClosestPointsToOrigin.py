"""
973. K Closest Points to Origin (Medium)

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer 'k',
return the 'k' closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)**2 + (y1 - y2)**2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import heapq
import math


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Calculate distances as first element and dd to minHeap based on first element.
    Pop k smallest elements (automatically sorted by smallest).
    Add the x and y to an output list.
    Time Complexity: O(n) heapify
    Space Complexity: O(n), new heap only, result does not count.
    """
    # Init list of lists
    minHeap = []

    # For each coordinate, calculate distance and add to ist of lists
    for x, y in points:
        # Calc distance from coord to origin. No subtraction needed, since origin is 0, 0.
        dist = math.sqrt((x**2) + (y**2))
        minHeap.append([dist, x, y])

    # Heapify the list of lists
    heapq.heapify(minHeap)

    # Init result list of lists
    result = []

    # Pop the smallest element k times and append to result
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        result.append([x, y])
        k -= 1

    return result


if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    k = 1
    print(kClosest(points, k), "expected: [[-2, 2]]")

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(kClosest(points, k), "expected:[[3, 3],[-2, 4]]")
