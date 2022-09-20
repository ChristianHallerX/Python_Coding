"""
125. Valid Palindrome (easy)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing

all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters

include letters and numbers.

Given a string 's', return True if it is a palindrome, or False otherwise.

"""

def isPalindrome(s: str) -> bool:
    """
    Built in functions (isalnum() and lower()) are unclear what time/space complexity they have
    """
    newStr = ""

    for char in s:
        if char.isalnum():  # check char if it is alphanumeric, if so write to new string
            newStr += char.lower()

    return newStr == newStr[::-1]


def isPalindromePointers(s: str) -> bool:
    """
    Compare chars at two pointers moving inward. Move pointers inward if not alphanum.
    time O(n), space O(1)
    """

    def alphanum(char):
        """
        Helper function to return True if a char is alphanumeric.
        """
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))


    # initialize pointers at left/right of string
    left_pointer, right_pointer = 0, len(s) - 1

    # keep pointers moving inward while they have not crossed
    while left_pointer < right_pointer:
        # move pointers inward if bad char (while not crossed and alphanumeric)
        while left_pointer < right_pointer and not alphanum(s[left_pointer]):
            left_pointer += 1
        while right_pointer > left_pointer and not alphanum(s[right_pointer]):
            right_pointer -= 1

        # compare the chars at the pointers
        if s[left_pointer].lower() != s[right_pointer].lower():
            return False

        # move pointers inward
        left_pointer += 1
        right_pointer -= 1

    return True


def main():
    print(isPalindrome(s="A man, a plan, a canal: Panama"), ' Expected: True')
    print(isPalindrome(s="race a car"), ' Expected: False')
    print(isPalindrome(s=" "), ' Expected: True')

    print(isPalindromePointers(s="A man, a plan, a canal: Panama"), ' Expected: True')
    print(isPalindromePointers(s="race a car"), ' Expected: False')
    print(isPalindromePointers(s=" "), ' Expected: True')


if __name__ == '__main__':
    main()
