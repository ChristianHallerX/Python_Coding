"""
5. Longest Palindromic Substring (medium)

Given a string 's', return the longest palindromic substring in 's'.

You may assume that the maximum length of 's' is 1000.
"""


def longestPalindrome(s: str) -> str:
    """
    Palindromes are mirrored and have a middle char.
    The longest palindrome is in the laf of the len of the string.
    """

    def palindrome_helper(left_index, right_index):
        """
        Given a central index to start from (left and right start from center index),
        Move pointers outwards until no more equal chars.
        Return longest palindrome string starting from indices.
        Time complexity: O(n^2)
        """
        while (
            left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]
        ):
            left_index -= 1
            right_index += 1
        return s[left_index + 1 : right_index]

    # Start the helper from every char
    result = ""
    for i in range(len(s)):
        # Case 1: With central char (odd-length string)
        test = palindrome_helper(i, i)

        # Update result
        if len(test) > len(result):
            result = test

        # Case 2: No central char (even-length string): shifted right index
        test = palindrome_helper(i, i + 1)

        # Update Result
        if len(test) > len(result):
            result = test

    return result


def main():
    print(longestPalindrome(s="babad"), "expected bab or aba")
    print(longestPalindrome(s="cbbd"), "expected bb")


if __name__ == "__main__":
    main()
