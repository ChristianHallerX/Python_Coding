"""
647. Palindromic Substrings (medium)

Compare to problem 5. Longest Palindromic Substring

Given a string 's', return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


def countSubstrings(s: str) -> int:
    """
    Brute force time complexity: O(n^3)
    Optimized time complexity: odd length O(n^2), even length O(n^2) -> O(2 * n^2) -> O(n^2)
    Search for each char in 's' for odd and even length palindromes by moving left/right pointers outwards.
    """

    def palindrome_helper(left, right):
        count = 0
        while (
            (left >= 0)  # left in bounds
            and (right < len(s))  # right in bounds
            and (s[left] == s[right])  # equal chars
        ):
            count += 1  # for each passing loop, we found a palindrome
            left -= 1
            right += 1
        return count

    # Use helper for each starting char in 's' for odd and even palindromes
    result = 0
    for i in range(len(s)):

        # Odd length palindromes (both pointers start from a center char)
        left = right = i
        result += palindrome_helper(left, right)

        # Even length palindromes (right starts shifted)
        left, right = i, i + 1
        result += palindrome_helper(left, right)

    return result


def main():
    s = "abc"
    print(countSubstrings(s), "expected: 3, explanation: a, b, c")

    s = "aaa"
    print(countSubstrings(s), "expected: 6, explanation: a, a, a, aa, aa, aaa")


if __name__ == "__main__":
    main()
