"""
543. Diameter of Binary Tree (Easy)

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def diameterOfBinaryTree(root: TreeNode) -> int:
    """
    Recursive DFS solution
    Depth on left branch + depth on right branch.
    Time complexity: O(n) linear, visit each node once
    Space complexity: height of tree O(logn) balanced tree, O(n) non-balanced tree.
    """
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        # Depths of left/right subtrees
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        # path through this node is left_depth + right_depth
        diameter = max(diameter, left_depth + right_depth)

        # return height of this subtree, don't forget + 1 for extending for curr
        return 1 + max(left_depth, right_depth)

    # Run DFS and update the diameter variable
    dfs(root)
    return diameter


def main():
    lst = [1, 2, 3, 4, 5]
    head = create_binary_tree(lst)
    print(diameterOfBinaryTree(head), "expected: 3")

    lst = [1, 2]
    head = create_binary_tree(lst)
    print(diameterOfBinaryTree(head), "expected: 1")


if __name__ == "__main__":
    main()
