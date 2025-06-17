"""
1448. Count Good Nodes in Binary Tree (Medium)

Given a binary tree root, a node 'X' in the tree is named good if in the path from root to 'X'
there are no nodes with a value greater than 'X'.

Return the number of good nodes in the binary tree.
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


def goodNodes(root: TreeNode) -> int:
    """
    DFS recursive solution using a max() variable comparing current node with previous node.
    Use Good-Node counter.
    """

    def dfs(node, maxVal):

        # Base case handling
        if not node:
            return 0

        # Calculate result based on maxVal and current node's value
        result = 1 if node.val >= maxVal else 0

        # Update maxVal for current node
        maxVal = max(maxVal, node.val)

        # Run recursive dfs call on next deeper nodes
        result += dfs(node.left, maxVal)
        result += dfs(node.right, maxVal)

        return result

    # start DFS and return result, use dummy value for maxVal
    return dfs(root, root.val)


if __name__ == "__main__":
    lst = [3, 1, 4, 3, None, 1, 5]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 4")

    lst = [3, 3, None, 4, 2]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 3")

    lst = [1]
    root = create_binary_tree(lst)
    print(goodNodes(root), "expected: 1")
