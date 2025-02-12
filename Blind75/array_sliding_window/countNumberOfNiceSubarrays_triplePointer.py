"""
1248. Count Number of Nice Subarrays (Medium)

Given an array of integers 'nums' and an integer 'k'.
A continuous subarray is called nice if there are 'k' odd numbers on it.

Return the number of nice sub-arrays.
"""


def numberOfSubarrays(nums: list[int], k: int) -> int:
    """
    Triple pointer sliding window.
    Sub-arrays can also contain trailing (left/right) values that are even.
    1. Right pointer moves forward with loop, add to odd counter
    2. Check of there are k odd vals between left and right. If too many, move Left and Middle, decrement odd
    3. Middle pointer moves to first odd number
    4. Count sub-arrays between the left and middle pointer that should all contain k odd values. res = M - L + 1

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, middle = 0, 0
    odd = 0
    result = 0

    for right in range(len(nums)):

        # increase window on the right, increment odd
        if nums[right] % 2:
            odd += 1

        # too many odd, decrease window from left and decrement odd
        while odd > k:
            if nums[left] % 2:
                odd -= 1
            left += 1
            middle = left

        if odd == k:
            # while not odd (while even) move middle. Open the gap between left and middle.
            while not nums[middle] % 2:
                middle += 1
            # calculate all possible sub-arrays between left and middle
            result += (middle - left) + 1

    return result


def main():
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(numberOfSubarrays(nums, k), "expected: 2")

    nums = [2, 4, 6]
    k = 1
    print(numberOfSubarrays(nums, k), "expected: 0")

    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(numberOfSubarrays(nums, k), "expected: 16")


if __name__ == "__main__":
    main()
