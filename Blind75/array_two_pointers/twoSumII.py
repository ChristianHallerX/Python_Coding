"""
167. Two Sum II - Input Array Is Sorted (medium)

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
    left/right pointer solution to go over list only once -> time complexity O(n), no extra memory space
    pointers will never cross each other
    shift right pointer to decrease sum, shift left pointer to increase sum
    """
    # initialize pointer indices at left and right of array_hashing
    left_pointer, right_pointer = 0, len(numbers) - 1

    # keep iterating while pointers do not cross
    while left_pointer < right_pointer:
        current_sum = numbers[left_pointer] + numbers[right_pointer]
        # if sum bigger than target, shift right pointer one left to decrease sum
        if current_sum > target:
            right_pointer -= 1
        # if sum smaller than target, shift left pointer one to right to increase sum
        elif current_sum < target:
            left_pointer += 1
        # if numbers at pointers match target return the 1-indexed pointers
        elif current_sum == target:
            return [left_pointer + 1, right_pointer + 1]

    # add a return in case nothing found, however, there should ALWAYS be exactly one solution
    return []


def main():
    print(twoSumII(numbers=[2, 7, 11, 15], target=9), "expected: [1, 2]")
    print(twoSumII(numbers=[2, 3, 4], target=6), "expected: [1, 3]")
    print(twoSumII(numbers=[-1, 0], target=-1), "expected: [1, 2]")


if __name__ == "__main__":
    main()
