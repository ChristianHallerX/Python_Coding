"""
152. Maximum Product Subarray (medium)

Given an integer array 'nums', find a contiguous non-empty subarray within the array that has

the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

"""


def maxProduct(nums: list[int]) -> int:
    # for a num in the array, get the max (positive) and min (negative?) products up to before num,
    # then multiply minCurrent and maxCurrent with num. Only one loop required.

    # initialize as some non-negative number (hoping the max is positive), the single biggest single element could be
    # a solution
    res = max(nums)

    # initialize as neutral value
    curMax = 1
    curMin = 1

    for num in nums:
        temp = curMax
        # here we re-assign the current max, but we want the original in the curMin -> assign curMax to temp var
        # before re-assigning

        curMax = max(num * curMax, num * curMin, num)
        # use temp, i.e. the original curMax here
        curMin = min(temp * curMax, num * curMin, num)

        # compare positive curMax with initial res (largest single element) and re-assign
        res = max(res, curMax)
    return res


def main():
    print(maxProduct(nums=[2, 3, -2, 4]), "expected: 6")
    print(maxProduct(nums=[-2, 0, -1]), "expected: 0")


if __name__ == "__main__":
    main()
