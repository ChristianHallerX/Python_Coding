"""
297. Serialize and Deserialize Binary Tree (hard)

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored

in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or

another computer environment.

Design an algorithm to serialize and deserialize a binary tree.

There is no restriction on how your serialization/deserialization algorithm should work.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to

the original tree structure.

*Clarification*: The input/output format is the same as how LeetCode serializes a binary tree.

You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_binary_tree(lst):
    """
    Helper function.
    """
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while i < len(lst):
        current = queue.pop(0)

        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root


def tree_to_list(root):
    """
    Helper Function.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # Remove trailing None values, as they represent missing children
    while result and result[-1] is None:
        result.pop()

    return result


class Codec:
    def __init__(self):
        # Global var for deserializer
        self.i = None

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        Do pre-order traversal, Depth First Search (recursive).
        End points are encoded as "N".
        Different node values are delimited with comma.
        Time complexity O(n) for pre-order traversal

        Params
            root(TreeNode)
        Return
            str
        """
        # Init a list that gets at the end converted to a comma delimited string
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return None

            # Global variable result list
            res.append(str(node.val))

            # Run recursion and write to global var
            dfs(node.left)
            dfs(node.right)

        # Run function
        dfs(root)

        # After DFS, join all list elements to a single comma-delimited string
        return ",".join(res)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        Time complexity: O(n)
        Params
            data: str
        Return
            TreeNode
        """

        # Strip last comma that would lead to '', convert single string to list of strings
        vals = data.split(",")

        # Global index variable for vals list
        self.i = 0

        def dfs():
            # Base case, end-point is encoded as N -> None
            if vals[self.i] == "N":
                # Increment index for next function call
                self.i += 1
                return None

            # Create node at index i, convert string to int
            node = TreeNode(int(vals[self.i]))
            # Increment index for next function call
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        # Run DFS, return node
        return dfs()


def main():
    root = create_binary_tree([1, 2, 3, None, None, 4, 5])
    print(tree_to_list(root))
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print(tree_to_list(ans), "expected: [1, 2, 3, None, None, 4, 5]")

    root = create_binary_tree([])
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print(tree_to_list(ans), "expected: []")


if __name__ == "__main__":
    main()
