"""
217. Contains Duplicate (easy)

Given an integer array 'nums', return 'True' if any value appears at least twice in the array,
and return 'False' if every element is distinct.
"""


def containsDuplicate(nums):
    """
    Brute force solution: sort, loop over numbers and check if numbers repeat.
    Time Complexity: O(nlogn + n)

    Optimized: Use hash map. Store current number in hash map and look up if it already exists.
    Time Complexity: O(n). Space complexity: O(n)
    Alternative: Use set, that avoids keys/values
    """

    # num(key) -> index(value)
    hash_map = {}

    for i, num in enumerate(nums):
        # Check if current element (num) is in hash_map, finish function and return True
        if num in hash_map.keys():
            return True

        # If num not in hash_map, write index as key
        hash_map[num] = i
    return False


def containsDuplicateSet(nums):
    return len(nums) != len(set(nums))


def main():
    print(containsDuplicate(nums=[1, 2, 3, 1]), "expected: True")
    print(containsDuplicate(nums=[1, 2, 3, 4]), "expected: False")
    print(containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "expected: True")
    print(containsDuplicateSet(nums=[1, 2, 3, 1]), "expected: True")
    print(containsDuplicateSet(nums=[1, 2, 3, 4]), "expected: False")
    print(containsDuplicateSet(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "expected: True")


if __name__ == "__main__":
    main()
