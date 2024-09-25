"""
547. Number of Provinces (medium)

There are 'n' cities. Some of them are connected, while some are not.

If city 'a' is connected directly with city 'b', and city 'b' is connected directly with city 'c',
then city 'a' is connected indirectly with city 'c'.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an 'n' * 'n' matrix 'isConnected' where isConnected[i][j] = 1 if the ith city and the 'j'th

city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


def findCircleNum_UnionFind(isConnected: list[list[int]]) -> int:
    """
    Time Complexity: find() and union() are nearly O(1). The nested loop is O(n(n - 1)/2), or O(n2)
    """
    # Rows is equal to number of nodes, n
    ROWS = len(isConnected)

    # Init global vars
    parent = [i for i in range(ROWS)]
    rank = [1] * ROWS

    def findParent(node):
        """
        Helper function: Find the root parent of a given node
        If the parent is not itself, assign the grandparent node as parent recursively (could also work with While)
        Then return the newly assigned parent
        """
        if parent[node] != node:
            parent[node] = findParent(parent[node])  # Path compression
        return parent[node]

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

    # Difference to 'connectedComponents()' how the union() function loops over the nodes
    # Nested loop through rows and decrement result.
    # The col loop only checks the upper triangle of the matrix, since the information is mirrored in the diagonal
    result = ROWS
    for row in range(ROWS):
        for col in range(row + 1, ROWS):
            if isConnected[row][col] == 1:
                result -= union(row, col)

    return result


def findCircleNum_DFS(isConnected: list[list[int]]) -> int:
    # Total number of cities
    n = len(isConnected)
    # Set to track visited cities
    visited = set()

    def dfs(i):
        """
        Pass i city (row).
        For each city 'j' (column), check if it's connected to the current city 'i' (row).
        """
        # Loop through 'j' (cols)
        for j in range(n):
            if (isConnected[i][j] == 1) and (j not in visited):
                # Mark city 'j' as visited
                visited.add(j)
                # Recursively perform DFS from city 'j'
                dfs(j)

    # Run DFS
    result = 0
    # Loop through rows indices
    for i in range(n):
        if i not in visited:
            visited.add(i)
            # dfs will loop through cols indices
            dfs(i)
            result += 1

    return result


def main():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum_UnionFind(isConnected), "expected: 2")

    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(findCircleNum_UnionFind(isConnected), "expected: 3")

    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum_DFS(isConnected), "expected: 2")

    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(findCircleNum_DFS(isConnected), "expected: 3")


if __name__ == "__main__":
    main()
