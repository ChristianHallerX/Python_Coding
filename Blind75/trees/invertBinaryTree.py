"""
226. Invert Binary Tree (easy)

Given the root of a binary tree, invert the tree, and return its root.
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


def invertTree(root: TreeNode) -> TreeNode:
    """
    Recursive Depth First Search (DFS)
    """
    if not root:
        return None

    # Swap children
    temp = root.left
    root.left = root.right
    root.right = temp

    # Apply same function recursively
    invertTree(root.left)
    invertTree(root.right)

    return root


def main():
    input = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
    print(tree_to_list(invertTree(root=input)), "expected: [4, 7, 2, 9, 6, 3, 1]")


if __name__ == "__main__":
    main()
