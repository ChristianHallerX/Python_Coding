"""
212. Word Search II (Hard)

Solution: Backtracking DFS Trie

Extension of LC 79 Word Search I, Backtracking. this time with a list of words.

Given an 'm' * 'n' board of characters and a list of strings 'words', return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where *adjacent cells* are horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word (no loops, but different words
may share a letter).

Essentially, implement a crossword algo??
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # Dict contains children. letter-> key, child nodes-> values
        self.isWord = False  # Defines that node/char is end of a word

    def addWord(self, word):
        cur = self
        for char in word:
            # Add char child node if it is not in Trie yet
            if char not in cur.children:
                cur.children[char] = TrieNode()
            # Move cur pointer to that char node
            cur = cur.children[char]
        # Mark last node as end of word
        cur.isWord = True


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Solution: Start DFS for each grid cell a backtracking brute-force search plus prfix Trie.
    Instead of looping over the search words individually, we search over a Trie that we build first.
    Time complexity: Bad implementation: O(n*m * 4^n*n * len(words)) just loop over 'words'
                     Good implementation O(n*m * 4^n*n) Visit each grid cell only once and use Trie
    """
    # Write the Trie (attach words char by char to root node)
    root = TrieNode()
    for word in words:
        root.addWord(word)

    ROWS, COLS = len(board), len(board[0])
    # Sets ensure we remove duplicates. We return the result, path keeps track with coordinates have been visited
    result, path = set(), set()

    def dfs(row, col, node, foundWord):
        """
        node = current node in Trie
        foundWord = (sub)string which chars have we visited and confirmed chars so far
        ROWS, COLS, result, path are global vars
        """

        # Base cases to exit dfs
        if (
            (row < 0 or col < 0)  # Row/Col out of bounds
            or (row == ROWS or col == COLS)  # Row/Col out of bounds
            or ((row, col) in path)  # Coord is on path and already visited
            or (board[row][col] not in node.children)
        ):  # Grid char at current coordinate is not a child of root or current node, skip
            return False

        # Not base case. Char at coord is in Trie. Mark coordinate as visited on path
        path.add((row, col))
        # Found a char, update the node
        node = node.children[board[row][col]]
        # Append letter to 'foundWord' string
        foundWord += board[row][col]
        # Check if this node/char is end, if yes, write foundWord string to result list
        if node.isWord:
            result.add(foundWord)

        # Recursive dfs call on four adjacent coordinates
        dfs(row - 1, col, node, foundWord)  # down
        dfs(row + 1, col, node, foundWord)  # up
        dfs(row, col - 1, node, foundWord)  # left
        dfs(row, col + 1, node, foundWord)  # right

        # Backtracking step, remove current coordinate from visited path again
        path.remove((row, col))

    # Run DFS with starting conditions on every starting position (all coordinates) of grid
    for r in range(ROWS):
        for c in range(COLS):
            dfs(row=r, col=c, node=root, foundWord="")

    return list(result)


def main():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(findWords(board, words), "expected: ['eat', 'oath']")

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print(findWords(board, words), "expected: []")


if __name__ == "__main__":
    main()
