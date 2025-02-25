"""
102. Binary Tree Level Order Traversal (medium)

Given the root of a binary tree, return the level order traversal of its nodes' values.

(i.e., from left to right, level by level).
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


def levelOrder(root: TreeNode) -> list[list[int]]:
    """
    Add each level's nodes to a level-sublist. Return a list of lists. -> Breadth First Search BFS with deque
    Append to right, pop on left onto level-sublist. FIFO. Like a conveyor belt moving left.
    Use collections.deque() (pronounce 'deck')
    Pattern: while-loop q not empty, level-for loop on length of q

    Time Complexity: O(n). Visit each node once.
    Space complexity: queue could have at any given time up to n/2 elements. O(n/2) -> simplifies to O(n)
    """
    result = []

    # Initialize q
    q = deque()
    q.append(root)

    while q:  # Run until q empty
        qLen = len(q)
        level_sublist = []

        # Loop over nodes of this level (add next level children, drop current level)
        for i in range(qLen):
            # Remove first node from deque, add to level_sublist, and append child nodes to right of q.
            node = q.popleft()
            if node:  # Only do if not None, could be None
                level_sublist.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level_sublist:  # Ignore empty level lists (all None)
            print(level_sublist)
            result.append(level_sublist)

    return result


def main():
    root = create_binary_tree([3, 9, 20, None, None, 15, 7])
    print(levelOrder(root), "expected: [[3], [9, 20], [15, 7]]")

    root = create_binary_tree([1])
    print(levelOrder(root), "expected: [[1]]")

    root = create_binary_tree([])
    print(levelOrder(root), "expected: []")


if __name__ == "__main__":
    main()
