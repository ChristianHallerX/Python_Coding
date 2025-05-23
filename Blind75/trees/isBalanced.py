"""
110. Balanced Binary Tree (Easy)
Given a binary tree, determine if it is height balanced.
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


def isBalanced(root: TreeNode) -> bool:
    """
    Recursive DFS, bottom up sub-tree checking of difference -> no more than 1
    Time complexity: O(n)
    """

    # helper DFS will return height of tree and blanced Boolean
    def dfs(root):
        """
        Returns a list [balanced_bool, depth (int)]
        """
        # Base case, empty tree is by default balanced and has 0 depth
        if not root:
            return [True, 0]

        # Run DFS on sub-trees
        left_res = dfs(root.left)
        right_res = dfs(root.right)

        # If both bools True and depths of left and right do not differ more than 1 --> balanced True
        balanced_bool = (
            left_res[0] and right_res[0] and abs(left_res[1] - right_res[1]) <= 1
        )
        return [balanced_bool, 1 + max(left_res[1], right_res[1])]

    # Start DFS on root and only return the balanced_bool
    return dfs(root)[0]


def main():
    lst = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = create_binary_tree(lst)
    print(isBalanced(root), "expected: False")

    lst = []
    root = create_binary_tree(lst)
    print(isBalanced(root), "expected: True")


if __name__ == "__main__":
    main()
