"""
209. Minimum Size Subarray Sum (medium)

Given an array of positive integers 'nums' and a positive integer 'target', return the minimal length of a
contiguous subarray [nums1, nums2, ..., nums7] whose sum is greater than or equal to 'target'.

If there is no such subarray, return 0 instead.
"""


def smallestSubarraySum(target: int, nums: list[int]):
    """
    Brute force: nested for loops, time complexity: O(n^2)

    Sliding Window: shift left/right pointers accordingly, time complexity: O(n), Memory complexity O(1)
    Right pointer gets moved to right continuously
    If total is above target, move left pointer forward to decrease total sum and minimize subarray size
    If total is below target, keep left pointer still.
    """
    left = 0
    total = 0
    result = float("inf")  # Minimize this subarray length. (right - left) distance

    # Move right pointer forward continuously
    for right in range(len(nums)):
        # Add value at right pointer to total
        total += nums[right]

        # Total above target, calculate subarray size and move left pointer so decrease size
        while total >= target:
            result = min((right - left + 1), result)
            total -= nums[left]
            left += 1

    return 0 if result == float("inf") else result


def main():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(smallestSubarraySum(target, nums), "expected: 2, explanation [4, 3]")

    target = 4
    nums = [1, 4, 4]
    print(smallestSubarraySum(target, nums), "expected: 1")

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(smallestSubarraySum(target, nums), "expected: 0")


if __name__ == "__main__":
    main()
