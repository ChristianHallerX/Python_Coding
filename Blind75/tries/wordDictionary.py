"""
211. Design Add and Search Words Data Structure (medium)

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- addWord(word) Adds word to the data structure, it can be matched later.
- search(word) Returns True if there is any string in the data structure that matches 'word' or False otherwise.
  'word' may contain dots '.' where dots can be matched with any letter (wildcard *)
"""


class TrieNode:
    def __init__(self):
        self.children = (
            {}
        )  # Will contain character Trie nodes in a dictionary. Char is key, children nodes is values
        self.endOfWord = False  # Marker by default False


class WordDictionary:
    """
    Trie prefix tree will contain nodes for each character (a-z, 26).
    Use marker for end of word.
    DFS to search with wildcards.
    """

    def __init__(self):
        # Root node contains no chars
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Loop over chars in 'word' and add node to root and children if not exists
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            # Move current node forward to char node
            cur = cur.children[char]
        # Reached end of word, set bool
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Entire search() is DFS
        # Multiple Wildcards in a row require brute force/DFS to find out if after one path there is another node
        # Has to contain stop marker at last node to be complete word

        def dfs(j, root):
            # Root is the starting node for DFS (will iterate)
            # j is the index in 'word' (will iterate)
            cur = root

            # Loop over letters in 'word' starting at j
            for i in range(j, len(word)):
                char = word[i]

                # Wildcard char
                if char == ".":
                    #  Dict key is the child nodes of the current node, search children on NEXT 'word' index
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                # Regular char
                else:
                    # Char does not exist
                    if char not in cur.children:
                        return False
                    # Char DOES exist, move cur node forward
                    cur = cur.children[char]

            # When reaching end of word/loop, return True if endOfWord marker is True
            return cur.endOfWord

        # Run DFS, starting at 0 index of 'word', returns Bool, so that search() returns Bool
        return dfs(j=0, root=self.root)


def main():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"), "expected False")
    print(wordDictionary.search("bad"), "expected True")
    print(wordDictionary.search(".ad"), "expected True")
    print(wordDictionary.search("b.."), "expected True")

    wordDictionary = WordDictionary()
    wordDictionary.addWord("a")
    wordDictionary.addWord("a")  # 'a' node should already exist and do nothing
    print(wordDictionary.search("."), "expected True")
    print(wordDictionary.search("a"), "expected True")
    print(wordDictionary.search("aa"), "expected False")
    print(wordDictionary.search("a"), "expected True")
    print(wordDictionary.search(".a"), "expected False")
    print(wordDictionary.search("a."), "expected False")


if __name__ == "__main__":
    main()
