"""
1143. Longest Common Subsequence (medium)

Given two strings 'text1' and 'text2', return the length of their longest common subsequence.

If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    LCS: Bottom-up 2-D grid of both strings: string1 * string2
    Base case: 0, bottom row +1, right column +1
    Matching chars: 1
    Fill in all grid cells. Then, starting bottom right, move over the grid and sum upwards.
    If matching chars, add diagonal from bottom right. If no match, take max of current cells' bottom cell and right cell.
    Result: top left corner.
    Time complexity: O(n * m)
    Space complexity: O(n * m) size of dp grid
    """
    # Initialize 2d-grid with 0s and add extra row on bottom and extra column on right
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    # Reverse loop over combinations of chars, but skip extra row and col. Start at bottom right.
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            # Matching chars: Write 1 to dp at current position and add the bottom right diagonal dp values
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            # No matching chars, write to dp at current position the maximum of right and bottom dp values
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


def main():
    text1 = "abcde"
    text2 = "ace"
    print(longestCommonSubsequence(text1, text2), "expected: 3, explanation: ace")

    text1 = "abc"
    text2 = "abc"
    print(longestCommonSubsequence(text1, text2), "expected: 3, explanation: abc")

    text1 = "abc"
    text2 = "def"
    print(longestCommonSubsequence(text1, text2), "expected: 0")

    text1 = "abcba"
    text2 = "abcbcba"
    print(longestCommonSubsequence(text1, text2), "expected: 5")


if __name__ == "__main__":
    main()
