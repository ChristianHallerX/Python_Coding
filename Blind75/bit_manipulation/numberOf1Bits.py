"""
191. Number of 1 Bits (easy)

Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).
"""


def hammingWeight(n: int) -> int:
    """
    Loop over all bits by using bit shift. Repeat until binary length is reduced to 0:
    (1) Modulo divide by 2, if 1 returned, then add the 1 to counter.
    (2) Then bit shift to right, which shortens the number binary.
    Time complexity: O(32) constant. An integer by default has 32 bits, which mean at worst loop 32 times.
    """
    result = 0

    # Loop over all 32 bits of the integer
    while n:
        # If last bit was 1, then modulo returns 1, which can be added to counter
        result += n % 2
        # Bit shift right and shorten binary
        n = n >> 1

    return result


def hammingWeightOnesOnly(n: int) -> int:
    """
    Time complexity: O(1) constant.
    Loop only over the '1' bits
    """
    result = 0

    # Loop only over the '1's in the bits by skipping over all the '0's. by comparing with n-1
    while n:
        n &= n - 1
        result += 1

    return result


def main():
    n = 11
    print(
        hammingWeight(n),
        "expected: 3, Explanation: The input binary string 1011 has a total of three set bits.",
    )
    print(hammingWeightOnesOnly(n))

    n = 128
    print(
        hammingWeight(n),
        "expected: 1, Explanation: The input binary string 10000000 has a total of one set bit.",
    )
    print(hammingWeightOnesOnly(n))

    n = 2147483645
    print(
        hammingWeight(n),
        "expected: 30, The input binary string 1111111111111111111111111111101 has a total of thirty set bits.",
    )
    print(hammingWeightOnesOnly(n))


if __name__ == "__main__":
    main()
