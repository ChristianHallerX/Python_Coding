"""
114. Flatten Binary Tree to Linked List (Medium)

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node
in the list and the left child pointer is always null. (WEIRD, not a true linked list)

The "linked list" should be in the same order as a pre-order traversal of the binary tree.
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


def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.

    Recursively DFS:(iteratively with stack)
    Flatten left sub-tree, and insert at right branch between root and original right child.
    Left branch will be None.
    Time complexity: O(n)
    Space complexity: O(height) => worst case o(n)
    """

    # Flatten the tree and return the "list" tail
    def dfs(root):
        if not root:
            return None

        # Run dfs recursively on left and right
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        # Attach flattened left branch into right branch and set left branch to None (in other cases we do nothing)
        if root.left:
            leftTail.right = root.right
            root.right = root.left  # insert here
            root.left = None

        # After inserting flattened branch, point at the branch node that comes after.
        # The or statements assign whichever node that is not None.
        last = rightTail or leftTail or root
        return last

    # Run DFS and return nothing
    dfs(root)


def main():
    root = create_binary_tree([1, 2, 5, 3, 4, None, 6])
    flatten(root)
    out_list = tree_to_list(root)
    print(out_list, "expected: [1, None, 2, None, 3, None, 4, None, 5, None, 6]")

    root = create_binary_tree([])
    flatten(root)
    out_list = tree_to_list(root)
    print(out_list, "expected: []")

    root = create_binary_tree([0])
    flatten(root)
    out_list = tree_to_list(root)
    print(out_list, "expected: [0]")


if __name__ == "__main__":
    main()
