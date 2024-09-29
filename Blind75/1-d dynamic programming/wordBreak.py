"""
139. Word Break (medium)

Given a string 's' and a dictionary of strings 'wordDict', return True if 's' can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s: str, wordDict: list[str]) -> bool:


    return True


def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict), "True")

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict), "True")

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict), "False")


if __name__ == "__main__":
    main()
