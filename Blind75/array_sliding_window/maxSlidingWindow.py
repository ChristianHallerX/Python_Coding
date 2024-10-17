"""
239. Sliding Window Maximum (hard)

You are given an array of integers nums, there is a sliding window of size 'k' which is moving from the very left
of the array to the very right.

You can only see the 'k' numbers in the window.

Each time the sliding window moves right by one position.

Return the max sliding window.
"""

from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Best solution: Monotonically decreasing queue (deque). Add and pop from end of deque in O(1) time.
    Deque is the window that contains the indices to nums.
    Add to deque and pop smaller elements on left, left most value remaining in deque goes to result list.
    Time complexity: O(n)
    """
    result = []
    # deque will contain indices window
    q = deque()
    leftPointer = 0
    rightPointer = 0

    while rightPointer < len(nums):
        # pop all values from right side of q if they are smaller than the right pointer's value
        while q and nums[q[-1]] < nums[rightPointer]:
            q.pop()
        # Append if last deque element is larger than rightPointer
        q.append(rightPointer)

        # Left most value out of bounds: If leftPointer is larger than left queue index
        # -> remove leftPointer from window
        if leftPointer > q[0]:
            q.popleft()

        # Append the largest number (left most in q) to result (edge case of min window size)
        if (rightPointer + 1) >= k:
            result.append(nums[q[0]])
            leftPointer += 1

        # right is always incremented
        rightPointer += 1

    return result


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k), "expected: [3, 3, 5, 5, 6, 7]")

    nums = [1]
    k = 1
    print(maxSlidingWindow(nums, k), "expected: [1]")


if __name__ == "__main__":
    main()
