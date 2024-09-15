"""
98. Validate Binary Search Tree (medium)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
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


def isValidBST(root: TreeNode) -> bool:
    """
    Recursive solution. Depth First Search, DFS.
    Brute force solution: check at each node for the subtree -> O(n^2)
    Can't just check the direct children.
    Check the subtrees for each node again.
    All nodes of a subtree must be larger than or smaller than the root.

    Time complexity: O(2n) -> O(n)
    """

    # Helper function
    def valid(node, left, right):
        # ends/None are still valid
        if not node:
            return True

        # Breaking condition for BST node/left/right
        if not (node.val < right and node.val > left):
            return False

        # Recursive call on left and right children values
        return valid(node=node.left, left=left, right=node.val) and valid(
            node=node.right, left=node.val, right=right
        )

    # Call helper function with initialized root/left/right values and return
    return valid(node=root, left=float("-inf"), right=float("inf"))


def main():
    root = create_binary_tree([2, 1, 3])
    print(isValidBST(root), "expected: True")

    root = create_binary_tree([5, 1, 4, None, None, 3, 6])
    print(isValidBST(root), "expected: False")


if __name__ == "__main__":
    main()
