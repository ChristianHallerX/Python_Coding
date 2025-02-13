"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)

Given an array of integers 'nums' and an integer 'limit', return the size of the longest non-empty subarray
such that the absolute difference between any two elements of this subarray is less than or equal to 'limit'.
"""

from collections import deque


def longestSubarray(nums: list[int], limit: int) -> int:
    """
    The Sliding Window with Deque algorithm is used to efficiently find the longest subarray where the
    absolute difference between any two elements is less than or equal to a given limit.
    By maintaining two deques, one for the maximum values and one for the minimum values within the current
    window, we can dynamically adjust the window size while ensuring the condition is met.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Initialize deques for max and min values
    maxDeque = deque()  # monotonically decreasing order
    minDeque = deque()  # monotonically increasing order

    # Initialize pointers for the sliding window
    left = 0
    result = 0

    # Right pointer moves forward constinuously
    for right in range(len(nums)):

        # Maintain the decreasing order in maxDeque, if not decreasing, right val too large, then pop from right end
        while maxDeque and nums[maxDeque[-1]] <= nums[right]:
            maxDeque.pop()  # the pop() removes from the right side of the deque

        # Maintain the increasing order in minDeque, if not increasing, right val too small, then pop from right end
        while minDeque and nums[minDeque[-1]] >= nums[right]:
            minDeque.pop()

        # Add the current element index to both deques
        maxDeque.append(right)
        minDeque.append(right)

        # Check if the current window is not valid (diff above limit)
        while nums[maxDeque[0]] - nums[minDeque[0]] > limit:

            # Move the left pointer to shrink the window
            left += 1

            # Remove indices that are out of the new window
            if maxDeque[0] < left:
                maxDeque.popleft()
            if minDeque[0] < left:
                minDeque.popleft()

        # Update the result with the maximum window size found
        result = max(result, right - left + 1)

    return result


def main():
    nums = [8, 2, 4, 7]
    limit = 4
    print(longestSubarray(nums, limit), "expected: 2")

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(longestSubarray(nums, limit), "expected: 4")

    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    print(longestSubarray(nums, limit), "expected: 3")


if __name__ == "__main__":
    main()
