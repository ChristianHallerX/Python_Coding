"""
15. 3Sum (medium) (updated description)

Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] such that

i != j,
i != k,
j != k, and
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    """Return a list with all unique triplets with sum zero
    Sort nums. O(nlogn)
    The triplet is A, B, and C.
    Iterate A. B and C are pointers that solve Two Sum.
    Time complexity: O(nlogn) (sorting), iterating a O(n) and fore at the same time
    iterating pointers O(n) -> total O(nlogn) + O(n2), but reduces to O(n2)
    """
    result = []
    # Sorted means left is negative, right are positive numbers
    nums = sorted(nums)

    # Iterate from left to right, negative to positive.
    for i, a in enumerate(nums):
        # skip A forward if value left of A is the same
        if i > 0 and a == nums[i - 1]:
            continue

        # B and C are a two-pointer problem.
        left = i + 1
        right = len(nums) - 1

        while left < right:
            threeSum = a + nums[left] + nums[right]
            if threeSum > 0:
                # Update pointers
                right -= 1
            elif threeSum < 0:
                # Update pointers
                left += 1
            else:
                result.append([a, nums[left], nums[right]])
                # Update pointers
                left += 1
                # Skip forward if Left is the same
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result


def main():
    print(threeSum(nums=[-1, 0, 1, 2, -1, -4]), "Expected [[-1,-1, 2], [-1, 0, 1]]")
    print(threeSum(nums=[0, 1, 1]), "Expected []")
    print(threeSum(nums=[0, 0, 0]), "Expected [[0, 0, 0]]")
    print(threeSum(nums=[0]), "Expected []")


if __name__ == "__main__":
    main()
