"""
88. Merge Sorted Array (Easy)

You are given two integer arrays 'nums1' and 'nums2', sorted in non-decreasing order, and two integers 'm' and
'n', representing the number of elements in 'nums1' and 'nums2' respectively.

Merge 'nums1' and 'nums2' into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside
the array 'nums1'.

To accommodate this, 'nums1' has a length of 'm' + 'n', where the first 'm' elements denote the elements
that should be merged, and the last 'n' elements are set to 0 and should be ignored.

'nums2' has a length of 'n'.
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify 'nums1' in-place instead.

    Use two reading pointers 'n'/'m' and one writing/fill pointer.
    Write the largest values of 'nums1' and 'nums2' to the right end of 'nums1' and fill in towards left
    (reverse order).

    Time Complexity: O(m)
    Memory Complexity: O(1) no extra memory used
    """

    # fill pointer in 'nums1' starts at last index
    fill_pointer = m + n - 1

    while m > 0 and n > 0:
        # 'nums1' val is greater, pick that and fill in end of 'nums1'
        if nums1[m - 1] > nums2[n - 1]:
            nums1[fill_pointer] = nums1[m - 1]
            # Decrement 'm'
            m -= 1
        # Equal or 'nums2' greater
        else:
            nums1[fill_pointer] = nums2[n - 1]
            # Decrement 'n'
            n -= 1
        # Decrement fill pointer
        fill_pointer -= 1

    # Edge case: leftover elements in 'nums2'
    while n > 0:
        nums1[fill_pointer] = nums2[n - 1]
        n -= 1
        fill_pointer -= 1

    return None


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1, "expected: [1, 2, 2, 3, 5, 6]")

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(nums1, "expected: [1]")

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1, "expected: [1]")


if __name__ == "__main__":
    main()
