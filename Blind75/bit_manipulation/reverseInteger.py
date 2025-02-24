"""
7. Reverse Integer (Medium, was Easy)

Given a signed 32-bit integer 'x', return 'x' with its digits reversed.

If reversing 'x' causes the value to go outside the signed 32-bit integer range [-2**31, (2**31) - 1],
then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned) as Python does.**
"""

import math


def reverse(x: int) -> int:
    """
    Get the ones digit by modding (%) by ten, then integer division by 10 to remove ones digit.

    Challenge: artificially integrate a 32bit overflow in a 64bit environment.
    Chop off digits from right of 'x' moving left, append digits on 'result' moving right.
    """
    MIN = -(2**31)
    MAX = (2**31) - 1

    result = 0

    # Loop over input integer while it get manipulated and is NOT 0
    while x:
        # Chop off last digit on the right of x, loop moves to left
        last_digit = int(math.fmod(x, 10))  # workaround -x % 10 yields 9 in Python

        # Clip last digit off 'x' and round to 0 with cast to int
        x = int(x / 10)

        # Check for positive overflow above MAX value. Don't look at last digit yet (div by 10)
        if result > MAX // 10 or (result == MAX // 10 and last_digit >= MAX % 10):
            return 0

        # Check for negative overflow below MIN value. Don't look at last digit yet (div by 10)
        if result < MIN // 10 or (result == MIN // 10 and last_digit <= MIN % 10):
            return 0

        # Assemble reversed value from left (loop appends on right)
        result = (result * 10) + last_digit

    return result


def main():
    x = 123
    print(reverse(x), "expected 321")

    x = -123
    print(reverse(x), "expected -321")

    x = 120
    print(reverse(x), "expected 21")

    x = -2147483412
    print(reverse(x), "expected -2143847412")


if __name__ == "__main__":
    main()
