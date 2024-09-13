"""
100. Same Tree (easy)

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
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


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    Time Complexity: O(p+q). In worst case iterate through both trees.
    We need to compare each node individually recursivelly.

    Consider all the comparisons in a position:
    1. Nodes both None = True
    2. One node None = False
    3. Nodes not equal values = False
    """
    # Base case 1: both nodes None
    if not p and not q:
        return True

    # Base case 2: one node None, the other is normal node
    if not p or not q:
        return False

    # Base case 3: values not equal
    if p.val != q.val:
        return False

    # Recursive step, if both recursions return True, also return True
    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)


if __name__ == "__main__":
    p = create_binary_tree([1, 2, 3])
    q = create_binary_tree([1, 2, 3])
    print(isSameTree(p, q), "expected: True")

    p = create_binary_tree([1, 2])
    q = create_binary_tree([1, None, 3])
    print(isSameTree(p, q), "expected: False")

    p = create_binary_tree([1, 2, 1])
    q = create_binary_tree([1, 1, 2])
    print(isSameTree(p, q), "expected: False")
