"""
199. Binary Tree Right Side View (Medium)

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
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


from collections import deque


def rightSideView(root: TreeNode) -> list[int]:
    """
    BFS, Modified level order traversal
    At each level, keep the right-most node.
    Time Complexity: O(n) visit each node once
    Space Complexity: O(1) create only result data structure
    """
    result = []

    # Initialize q with root
    q = deque([root])

    # Loop through levels of tree
    while q:
        # Number of nodes on level
        qLen = len(q)
        rightSide = None
        for i in range(qLen):
            # Remove the leftmost node from q
            node = q.popleft()
            if node:
                # Last node in this level of the q
                rightSide = node
                # Append children of node to q
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            result.append(rightSide.val)

    return result


if __name__ == "__main__":
    lst = [1, 2, 3, None, 5, None, 4]
    root = create_binary_tree(lst)
    print(rightSideView(root), "expected: [1, 3, 4]")

    lst = [1, 2, 3, 4, None, None, None, 5]
    root = create_binary_tree(lst)
    print(rightSideView(root), "expected: [1, 3, 4, 5]")

    lst = [1, None, 3]
    root = create_binary_tree(lst)
    print(rightSideView(root), "expected: [1, 3]")

    lst = []
    root = create_binary_tree(lst)
    print(rightSideView(root), "expected: []")
