"""
152. Maximum Product Subarray (medium)

Given an integer array 'nums', find a contiguous subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""


def maxProduct(nums: list[int]) -> int:
    """
    Brute force: try every single subarray with O(n^2)

    Optimized:
    If all positive numbers, then numbers will always increase.
    Subarrays with negatives are only positive if even number negatives.
    Keep track of max and min product subarray. If the next number is positive, multiply with max,
    if negative, multiply with min.
    0  resets min and max after 0 to 1
    Time complexity: O(n)
    Space complexity: O(1) Just two values curMax, curMin
    """
    # Init result, zero is not a good default, because nums = [-1], then the max is negative.
    result = max(nums)

    curMin, curMax = 1, 1

    for n in nums:
        # if n == 0:
        #     curMin, curMax = 1, 1
        #     continue

        tmp = curMax * n

        # This line re-assigns curMax, but the curMin calculation requires the old value -> use tmp variable
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        result = max(result, curMax)

    return result


def main():
    nums = [2, 3, -2, 4]
    print(maxProduct(nums), "expected: 6")

    nums = [-2, 0, -1]
    print(
        maxProduct(nums),
        "expected: 0, Explanation: cannot be 2, because [-2,-1] is not a contiguous subarray.",
    )


if __name__ == "__main__":
    main()
