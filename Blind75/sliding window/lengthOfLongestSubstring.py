"""
3. Longest Substring Without Repeating Characters (medium)

Given a string 's', find the length of the longest UNIQUE substring without repeating characters.

Time complexity: O(n)
Space complexity: O(n) because each character could be unique and the result may be a copy of the input string.
"""


def lengthOfLongestSubstring(s: str) -> int:
    """
    Sliding window, two pointers, move across string only once.
    Move across s only once, move left and right pointers in a smart way.
    Check if substring has dublicates with set. If yes, move left pointer
    Time complexity O(n)
    Memory complexity O(n)
    You can only solve this if you can visualize the pointer movement.
    """
    charSet = set()
    left = 0
    resultLength = 0

    # right pointer is going through every character
    for right in range(len(s)):
        # Check if current right pointer is already in set,
        while s[right] in charSet:
            # If yes, remove left value and move left pointer
            charSet.remove(s[left])
            left += 1
        # In any case, add right value to charSet
        charSet.add(s[right])
        # Check current window size
        resultLength = max(resultLength, right - left + 1)

    return resultLength


def main():
    print(lengthOfLongestSubstring(s="abcabcbb"), "expected 3, abc")
    print(lengthOfLongestSubstring(s="bbbbb"), "expected 1, b")
    print(lengthOfLongestSubstring(s="pwwkew"), "expected 3, kew")


if __name__ == "__main__":
    main()
