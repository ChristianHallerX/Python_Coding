"""
371. Sum of Two Integers (medium)

Given two integers 'a' and 'b', return the sum of the two integers without using the operators + and -.
"""


def getSum(a: int, b: int) -> int:
    """
    First op: binary 'xor' operator (returns 0 if both bits equal, returns 1 if bits different)
    Second op:  binary 'and' operator for the carry over forward -> if both bits are one, return 0,
        then left shift one <<
    Repeat ops until carry over is 0.
    Negative vals are NOT handled automatically in Python because it does NOT have fixed-size 32bit ints.
    Use MASK to fix binary size (unlimited leading 1s).
    Time complexity: O(1) because limited size of input numbers
    """
    # Mask to limit python's unlimited leading 1's
    MASK = 0xFFFFFFFF

    # b is the carry
    while b != 0:
        # Second Op, carry bits: bitwise and (&), bitshift left (<<)
        oldB = (a & b) << 1
        # First op, addition without carry bits: bitwise exclusive or (xor ^)
        a = (a ^ b) & MASK
        b = oldB & MASK

    # Negative number fix: Check if number is negative or 0, convert to python's negative number representation
    if a > MASK // 2:
        return ~(a ^ MASK)
    # Positive number
    else:
        return a


def main():
    print(getSum(a=1, b=2), "expected: 3")

    print(getSum(a=2, b=3), "expected: 5")

    print(getSum(a=-1, b=1), "expected: 0")


if __name__ == "__main__":
    main()
