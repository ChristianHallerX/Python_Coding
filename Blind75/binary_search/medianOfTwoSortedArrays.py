"""
4. Median of Two Sorted Arrays (Hard)

Given two sorted arrays 'nums1' and 'nums2' of size 'm' and 'n' respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    return None


def main():
    nums1 = [1, 3]
    nums2 = [2]
    print(
        findMedianSortedArrays(nums1, nums2),
        "explanation: merged array = [1,2,3] and median is 2",
    )

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(
        findMedianSortedArrays(nums1, nums2),
        "explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5",
    )


if __name__ == "__main__":
    main()
