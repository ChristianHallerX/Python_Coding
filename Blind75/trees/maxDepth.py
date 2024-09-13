"""
104. Maximum Depth of Binary Tree (easy)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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


def maxDepthRecursiveDFS(root: TreeNode) -> int:
    """
    1. Recursive DFS, O(n)
    """
    if not root:
        return 0

    return 1 + max(maxDepthRecursiveDFS(root.left), maxDepthRecursiveDFS(root.right))


from collections import deque


def maxDepthIterativeBFS(root: TreeNode) -> int:
    """
    2. Iterative BFS, O(n)
    Use deque() to host the tree nodes of a level.
    Use a level counter to keep track of max depth.
    Move down the tree. Remove current node on left side of deque.
    Get left and right nodes of current level nodes and append to right of deque.
    (Cycle of nodes on deque: Append lower level nodes on right, pop upper level nodes on left)
    """
    if not root:
        return 0

    level = 0
    # Deque will initially have the root value of the tree and then the two next lower nodes (breadth first search)
    # Append top tree node (root) to deque (easier to pop on the left, normal list is only efficient popping right)
    q = deque([root])
    while q:

        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def maxDepthIterativeDFS(root: TreeNode) -> int:
    """
    3. DFS but without recursion
    Use Stack with pairs of node/depth
    """
    result_depth = 0

    stack = [[root, 1]]
    while stack:
        # Take pair from top and fill into vars
        node, depth = stack.pop()

        if node:
            result_depth = max(depth, result_depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return result_depth


def main():
    root = create_binary_tree(lst=[3, 9, 20, None, None, 15, 7])
    print(f"recursive DFS: {maxDepthRecursiveDFS(root)}, expected: 3")
    print(f"iterative BFS: {maxDepthIterativeBFS(root)}, expected: 3")
    print(f"iterative DFS: {maxDepthIterativeDFS(root)}, expected: 3")

    print("\n")
    root2 = create_binary_tree(lst=[1, None, 2])
    print(f"recursive DFS: {maxDepthRecursiveDFS(root2)}, expected: 2")
    print(f"iterative BFS: {maxDepthIterativeBFS(root2)}, expected: 2")
    print(f"iterative DFS: {maxDepthIterativeDFS(root2)}, expected: 2")


if __name__ == "__main__":
    main()
