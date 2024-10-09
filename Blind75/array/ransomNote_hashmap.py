"""
383. Ransom Note (easy)

Given two strings 'ransomNote' and 'magazine', return 'True' if 'ransomNote' can be constructed by using
the letters from 'magazine' and False otherwise.

Each letter in 'magazine' can only be used once in 'ransomNote'.
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Very similar to isAnagram.
    Add both to hash map with count, then check if magazine count is higher or equal to ransomNote's dict
    """
    if len(ransomNote) > len(magazine):
        return False

    ransomDict = {}
    magazineDict = {}

    # Populate both dicts with char(key): count(value)
    # Use .get() for value for default value 0 if key is not in dict, this also works like +=
    for char_ran in ransomNote:
        ransomDict[char_ran] = 1 + ransomDict.get(char_ran, 0)
    for char_mag in magazine:
        magazineDict[char_mag] = 1 + magazineDict.get(char_mag, 0)

    # Compare counts in dicts. Fail if char does not exist in magazine dict or if count is lower
    for char, count in ransomDict.items():
        if (char not in magazineDict) or (magazineDict[char] < ransomDict[char]):
            return False

    return True


def main():
    ransomNote = "a"
    magazine = "b"
    print(canConstruct(ransomNote, magazine), "expected: False")

    ransomNote = "aa"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine), "expected: False")

    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine), "expected: True")


if __name__ == "__main__":
    main()
