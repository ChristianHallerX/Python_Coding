"""
242. Valid Anagram (easy)

Given two strings 's' and 't', return True if 't' is an anagram of 's', and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
"""


def isAnagram(s: str, t: str) -> bool:
    """
    Intuition: create dicts for s and t with letter(key): count(value)
    Dicts are equal for valid anagrams
    """
    if len(s) != len(t):
        return False

    # Init dicts for both strings
    dictS, dictT = {}, {}

    # Loop through index of and s and t, write dicts with char count
    for i in range(len(s)):
        # Write char at index i as dict key, count as value
        # Use .get() for value for default value 0 if key is not in dict, this also works like +=
        dictS[s[i]] = 1 + dictS.get(s[i], 0)
        dictT[t[i]] = 1 + dictT.get(t[i], 0)

    # Compare dicts
    if dictT == dictS:
        return True
    else:
        return False


def isAnagramBuiltIn(s: str, t: str) -> bool:
    from collections import Counter

    # counter creates dictionaries of s and t
    return Counter(s) == Counter(t)


def isAnagramSorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    print(isAnagram(s="anagram", t="nagaram"), "expected: True")
    print(isAnagram(s="rat", t="car"), "expected: False")

    print(isAnagramBuiltIn(s="anagram", t="nagaram"), "expected: True")
    print(isAnagramBuiltIn(s="rat", t="car"), "expected: False")

    print(isAnagramSorted(s="anagram", t="nagaram"), "expected: True")
    print(isAnagramSorted(s="rat", t="car"), "expected: False")


if __name__ == "__main__":
    main()
