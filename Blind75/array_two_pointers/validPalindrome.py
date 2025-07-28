"""
125. Valid Palindrome (easy)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing

all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters

include letters and numbers but no spaces and punctuation.

Given a string 's', return True if it is a palindrome, or False otherwise.

"""


def isPalindrome(s: str) -> bool:
    """
    Solution 1:
    Check if string matches reversed string.

    Built-in functions (isalnum() and lower()) are unclear what time/space complexity they have
    """
    newStr = ""

    for char in s:
        if (
            char.isalnum()
        ):  # check char if it is alphanumeric, if so write to new string
            newStr += char.lower()

    return newStr == newStr[::-1]


def isPalindromePointers(s: str) -> bool:
    """
    Solution 2:
    Two pointers moving from outside to center of word.
    Compare letter/number between the pointers. Move inward if match.

    Build own alphanumeric helper function
    Time complexity: O(n), pointers iterate only once over string.
    """

    def validAlphaNum(char: str) -> bool:
        """
        Returns True if alphanumeric.
        """
        return (
            ord("a") <= ord(char) <= ord("z")
            or ord("A") <= ord(char) <= ord("Z")
            or ord("0") <= ord(char) <= ord("9")
        )

    left = 0
    right = len(s) - 1

    while left < right:
        # Skip forward if not alphanumeric
        while left < right and not validAlphaNum(s[left]):
            left += 1
        while right > left and not validAlphaNum(s[right]):
            right -= 1

        # Return false if lowercase chars are not equal
        if s[left].lower() != s[right].lower():
            return False
        # Move pointers inward
        else:
            left += 1
            right -= 1
    return True


def main():
    print(isPalindrome(s="A man, a plan, a canal: Panama"), " Expected: True")
    print(isPalindrome(s="race a car"), " Expected: False")
    print(isPalindrome(s=" "), " Expected: True")

    print(isPalindromePointers(s="A man, a plan, a canal: Panama"), " Expected: True")
    print(isPalindromePointers(s="race a car"), " Expected: False")
    print(isPalindromePointers(s=" "), " Expected: True")


if __name__ == "__main__":
    main()
