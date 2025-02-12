"""
954. Array of Doubled Pairs (Medium)

Given an integer array of even length 'arr', return True if it is possible to reorder 'arr' such that
arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or False otherwise.
"""


def canReorderDoubled(arr: list[int]) -> bool:
    """
    Determine if an array can be reordered such that every element at an odd index is double the preceding element
    at an even index.
    -> Intuition: Count occurrences of each num and match each number with its double.
    Small nums matched with large numbers -> sort by absolute.
    Time Complexity: counting O(n), sorting O(n*logn), pairing O(n) -> total O(n*logn) dominated by sorting
    Space Complexity: count dict O(n), sorted arr O(n) -> total 2O(n) -> O(n)
    """
    # Step 1: Count the occurrences
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Step 2: Sort the keys by absolute values e.g. [-2, 2, 4, -4] so that the smaller numbers come
    # first and the double numbers later (otherwise we'd be looking for the double of the double)
    sorted_keys = sorted(count_dict, key=abs)

    # Step 3: Loop over unique numbers (sorted keys, find pairs, and break the loop if the double value pair can't be
    # found in enough quantity
    for num in sorted_keys:
        # If there aren't enough 2*num's to pair with num, return False.
        if count_dict[num] > count_dict.get(2 * num, 0):
            return False
        # Reduce double num's count by num's count
        count_dict[2 * num] = count_dict.get(2 * num, 0) - count_dict[num]
    return True


def main():
    arr = [3, 1, 3, 6]
    print(canReorderDoubled(arr), "expected: False")

    arr = [2, 1, 2, 6]
    print(canReorderDoubled(arr), "expected: False")

    arr = [4, -2, 2, -4]
    print(canReorderDoubled(arr), "expected: True")
    print(
        "explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4]."
    )

    arr = [2, 1, 2, 1, 1, 1, 2, 2]
    print(canReorderDoubled(arr), "expected: True")


if __name__ == "__main__":
    main()
