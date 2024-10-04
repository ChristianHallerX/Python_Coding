"""
300. Longest Increasing Subsequence (medium)

Given an integer array 'nums', return the length of the longest strictly increasing subsequence.
"""


def lengthOfLIS(nums: list[int]) -> int:
    """
    Brute Force DFS: create every possible subsequence. Decide for each index if you want to include in
    subsquence or not? Time complexity: O(2^n)

    DFS with caching (tree)

    Dynamic Programming bottom up
    Time complexity: O(n^2)
    Space complexity: O(n) for LIS cache
    Default minimal length is 1. Each value could be its own subsequence.
    When going backwards, add the lengths of the previous index if the value is less, otherwise it remains default 1.
    Why O(n^2)?? For each i, check he positions afterwards.
    """
    # Initialize cache as a list with default 1 (each index can be its own subarray with length 1)
    LIS = [1] * len(nums)

    # Reverse loop over 'nums'
    for i in range(len(nums) - 1, -1, -1):
        # Forward loop over elements i to end
        for j in range(i + 1, len(nums)):
            # For each index moving left, check for each index going right if its lower (increasing to right)
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    # Return the maximum of the list
    return max(LIS)


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums), "expected: 4, explanation: [2,3,7,101]")

    nums = [0, 1, 0, 3, 2, 3]
    print(lengthOfLIS(nums), "expected: 4")

    nums = [7, 7, 7, 7, 7, 7, 7]
    print(lengthOfLIS(nums), "expected: 1")


if __name__ == "__main__":
    main()
