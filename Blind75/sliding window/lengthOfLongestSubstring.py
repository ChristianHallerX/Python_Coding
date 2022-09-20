"""
3. Longest Substring Without Repeating Characters (medium)

Given a string 's', find the length of the longest UNIQUE substring without repeating characters.

Time complexity: O(n)
Space complexity: O(n) because each character could be unique and the result may be a copy of the input string.
"""

def lengthOfLongestSubstring(s: str) -> int:
    left_pointer, right_pointer = 0, 1
    result = 0

    while right_pointer < len(s):
        if len(s[left_pointer:right_pointer + 1]) == len(set(s[left_pointer:right_pointer + 1])):
            # no duplicates
            # substring_length = len(set(s[left_pointer:right_pointer + 1]))
            substring_length = right_pointer - left_pointer + 1
            result = max(result, substring_length)
            # move right pointer
            right_pointer += 1
        else:
            # contains duplicate
            left_pointer += 1
    return result


def main():
    print(lengthOfLongestSubstring(s="abcabcbb"), "expected 3, abc")
    print(lengthOfLongestSubstring(s="bbbbb"), "expected 1, b")
    print(lengthOfLongestSubstring(s="pwwkew"), "expected 3, kew")


if __name__ == "__main__":
    main()
