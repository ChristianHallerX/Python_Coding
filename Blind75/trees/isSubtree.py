"""
572. Subtree of Another Tree (easy)

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same

structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.

The tree tree could also be considered as a subtree of itself.

## Contains recursive solution 100. isSameTree.py
## WHY IS THIS STILL CONSIDERED EASY
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


### FIRST IMPLEMENT isSameTree()
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
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


def isSubtree(rootS: [TreeNode], subRootT: [TreeNode]) -> bool:
    """
    Time complexity: O(s*t)
    Compare for each s node with whole t subRoot
    """
    # Start with base case
    if not subRootT:
        # If Subroot is None, it's always a sub tree, regardless what tree is.
        return True
    if not rootS:
        # Subroot is not None (checked above) and root is empty, no subtree possible
        return False

    # Both trees are not None, compare them
    if isSameTree(rootS, subRootT):
        return True

    # Resursive part, OR since sub tree only has to match in one of the branches
    return isSubtree(rootS.left, subRootT) or isSubtree(rootS.right, subRootT)


def main():
    root = create_binary_tree([3, 4, 5, 1, 2])
    subRoot = create_binary_tree([4, 1, 2])
    print(isSubtree(root, subRoot), "expected: True")

    root = create_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = create_binary_tree([4, 1, 2])
    print(isSubtree(root, subRoot), "expected: False")


if __name__ == "__main__":
    main()
