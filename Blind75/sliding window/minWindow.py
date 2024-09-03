"""
76. Minimum Window Substring (hard)

Given two strings 's' and 't' of lengths 'm' and 'n' respectively, return the minimum window substring of 's'
such that every character in 't' (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""


def minWindow(s: str, t: str) -> str:
    """
    Dict for window contents
    Dict for t chars
    Chars in window dict
    Move right pointer. Once the window contains all correct chars, move the left pointer.
    """
    # Handle edge case
    if s == "":
        return ""

    countT = {}
    windowDict = {}

    # Add t chars to dict and increment, default to 0 if not in dict. Will not change.
    for char in t:
        countT[char] = countT.get(char, 0) + 1

    left = 0
    haveCount = 0  # correct chars in window
    needCount = len(countT)  # unique characters in T
    result = [-1, -1]  # we return a substring with pair of window indices
    resultLength = float("infinity")  # start high, go lower

    # Always move right pointer
    for right in range(len(s)):

        # as right pointer moved, add new char to window dict
        windowDict[s[right]] = windowDict.get(s[right], 0) + 1

        # If this is a char we need and the count of this char is correct
        if (s[right] in countT) and (windowDict[s[right]] == countT[s[right]]):
            haveCount += 1

        # When chars with count are present, record the window and its length and mimimize its size
        # When we don't have all chars anymore, then move right pointer again.
        while haveCount == needCount:
            # Update resultLength (window) if smaller than previous (starts @infinity)
            if (right - left + 1) < resultLength:
                result = [left, right]
                resultLength = right - left + 1

            # Decrement left pointer in window dict
            windowDict[s[left]] -= 1

            # Remove from Have counter if it was correct char and if window dict count
            # of char is now lower
            if (s[left] in countT) and (windowDict[s[left]] < countT[s[left]]):
                haveCount -= 1

            # Move left pointer
            left += 1

    left, right = result
    # edge case: only return if result lower than infinity
    return s[left : right + 1] if resultLength != float("infinity") else ""


def main():
    print(minWindow(s="ADOBECODEBANC", t="ABC"), "expected BANC")
    print(minWindow(s="a", t="a"), "expected a")
    print(minWindow(s="a", t="aa"), "expected '' empty string")


if __name__ == "__main__":
    main()
