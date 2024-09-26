"""
269. Alien Dictionary (hard)

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
(The order is not a, b, c, d,...)

You are given a list of strings 'words' from teh alien language's dictionary, where the strings in 'words' are sorted
lexicographically increasing order by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the
new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string 's' is lexicographically smaller than a string 't' if at the first letter where they differ, the letter in 's'
comes before the letter in 't' in the alien language. If the first min(s.length, t.length) letters are the same, then
's' is smaller if and only of s.length < t.length.
"""


def alienOrder(words: list[str]) -> str:
    """
    Topological Sort, Directed A-cyclical Graph (DAG) with Depth First Search
    Strings given are already sorted according to 'alien dictionary'.
    Compare two strings with overlapping chars (prefix), the first differing letters give a clue on order.
    Shorter words that are a prefix of another word always come first in order: 1. "ape", 2. "apes".
    If this rule is violated, the "alien dict" is invalid and return "" empty string.
    Create a graph that brings the letters in order.
    If the graph of letters cannot be connected (islands) or there is a cycle,
    -> there is no solution and return "" empty string.
    Time Complexity: O(n) number of chars in input
    """
    # Init char adjacency dict with key(char)->value(set(chars))
    adjacency = {char: set() for w in words for char in w}

    # DFS prep. Loop through word pairs and populate the adjacency dict with chars
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        # The shorter length of word pair
        minLen = min(len(word1), len(word2))

        # Edge case of same prefix but word2 is longer than word1 -> wrong ordering according to description
        if (len(word1) > len(word2)) and (word1[:minLen] == word2[:minLen]):
            return ""

        # Loop over common length letters and break where they start differing
        for j in range(minLen):
            if word1[j] != word2[j]:
                # When the letters start to differ, add the two differing letters to adjacency dict
                adjacency[word1[j]].add(word2[j])
                break

    # Global vars. True=visited and in path, False=visited, not in dict=not visited
    visit = {}
    result = []

    # Define post-order DFS that builds 'result' in reversed
    def dfs(char):
        """
        Mainly checks on neighbors if the visit dict contains True or False
        """
        if char in visit:
            return visit[char]

        # If char not in visit, add and set to 'in path' True
        visit[char] = True

        # Recursive dfs call on dict values and check for loops
        for neighborChar in adjacency[char]:
            # If dfs() returns True, we have a loop, return True
            if dfs(neighborChar):
                return True

        # Set to 'not in path', i.e., False
        visit[char] = False
        result.append(char)

    # Call DFS on dict key chars
    for char in adjacency:
        # Detected a loop, bad
        if dfs(char):
            return ""

    # Reverse result list
    result.reverse()
    # Join chars on list to a single string
    return "".join(result)


def main():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(alienOrder(words), "expected: wertf")


if __name__ == "__main__":
    main()
