"""
105. Construct Binary Tree from Preorder and Inorder Traversal (medium)

Given two integer arrays 'preorder' and 'inorder' where 'preorder' is the preorder traversal
of a binary tree and 'inorder' is the inorder traversal of the same tree, construct and return the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Recursive Solution
    Preorder = root, left node, right node (pattern: center, left, right)
    Inorder = skip root, left node, root, left node of right node, right node, right node of right node
    (pattern = left, center, right)
    How do we leverage the differences of inorder and preorder to build the tree?
    Every value in tree is unique.
    Preorder starts with root. Find root val in inorder. Left of root is left subtree, right of root is right subtree.
    """
    # Base Case, None
    if not preorder or not inorder:
        return None

    # First preorder value is always root
    root = TreeNode(preorder[0])
    # Find index of root in inorder
    mid = inorder.index(preorder[0])

    # Recursive part with slices
    # preorder:Start at index 1 after root, end at mid (+1 because slicing is non-inclusive).
    # inorder: everything left of root is left subtree
    root.left = buildTree(preorder=preorder[1 : mid + 1], inorder=inorder[:mid])
    # preorder:Start at index after mid to end
    # inorder: everything left of root is left subtree
    root.right = buildTree(preorder=preorder[mid + 1 :], inorder=inorder[mid + 1 :])

    return root


def main():
    preoder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(
        tree_to_list(buildTree(preoder, inorder)),
        "expected: [3, 9, 20, None, None, 15, 7]",
    )

    preoder = [-1]
    inorder = [-1]
    print(tree_to_list(buildTree(preoder, inorder)), "expected: [-1]")


if __name__ == "__main__":
    main()
