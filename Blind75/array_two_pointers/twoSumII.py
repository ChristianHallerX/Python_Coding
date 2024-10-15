"""
167. Two Sum II - Input Array Is Sorted (medium, was easy)

Given a *1-indexed* array_hashing of integers numbers that is *already sorted in non-decreasing order*, find two numbers

such that they add up to a specific target number.

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array_hashing [index1, index2] of length 2.

Notes:
    The tests are generated such that there is exactly one solution.
    You may not use the same element twice.
    Your solution must use only constant extra space.
"""


def twoSumII(numbers: list[int], target: int) -> list[int]:
    """
    Brute Force Solution:
    Fix left pointer at an index (loop) and check with right pointer if sum adds up to target (inner loop).
    Stop inner loop when sum above target.
    Time complexity: O(n^2)

    Two pointer optimal solution:
    Make use of sorting.
    Left pointer init at start of list, right pointer at end.
    If total sum too big, shift right pointer to down and decrease total sum.
    If total sum too small, shift left pointer up
    Time complexity: O(n) pointers will not cross
    Space complexity: O(1) no extra memory
    """
    # Initialize pointer indices at left and right of nums
    left_pointer, right_pointer = 0, len(numbers) - 1

    # Keep iterating while pointers do not cross
    while left_pointer < right_pointer:
        current_sum = numbers[left_pointer] + numbers[right_pointer]
        # If sum bigger than target, shift right pointer one left to decrease sum
        if current_sum > target:
            right_pointer -= 1
        # If sum smaller than target, shift left pointer one to right to increase sum
        elif current_sum < target:
            left_pointer += 1
        # Sum matches target -> return the 1-indexed pointers
        elif current_sum == target:
            return [left_pointer + 1, right_pointer + 1]

    # Add a return in case nothing found, however, there should ALWAYS be exactly one solution
    return []


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(
        twoSumII(numbers, target),
        "expected [1, 2]."
        "The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].",
    )

    numbers = [2, 3, 4]
    target = 6
    print(
        twoSumII(numbers, target),
        "expected [1, 3]."
        "Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].",
    )

    numbers = [-1, 0]
    target = -1
    print(
        twoSumII(numbers, target),
        "expected [1, 2]."
        "Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].",
    )


if __name__ == "__main__":
    main()
