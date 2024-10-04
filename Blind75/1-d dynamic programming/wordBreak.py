"""
139. Word Break (medium)

Given a string 's' and a dictionary of strings 'wordDict', return True if 's' can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    DP cache solution bottom up (reversing through the word)
    Check for each index of 's' if it matches a word in the 'wordDict'. Store the result in cache of bools.
    If words are in 's': create a chain of True bools from back to front of word.
    Did the chain of True get forwarded from last word to index 0? If not, return the default False at dp index 0.
    """
    # The cache is a list of bools (for each index a bool)
    dp = [False] * (len(s) + 1)

    # Initialize base case. If we ever get to the last index, return True
    dp[len(s)] = True

    # Reverse through index
    for i in range(len(s) - 1, -1, -1):
        # Check if any of the dict words matches this portion.
        # For this 'word', check if current word fits into 's' and if 'word' starts at index, then write True
        for word in wordDict:
            if (i + len(word)) <= len(s) and (s[i : i + len(word)]) == word:
                # Pick up the bool from the end of the 'word' and forward to i, so it becomes a chain of True (or not)
                dp[i] = dp[i + len(word)]
            # Avoid duplicating work and searching for more words if True bool already exists for this index
            if dp[i]:
                break

    # Was True forwarded all the way to index 0? If not, return the default False at dp index 0.
    return dp[0]


def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict), "expected: True")

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict), "expected: True")

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict), "expected: False")


if __name__ == "__main__":
    main()
