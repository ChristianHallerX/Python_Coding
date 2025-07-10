"""
4. Median of Two Sorted Arrays (Hard)

Given two sorted arrays nums1 and nums2 of size 'm' and 'n' respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Median = middle value. Easy for odd number of values.
    But requires mean of two middle values in even number of values.

    Run a binary search over smaller array. Two pointers and two middle values to compare.

    O(log min(m,n)) -> requires binary search with pointers on the smaller of the arrays
    """

    # Convenient length variables
    total = len(nums1) + len(nums2)
    half = total // 2

    # Ensure nums1 is the smaller array. If not, reverse them.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Init pointers on nums1 (smaller array)
    l, r = 0, len(nums1) - 1

    # Perform binary search
    while True:

        # Middle index of left binary search partition
        i = (l + r) // 2

        # Middle index of right partition
        j = half - i - 2

        # Use indices to get values to compare partitions. Set -inf or +inf when values out of bounds
        nums1_left = nums1[i] if i >= 0 else float("-infinity")
        nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float("infinity")

        nums2_left = nums2[j] if j >= 0 else float("-infinity")
        nums2_right = nums2[j + 1] if j + 1 < len(nums1) else float("infinity")

        # Evaluate values of this iteration
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # odd length
            if total % 2:
                return min(nums1_right, nums2_right)
            # even length
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

        # We have too many elements from nums1, reduce size of left partition/nums1
        elif nums1_left > nums2_right:
            r = i - 1
        # Not enough elements from nums1, increase left partition
        else:
            l = i + 1


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(
        findMedianSortedArrays(nums1, nums2),
        "expected: 2.0000 \n explanation: merged array = [1,2,3] and median is 2",
    )

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(
        findMedianSortedArrays(nums1, nums2),
        "expected: 2.5000 \n explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5",
    )

    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [1, 2, 3, 4, 5]
    print(findMedianSortedArrays(nums1, nums2), "expected: 4")

    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [1, 2, 3, 4]
    print(findMedianSortedArrays(nums1, nums2), "expected: 3.5")
