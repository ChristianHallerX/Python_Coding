"""
53. Maximum Subarray (medium, used to be easy)

Given an integer array 'nums', find the *contiguous* subarray (containing at least one number) which has

the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


def maxSubArray(nums: list[int]) -> int:
    """
    Only return 'maximum sum' value. (Do not return the values used for the sum)
    Keep a 'curSum' and a 'maxSum', reset 'curSum' when adding num made sum negative.
    Intuition: Loop over nums once with one pointer. Only sum up negative values if they don't bring
        the curSum into negative. Otherwise, reset curSum to 0. Similar to sliding window.
    Time complexity: O(n), loop once over nums
    Space complexity: O(1), two integers
    """

    # Initialize maxSub sum with first value of list and curSum variables
    maxSub = nums[0]
    curSum = 0

    # Loop over list once
    for num in nums:
        # If adding the last num made sum negative, reset curSum to 0 and restart subarray.
        if curSum < 0:
            curSum = 0

        # Add current number to curSum
        curSum += num

        # Recalculate the maxSub
        maxSub = max(maxSub, curSum)

    return maxSub


def main():
    print(
        maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        "Expected: 6, explanation: [4, -1, 2, 1]",
    )
    print(maxSubArray(nums=[1]), "Expected 1")

    print(maxSubArray(nums=[5, 4, -1, 7, 8]), "Expected 23")


if __name__ == "__main__":
    main()
