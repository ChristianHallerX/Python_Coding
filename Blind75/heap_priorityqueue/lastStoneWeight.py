"""
1046. Last Stone Weight (Easy)

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y.

The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

import heapq


def lastStoneWeight(stones: list[int]) -> int:
    """
    Max heap (does not exist in Python) -> Solution as negative Min Heap (Python only implements min heaps)
    Pop the two largest items with auto-sorting in O(1) time
    The difference of the stones gets added back to the heap.

    Time Complexity: O(n) heapify, O(log n) get max from heap, get it n times. Total: O(nlogn)
    Space Complexity: O(n) create new heap and two vars.
    """
    # Convert to negative values. minheap --> maxheap
    stones = [-1 * item for item in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        # Pop two elements and make them positive
        first = heapq.heappop(stones) * -1
        second = heapq.heappop(stones) * -1
        # If both are equal, then we don't do anything, they destroy each other.
        # If they are different in size, then add the difference back.
        if first > second:
            # add the negative of the difference back to the heap
            heapq.heappush(stones, -(first - second))

    # Edge case: the heap was empty (two equal stones destroying each other in the last loop iteration)
    stones.append(0)

    # Return the remaining largest value and make positive
    return -stones[0]


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(stones), "expected: 1")

    stones = [1]
    print(lastStoneWeight(stones), "expected: 1")
