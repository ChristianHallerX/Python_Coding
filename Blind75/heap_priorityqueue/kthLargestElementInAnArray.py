"""
215. Kth Largest Element in an Array (Medium)

Given an integer array 'nums' and an integer 'k', return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""


def findKthLargest(nums: list[int], k: int) -> int:
    """
    Solution 1: Python built-in Sorting
        Time Complexity: O(n*logn) do not use!

    Solution 2: Max Heap
        1. Heapify max heap in n time
        2. pop from end k times in logn time -> k*logn
        Time Complexity: O(n + k*logn).
        Only if k is small, then this is faster than sorting.

    Solution 3: Recursive Quick Select
        1. Partition the array in larger/smaller than pivot (not sort)
        2. Choose a pivot pointer
        3. left p starts at index 0 and increment upwards with for-loop
        3. Val@ Left p larger than val@ pivot pointer?
            smaller-> increment left p,
            larger-> left p remains equal
        4. Swap val@ left p with val@ pivot pointer
        5. Result value must be right of left p
        Time Complexity: O(2*n) average, O(n**2) worst
        Space Complexity: O(1) all in place
    """
    # nums.sort()
    # return nums[len(nums) - k]

    # convert k to an index in an ascending sorted array
    k_index = len(nums) - k

    def quickSelect(l, r):
        # Read out the pivot value and set left_p to left most position
        pivot_val, left_p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot_val:
                nums[left_p], nums[i] = nums[i], nums[left_p]
                left_p += 1

        # Swap left_p with pivot_val (nums[r] is the pivot_val)
        nums[left_p], nums[r] = nums[r], nums[left_p]

        # Check where to continue quickSelect
        if left_p > k_index:
            # Search left of left_p
            return quickSelect(l, left_p - 1)
        elif left_p < k_index:
            # Search right of left_p
            return quickSelect(left_p + 1, r)
        else:
            # left_p is equal to k_index
            return nums[left_p]

    # Start with initial values
    return quickSelect(0, len(nums) - 1)


def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k), "expected: 5")

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k), "expected: 4")


if __name__ == "__main__":
    main()
