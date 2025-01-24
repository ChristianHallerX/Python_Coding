"""
DuoDigit

We call a decimal inter a "DuoDigit" if its decimal representation uses NO MORE than two different digits.
For example, "12" is a DuoDigit, but "102" is not.

Implement the function is_duo_ditit(number) which returns a string:
-y if a number is a DuoDigit
-n otherwise
"""


def is_duo_digit(number: int) -> str:
    # Convert the number to its absolute value and string representation
    number_str = str(abs(number))

    # Use a set to store the unique digits
    unique_digits = set(number_str)

    # Check if there are no more than two unique digits
    if len(unique_digits) <= 2:
        return "y"
    else:
        return "n"


def main():
    print(is_duo_digit(12), "expected y")
    print(is_duo_digit(-301), "expected: n")
    print(is_duo_digit(2828), "expected: y")


if __name__ == "__main__":
    main()
