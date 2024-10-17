"""
567. Permutation in String (medium)

Given two strings 's1' and 's2', return 'True' if 's2' contains a permutation of 's1', or 'False' otherwise.

In other words, return 'True' if one of 's1''s permutations is the substring of 's2'.
"""


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Permutation = do not care about order of letters

    Solution 1: keeping count with two hashmaps/lists (s1 and s2's window) with 26 lowercase chars
    Shift window and update S2 list. Window remains the same. Right pointer shift by for loop, left manually.
    Use a matches counter between vector 1 and 2 (avoid comparing both hash maps again and again).

    Time complexity: O(26*n)
    Space complexity: O(2*26) -> two lists O(1) constant

    Solution 2 (not shown)
    Time complexity: O(n)
    """
    # Edge Case, can never return true
    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    # Populate the s1 list and s2 partially (first window, pick up rest of s2 later in window loop)
    for i in range(len(s1)):
        # ord() returns the letter's index in the list, subtracting ord('a') sets a = 0, b = 1 etc.
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    # Initially Compare s1 and s2 counts at every index (come back to that later)
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1

    # Sliding window portion
    leftPointer = 0
    # Start sliding window after first window width (already did above)
    for rightPointer in range(len(s1), len(s2)):
        # All counts match inside window (all count 1) and outside window (all count 0)
        if matches == 26:
            return True

        # RIGHT POINTER: Get list index of letter at RIGHT POINTER
        index = ord(s2[rightPointer]) - ord("a")
        # Increment counter for letter at right index
        s2Count[index] += 1
        # Increment 'matches' by one if s1 and s2 window letter counts are equal
        if s1Count[index] == s2Count[index]:
            matches += 1
        # If counts were equal BEFORE, decrement 'matches' by one
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # LEFT POINTER: Get list index of letter @ LEFT POINTER
        index = ord(s2[leftPointer]) - ord("a")
        # decrement counter for letter at left index
        s2Count[index] -= 1
        # Increment 'matches' by one if s1 and s2 window letter counts are equal
        if s1Count[index] == s2Count[index]:
            matches += 1
        # If counts were equal BEFORE, decrement 'matches' by one
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        leftPointer += 1

    # On last iteration there might be a match, so one last check.
    return matches == 26


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    print(
        checkInclusion(s1, s2),
        "expected: True. Explanation: s2 contains one permutation of s1 (ba).",
    )

    s1 = "ab"
    s2 = "eidboaoo"
    print(checkInclusion(s1, s2), "expected: False")


if __name__ == "__main__":
    main()
