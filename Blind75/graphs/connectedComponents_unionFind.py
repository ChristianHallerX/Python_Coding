"""
323 Number of Connected Components in an Undirected Graph (medium)

Compare LC 547 Number of Provinces

You have a graph of 'n' nodes. You are given an integer 'n' and an array 'edges' where edges[i] = [ai, bi] indicates
that there is an edge between 'ai' and 'bi' in the graph

Return the number of connected components in the graph.
"""


def countComponents(n: int, edges: list[list[int, int]]) -> int:
    """
    Normal DFS
    -------------------
    Since the components are not conencted, we need to start DFS multiple times at unvisited nodes
    -> check if node in a visited nodes set.
    For each DFS search, increment components counter. The search will mark all connected nodes as visited.
    Start next DFS at an unvisited node and increment counter.
    Time complexity: O(edges+node)

    Union Find (forest of trees)
    -------------------
    1. Parent list of nodes
    2. Rank list
    Parent list usually every node is parent of itself, then we re-assign and connect nodes by
    merging like a binary tree.
    Merge/union nodes if parents rank are different and decrement n each time by one. If no union, do not decrement.

    """
    # Initially, each node is the parent of itself
    parent = [i for i in range(n)]

    # Initial rank of 1 for each node (connected to itself)
    # Rank equals the size of the connected component of a node.
    rank = [1] * n

    def findParent(node1):
        """
        Helper function: Find the root parent of a given node
        """
        # Initially, each node is each own parent
        result = node1

        # While result not equal to itself node, go up until can't go any higher
        while result != parent[result]:

            # Assign grandparent if exists (if not exists, this will do nothing)
            parent[result] = parent[parent[result]]

            # Update result
            result = parent[result]

        return result

    def union(node1, node2):
        """
        Helper function:
        Return 0 if no union for decerement,
        Return 1 if successful union for decrement.
        """
        # Find the root parents of each of these nodes
        p1, p2 = findParent(node1), findParent(node2)

        # Same parent -> already unioned nodes, skip
        if p1 == p2:
            return 0

        # Do the union by re-assigning parents from the findParent() function
        # For example, one node may be connected to parent=root (rank=2),
        # a new node is still connected to parent=itself (rank=1).
        # -> Re-assign parents and increase rank (size of connected component)
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        # Reverse rank case
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1

    # Apply function on edges
    result = n
    for node1, node2 in edges:
        # Every time we complete a successful union, decrement result by one, else do nothing
        result -= union(node1, node2)

    return result


def main():
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(countComponents(n, edges), "expected: 2")

    n = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
    print(countComponents(n, edges), "expected: 2")

    n = 3
    edges = [[0, 1], [0, 2]]
    print(countComponents(n, edges), "expected: 1")


if __name__ == "__main__":
    main()
