"""
202. Happy Number (Easy)

Write an algorithm to determine if a number 'n' is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return True if 'n' is a happy number, and False if not.
"""


def sumOfSquares(n: int) -> bool:
    result = 0

    while n:
        # Grab last digit by modulo and square
        last_digit = (n % 10) ** 2

        # Drop last digit off of n
        n = n // 10

        # Sum up the squared last digits
        result += last_digit

    return result


def isHappy(n: int) -> bool:
    """

    Hash Set to record sum of squares.
        If endless repeating circle of sum of squares values (3, 4, 5, 3, 4, 5...) -> unhappy
        If endless repeating loop of 1 (1, 1, 1, 1...)-> happy

    Memory Complexity: O(n) bad
    Better memory complexity with linked list cycle detection problem.
    """
    visit_set = set()

    while n not in visit_set:
        visit_set.add(n)
        n = sumOfSquares(n)
        if n == 1:
            return True

    # While-loop cancelled because n was in the set (loop) and not 1
    return False


def main():
    n = 19
    print(isHappy(n), "expected: True")

    n = 2
    print(isHappy(n), "expected: False")

    n = 1
    print(isHappy(n), "expected: True")


if __name__ == "__main__":
    main()
