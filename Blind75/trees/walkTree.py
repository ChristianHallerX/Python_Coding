"""
Walk a tree.

Designations are relative to root.
1. preorder (root, left, right)
2. inorder (left, root, right)
3. postorder (left, right, root)
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 1. Recursive depth-first traversal
def preorder(node):
    """
    Root (value) → Left → Right
    Print node value, then run function on branches.
    """
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


# 2. Recursive depth-first traversal
def inorder(node):
    """
    Left → Root → Right
    Run function on left branch, print node, run function on right branch.
    """
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


# 3. Recursive depth-first traversal
def postorder(node):
    """
    Left → Right → Root
    Run function on left branch, right branch, then print node
    """
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)


# 4. Iterative inorder using a stack
def inorder_iterative(root):
    """
    Left → Root → Right

    """
    stack, current = [], root
    while stack or current:
        # append all left to stack
        while current:
            stack.append(current)
            current = current.left
        # print node
        current = stack.pop()
        print(current.value)
        # then go right
        current = current.right


# 5. Breadth-first (level-order) traversal using a queue
def level_order(root):
    """
    Print layer by layer from left to right.
    """
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


if __name__ == "__main__":
    # Build this tree:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))

    print("Pre-order:")
    preorder(tree)  # 1 2 4 5 3 6

    print("\nIn-order:")
    inorder(tree)  # 4 2 5 1 3 6

    print("\nPost-order:")
    postorder(tree)  # 4 5 2 6 3 1

    print("\nIterative In-order:")
    inorder_iterative(tree)  # 4 2 5 1 3 6

    print("\nLevel-order:")
    level_order(tree)  # 1 2 3 4 5 6
