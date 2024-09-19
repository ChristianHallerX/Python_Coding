"""
208. Implement Trie (Prefix Tree) (medium)

A trie (pronounced as "try") or prefix tree is a special kind of tree data structure used to efficiently store
and retrieve keys in a dataset of strings.

There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- 'insert(word)' Inserts the string 'word' into the trie.
- 'search(word)' Returns True if the string 'word' is in the trie (i.e., was inserted before), and False otherwise.
- 'startsWith(prefix)' Returns True if there is a previously inserted string 'word' that has the prefix 'prefix',
    and False otherwise.
"""


class TrieNode:
    def __init__(self):
        # Will contain chars implicitly as dict. Add char as key. children[char]
        self.children = {}
        self.endOfWord = False


class Trie:
    """
    The main point of a Trie is the 'startsWith' function for partial words. Otherwise, we could use a hash map (dict).
    A Trie requires each character of a word inserted as separate child node of the root (root is a placeholder node).
    Last char needs to be marked.
    """

    def __init__(self):
        # init with empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at root
        cur = self.root

        # Add each character as new node
        for char in word:
            # If node for this char does NOT exist, then create node for this character
            if char not in cur.children:
                cur.children[char] = TrieNode()
            # Set that child node as current
            cur = cur.children[char]
        # After looping through all chars, mark last character node as end of word node
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Start at root
        cur = self.root

        # Check if each node exists consecutively and last char marked as end
        for char in word:
            # Node with char not found in children! Break
            if char not in cur.children:
                return False
            # Node found, move to that child node
            cur = cur.children[char]

        # Made it through loop AND check if last node has endOfWord marker set True
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start at root
        cur = self.root

        # Check if each node exists consecutively
        for char in prefix:
            # node with char not found in children! Break
            if char not in cur.children:
                return False
            # Node found, move to that child node
            cur = cur.children[char]

        # Made it through loop
        return True


def main():
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    obj.startsWith("app")
    obj.insert("app")
    print(obj.search("app"))

    print("expected: [None, None, True, False, True, None, True]")


if __name__ == "__main__":
    main()
