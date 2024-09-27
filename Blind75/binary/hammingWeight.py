"""
191. Number of 1 Bits (easy)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the
Hamming weight).

Note:
    - Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be
    given as a signed integer type. It should not affect your implementation, as the integer's internal binary
    representation is the same, whether it is signed or unsigned.
    - In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the
    input represents the signed integer. -3.
"""


def hammingWeight(n: int) -> int:
    """
    Intuition: modulus 'n' by two, if last place was 1, returns 1, if 0 then 0. Use the output of the modulus
    to add to a running sum 'result'. Then, bit shift 'n' to the right, a 0 is added on the left of 'n'.
    When bit-shifted far enough, 'n' is all 0, which we use as condition for the while-loop to finish.
    """
    result = 0

    # While the number still contains 1s....
    while n > 0:
        result += n % 2  # Modulus by two and add rest 'to result'
        n = n >> 1
    return result


def main():
    print(hammingWeight(n=0b00000000000000000000000000001011), "expected: 3")
    print(hammingWeight(n=0b00000000000000000000000010000000), "expected: 1")
    print(hammingWeight(n=0b11111111111111111111111111111101), "expected: 31")


if __name__ == "__main__":
    main()
