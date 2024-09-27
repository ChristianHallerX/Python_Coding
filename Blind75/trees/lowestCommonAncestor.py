"""
235. Lowest Common Ancestor of a Binary Search Tree (medium)

Given a binary_search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes

p and q as the lowest node in T that has both p and q as descendants

(where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
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


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    # Case 1: Split further down on one branch: if p and q both larger than root, then search right for LCA,
    # else search left for LCA
    # Case 2: Split at root: if p larger than root and q smaller than root (or vice versa) then root is LCA
    # Case 3: if p or q are equal to the root value, then the root is LCA by definition
    # return the node where the p/q are larger/smaller then current node
    # Time Complexity: O(logn) visit only one node per level, which means height of the tree -> logn
    # Memory Complexity: O(1), no extra data structures

    cur = root

    while cur:
        # Case 1: p and q down right sub tree
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        # Case 1: p and q down left sub tree
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        # Case 2/3: split at root or p/q are same val as root -> return root/node
        else:
            return cur


def main():
    root = create_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(8)
    print(lowestCommonAncestor(root, p, q).val, "expected: 6")

    root = create_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(4)
    print(lowestCommonAncestor(root, p, q).val, "expected: 2")

    root = create_binary_tree([2, 4])
    p = TreeNode(2)
    q = TreeNode(4)
    print(lowestCommonAncestor(root, p, q).val, "expected: 2")


if __name__ == "__main__":
    main()
