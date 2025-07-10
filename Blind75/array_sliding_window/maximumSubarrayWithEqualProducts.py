"""
3411. Maximum Subarray With Equal Products (Easy)

You are given an array of positive integers 'nums'.

LCM = Least Common Multiple
GCD = Greatest Common Divisor

An array 'arr' is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

    - prod(arr) is the product of all elements of arr.
    - gcd(arr) is the Greatest Common Divisor of all elements of arr.
    - lcm(arr) is the Least Common Multiple of all elements of 'arr'.

Return the length of the longest product equivalent of 'nums'.
"""

import math


def gcd(a, b):
    return math.gcd(a, b)


# Helper function
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def maxLength(nums: list[int]) -> int:
    """
    Two pointer approach, nested loops.
    Time Complexity: O(n2)
    """
    # Init subarray max length counter
    result = 1

    # left pointer sweeps left to right
    for left in range(len(nums)):
        # init all vars
        subarray_gcd = subarray_lcm = subarray_product = nums[left]

        # right pointer start in front of left pointer to end of array
        for right in range(left + 1, len(nums)):
            right_val = nums[right]
            subarray_product *= right_val
            subarray_lcm = lcm(subarray_lcm, right_val)
            subarray_gcd = gcd(subarray_gcd, right_val)

            # Check for equal products using helper funs
            if subarray_product == (subarray_lcm * subarray_gcd):
                # update result with length of subarray
                result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 1, 1, 1]
    print(maxLength(nums), "expected: 5")

    nums = [2, 3, 4, 5, 6]
    print(maxLength(nums), "expected: 3")

    nums = [1, 2, 3, 1, 4, 5, 1]
    print(maxLength(nums), "expected: 5")
