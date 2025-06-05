"""
1448. Count Good Nodes in Binary Tree (Medium)

Given a binary tree root, a node 'X' in the tree is named good if in the path from root to 'X'
there are no nodes with a value greater than 'X'.

Return the number of good nodes in the binary tree.
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


def goodNodes(root: TreeNode) -> int:

    return None


if __name__ == "__main__":
    lst = [3, 1, 4, 3, None, 1, 5]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 4")

    lst = [3, 3, None, 4, 2]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 3")

    lst = [1]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 1")
