"""
49. Group Anagrams (medium)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using

all the original letters exactly once.

"""


def groupAnagramsZeroArray(strs):
    """
    Time complexity: m*n*26 = O(n * m), m=number of strings, n=average length of string, 26=chars in alphabet
    """
    from collections import defaultdict

    hash_map = defaultdict(list)  # mapping charCount to list of anagrams

    for string in strs:
        count = [0] * 26  # initiate with list with zeros for the 26 letters from a...z

        for char in string:
            count[
                ord(char) - ord("a")
            ] += 1  # write to list at index by using char's ASCII value a->0, b->1
        hash_map[tuple(count)].append(
            string
        )  # write the count list/tuple as key and the string as value to hash_map

    return list(hash_map.values())  # return all values as one list


def groupAnagramsSorted(strs):
    """
    Time complexity: O(m * nlogn), m=number of strings, nlogn = sorting string
    """
    hash_map = {}

    for string in strs:
        sortedString = tuple(sorted(string))  # only tuples are hashable in dict
        if sortedString not in hash_map:
            hash_map[sortedString] = [
                string
            ]  # write sorted string (list) as key and string as value to hash_map
        else:
            hash_map[sortedString].append(
                string
            )  # append the list with additional strings with same sortedString

    return list(hash_map.values())  # return all values as one list of lists


def main():
    print(
        groupAnagramsZeroArray(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
        'expected: [["bat"],["nat", "tan"],\
    ["ate", "eat", "tea"]]',
    )
    print(groupAnagramsZeroArray(strs=[""]), 'expected: [[""]]')
    print(groupAnagramsZeroArray(strs=["a"]), 'expected: [["a"]]')

    print(
        groupAnagramsSorted(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
        'expected: [["bat"],["nat", "tan"],\
    ["ate", "eat", "tea"]]',
    )
    print(groupAnagramsSorted(strs=[""]), 'expected: [[""]]')
    print(groupAnagramsSorted(strs=["a"]), 'expected: [["a"]]')


if __name__ == "__main__":
    main()
