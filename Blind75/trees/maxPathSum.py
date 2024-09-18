"""
124. Binary Tree Maximum Path Sum (hard)

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge

connecting them. A node can only appear in the sequence at most once.

Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

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


def maxPathSum(root: TreeNode) -> int:
    """
    Depth First Search, recursively.
    Time complexity O(n)
    """

    # Init global var with root val, otherwise dfs() has to return max path with split and without split
    res = [root.val]

    def dfs(root):
        """
        DFS helper, return max path sum WITHOUT split
        Update global result list WITH split
        """

        # base case
        if not root:
            return 0

        # Compute the recursive part in straight path, NO split. Root -> left -> root -> left
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        # Previous left max vs 0 (if negative value hurts the sum, use zero, skip
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # Compute max path sum WITH split on root and compare to global variable result
        res[0] = max(res[0], root.val + leftMax + rightMax)

        # Max() returns only the highest straight direction
        return root.val + max(leftMax, rightMax)

    # Run DFS and update global var result
    dfs(root)

    return res[0]


def main():
    root = create_binary_tree([1, 2, 3])
    print(maxPathSum(root), "expected: 6")

    root = create_binary_tree([-10, 9, 20, None, None, 15, 7])
    print(maxPathSum(root), "expected: 42")


if __name__ == "__main__":
    main()
