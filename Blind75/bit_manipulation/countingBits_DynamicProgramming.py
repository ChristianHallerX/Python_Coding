"""
338. Counting Bits (easy, was medium)

Given an integer 'n', return an array 'ans' of length 'n' + 1 such that for each 'i' (0 <= i <= n), 'ans[i]' is the
number of 1's in the binary representation of 'i'.
"""


def countBits(n: int) -> list[int]:
    """
    Loop through range of n, get binary of each and count 1s, append count to list.
    Dynamic Programming: Eliminate repeated work looking at the '1's where patterns repeat.
    Every 4 numbers, we add one significant number to the count of '1'.
    Use offset to read the FIRST set of four numbers (n=0 to n=3).
    For current n, add 1 to count at n-4 plus increasing offset.
    Time complexity: O()
    """
    # DP is a list that stores previously computed results for '1's and is also result
    dp = [0] * (n + 1)

    # Offset is a variable that determines how far back we look in dp and gets increased
    offset = 1

    # Start at 1, skip 0
    for i in range(1, n + 1):
        if i == offset * 2:
            offset = i

        # Calculate '1's for current i with help of pre-calculated '1's in dp
        dp[i] = 1 + dp[i - offset]

    return dp


def main():
    n = 2
    print(
        countBits(n),
        "expected: [0, 1, 1]",
        """
        Explanation: i = 0 --> 0 bin --> 0 '1's
                     i = 1 --> 1 bin --> 1 '1's
                     i = 2 --> 10 bin --> 1 '1's
        """,
    )

    n = 5
    print(
        countBits(n),
        "expected: [0, 1, 1, 2, 1, 2]",
        """
        Explanation: 0 --> 0 bin --> 0 '1's
                     1 --> 1 bin --> 1 '1's
                     2 --> 10 bin --> 1 '1's
                     3 --> 11 bin --> 2 '1's
                     4 --> 100 bin --> 1 '1's
                     5 --> 101 bin --> 2 '1's
        """,
    )


if __name__ == "__main__":
    main()
