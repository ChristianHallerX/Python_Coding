"""
5. Longest Palindromic Substring
Given a string 's', return the longest palindromic substring in 's'.
"""

def longestPalindrome(s: str) -> str:
    # palindromes are mirrored and have a middle char. the longest palindrome is in the laf of the len of the string.

    def helper(left_index, right_index):
        """Returns the longest palindrome in s for a single central char entered as left_index and right_index params"""
        while (left_index>=0 and right_index<len(s) and s[left_index] == s[right_index]):
            left_index-=1
            right_index+=1
        return s[left_index+1:right_index]

    result=""
    for i in range(len(s)):
        # for uneven len s that have central char
        test = helper(i,i)
        if len(test) > len(result):
            result = test
        # repeat with shifted right index for even length s, since there is no central char
        test = helper(i, i+1)
        if len(test) > len(result):
            result = test

    return result


def main():
    print(longestPalindrome(s='babad'), 'expected bab or aba')
    print(longestPalindrome(s='cbbd'), 'expected bb')


if __name__ == '__main__':
    main()