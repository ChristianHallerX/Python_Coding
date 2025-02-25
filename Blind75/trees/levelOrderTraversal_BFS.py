"""
Level order traversal: Print each tree level on a separate line

The queue (deque) works like a list of nodes of a horizontal tree level
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal_and_print(root):
    if not root:
        return

    # Init deque with root node (double ended queue has O(1) append/pop on both ends)
    queue = deque([root])

    while queue:
        level_vals = []

        for _ in range(len(queue)):

            # always pop (remove) nodes on left side of deque, append nodes on right side of deque
            node = queue.popleft()

            # Append node's VALUE from deque to level-list
            level_vals.append(node.val)

            # If left child exists -> append to deque
            if node.left:
                queue.append(node.left)

            # If right child exists -> append to deque
            if node.right:
                queue.append(node.right)

        # Unpack list and print
        print(*level_vals)


def main():
    # Example tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # Example tree:
    #       1
    #      /  \
    #     2    3
    #    / \  / \
    #   4   5 0  8

    # Test
    level_order_traversal_and_print(root)


if __name__ == "__main__":
    main()
