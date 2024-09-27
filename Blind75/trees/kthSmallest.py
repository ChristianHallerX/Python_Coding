"""
230. Kth Smallest Element in a BST (medium)

Given the root of a binary_search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
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


def kthSmallest(root: TreeNode, k: int) -> int:
    """
    Iterative with Stack containing unprocessed nodes. Add node, visit left (lower val) child node,
    Add left child -> child becomes center
    -> add left child node until reaching bottom of tree/None
    Start processing/popping stack when reached None at left node.
    Process center node, add right node.
    -> Visits all nodes in order small->large
    -> use counter 'n' for number of visited nodes and return node value when n==k.
    """
    # Init counter n
    n = 0
    stack = []

    # Pointer at node visiting
    cur = root

    while cur or stack:
        # While node is not None (end of tree), go move down left child nodes and add to stack
        while cur:
            stack.append(cur)
            cur = cur.left

        # Processing section. When reaching left None, process last node from stack and increment n
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val

        # If left's n was not k, go to right node and got to top of loop
        cur = cur.right


def main():
    root = create_binary_tree([3, 1, 4, None, 2])
    print(kthSmallest(root, k=1), "expected: 1")

    root = create_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    print(kthSmallest(root, k=3), "expected: 3")


if __name__ == "__main__":
    main()
