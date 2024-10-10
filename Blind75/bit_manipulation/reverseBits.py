"""
190. Reverse Bits (easy)

Reverse bits of a given 32 bits unsigned integer.
"""


def reverseBits(n: int) -> int:
    """
    Read a bit from right to left, and write it from left to right a new result variable.
    Iterate through the 32 indices.
    Time complexity: O(32) constant
    """
    result = 0

    # i increases
    for i in range(32):
        # Read the bit at right-shifted position i. Read using the & operation.
        bit = (n >> i) & 1

        # Write the bit in result, but from the reversed direction, write at the shifted position
        result = result | (bit << (31 - i))

    return result


def main():
    n = 0b00000010100101000001111010011100
    print(reverseBits(n), "expected: 964176192 (00111001011110000010100101000000)")

    n = 0b11111111111111111111111111111101
    print(reverseBits(n), "expected: 3221225471 (10111111111111111111111111111111)")


if __name__ == "__main__":
    main()
