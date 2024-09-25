"""
261. Graph Valid Tree (medium)

Given 'n' nodes labeled from 0 to n-1 and a list of undirected 'edges' (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Note: You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


def validTree(n: int, edges: list[list[int]]) -> bool:
    """
    A tree may be binary or not. (This is not specified as binary tree)
    Requirements:
    - Are all nodes connected? 5 nodes = 4 connections
    - Are there loops/cycles? Loops are not allowed.
    DFS: visit neighbors and check if they are connected to 0 node (root), cycle, and all nodes visited.
    Time complexity: O(edges+vertices)
    Memory complexity: O(edges+vertices)
    """
    # An empty graph counts as a tree
    if not n:
        return True
    # Global var. Can only visit nodes that are connected. In the end, compare len(visitedNodes) with passed 'n'
    visitedNodes = set()

    # For moving forward, keep track prev node, so we do not visit again.
    # Or else we may get false positives for loops. Start with node value -1 that can't exist

    # Generate dict node (key): empty list with list comprehension
    edgeDict = {i: [] for i in range(n)}

    # Populate lists with connections
    for node1, node2 in edges:
        edgeDict[node1].append(node2)
        edgeDict[node2].append(node1)

    def dfs(node, prevNode):
        """
        Mainly checks for cycles
        """

        # Base case, no more neighbors left to visit
        if not edgeDict[node]:
            return False
        # Base case, cycle
        if node in visitedNodes:
            return False

        visitedNodes.add(node)

        for childNode in edgeDict[node]:
            # Skip going backward
            if childNode == prevNode:
                continue

            # If this child node returns False, return false
            if not dfs(childNode, node):
                return False

        # If all checks pass return True
        return True

    # 1. Start dfs() and check for cycles, 2. were all nodes visited?
    return dfs(node=0, prevNode=-1) and n == len(visitedNodes)


def main():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(n, edges), "expected: True")

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(validTree(n, edges), "expected: False")


if __name__ == "__main__":
    main()
