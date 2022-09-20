"""
242. Valid Anagram (easy)

Given two strings 's' and 't', return True if 't' is an anagram of 's', and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # dicts for both strings
    dictS, dictT = {}, {}

    # loop through index of s, write dicts with char count
    for i in range(len(s)):
        # write char at index i as dict key, count as value -> get count of current index (default val 0), add one
        dictS[s[i]] = 1 + dictS.get(s[i], 0) #use .get() for value for default value if key is not in dict
        # same for t
        dictT[t[i]] = 1 + dictT.get(t[i], 0)

    # compare each dict value
    for j in dictS:
        if dictS[j] != dictT.get(j, 0): #use .get() for value for default value if key is not in dict
            return False

    return True


def isAnagramBuiltIn(s: str, t: str) -> bool:
    from collections import Counter
    # counter creates dictionaries of s and t
    return Counter(s) == Counter(t)


def isAnagramSorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    print(isAnagram(s="anagram", t="nagaram"), 'expected: True')
    print(isAnagram(s="rat", t="car"), 'expected: False')
    print(isAnagramBuiltIn(s="anagram", t="nagaram"), 'expected: True')
    print(isAnagramBuiltIn(s="rat", t="car"), 'expected: False')
    print(isAnagramSorted(s="anagram", t="nagaram"), 'expected: True')
    print(isAnagramSorted(s="rat", t="car"), 'expected: False')


if __name__ == '__main__':
    main()
