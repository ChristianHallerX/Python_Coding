"""
53. Maximum Subarray (medium)

Given an integer array 'nums', find the contiguous subarray (containing at least one number) which has

the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


def maxSubArray(nums: list[int]) -> int:
    # we don't care about the indices where the numbers come for, all that matters is the maximum sum
    # keep a current sum and a max sum, reset current sum when element is negative
    # kind of a 'array_sliding_window'

    # initialize max Sub with first value of list
    maxSub = nums[0]

    # initialize current sum
    curSum = 0

    # loop over list once
    for num in nums:
        # if negative, reset current Sum to 0
        if curSum < 0:
            curSum = 0

        # add number to current Sum
        curSum += num

        # recalculate the maximum
        maxSub = max(maxSub, curSum)
    return maxSub


def main():
    print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), "Expected: 6")
    print(maxSubArray(nums=[1]), "Expected 1")
    print(maxSubArray(nums=[5, 4, -1, 7, 8]), "Expected 23")


if __name__ == "__main__":
    main()
