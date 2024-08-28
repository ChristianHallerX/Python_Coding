"""
238. Product of Array Except Self (medium)

Given an integer array 'nums', return an array 'answer' such that 'answer[i]' is equal to the product of all the

elements of 'nums' except 'nums[i]'.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

(We could simply multiply all values, loop over them and divide for each value. That is forbidden.)
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Write the prefix and postfix multiplications to the same results array
    Prefix is the multiplication up to the index before i,
    Postfix is the multiplication of index after i to end.
    """

    # Initialize output array with same size as nums, populate with 1's
    result = [1] * len(nums)

    # Loop over nums and assign prefixes to result
    # Starting value for prefix
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]  # Update prefix

    # Starting value for postfix
    postfix = 1
    # Loop backwards from right to left
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix  # effectively multiplying pre with post
        postfix *= nums[i]  # Update postfix

    return result


def main():
    print(productExceptSelf(nums=[1, 2, 3, 4]), "expected output = [24,12,8,6]")
    print(productExceptSelf(nums=[-1, 1, 0, -3, 3]), "expected output = [0,0,9,0,0]")


if __name__ == "__main__":
    main()
