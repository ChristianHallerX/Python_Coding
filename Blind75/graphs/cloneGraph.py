"""
133. Clone Graph (medium)

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of
neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a
reference to the cloned graph.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def buildGraph(adjList):
    """
    Helper function
    """
    if not adjList:
        return None

    # Create a dictionary to hold the nodes, key is node value
    nodes = {}

    # First pass: Create all nodes
    for i in range(1, len(adjList) + 1):
        nodes[i] = Node(i)

    # Second pass: Set neighbors
    for i, neighbors in enumerate(adjList):
        node = nodes[i + 1]
        node.neighbors = [nodes[neighbor_val] for neighbor_val in neighbors]

    # Return the reference to the node with val = 1
    return nodes[1]


def graphToAdjList(node):
    """
    Helper function
    """
    if not node:
        return []

    visited = {}
    max_val = 0

    def dfs(node):
        nonlocal max_val
        if node.val in visited:
            return
        visited[node.val] = [neighbor.val for neighbor in node.neighbors]
        max_val = max(max_val, node.val)
        for neighbor in node.neighbors:
            dfs(neighbor)

    dfs(node)

    # Ensure the adjacency list is in order and includes all nodes up to max_val
    adjList = []
    for i in range(1, max_val + 1):
        adjList.append(visited.get(i, []))

    return adjList


def cloneGraph(node: Optional["Node"]) -> Optional["Node"]:
    """
    Clone = Deep Copy
    Returns a new node with neighbor attributes
    Pick node, clone, write new node to hash map, look up neighbors, connect neighbors, move on to neighbor....repeat.
    Hash map (dictionary) to map the old nodes to new nodes and as record which nodes are already done.
    Recursive Depth First Search with hash map.
    Time complexity: O(n) = edged+vertices
    """
    # Global variable
    oldToNew = {}

    def dfs(node):
        "returns copy of a node with its neighbors attched"
        # If old already in dict, then we already copied it, return the new node from the dict
        if node in oldToNew:
            return oldToNew[node]

        # If old node not in dict, create a new node with same value and add to dict
        copy = Node(node.val)
        # Add old node as key, copy as val dict
        oldToNew[node] = copy

        # Run DFS on all the old node's neighbors and append them to copy's neighbors list.
        # Make copies of every single neighbor and append to new node's neighbor list
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(node=neighbor))
        return copy

    # Run dfs and return any of the new graph's nodes
    return dfs(node) if node else None


def main():
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = buildGraph(adjList)
    cloned_node = cloneGraph((node))
    print(graphToAdjList(cloned_node), "expected: [[2, 4], [1, 3], [2, 4], [1, 3]]")

    adjList = [[]]
    node = buildGraph(adjList)
    cloned_node = cloneGraph((node))
    print(graphToAdjList(cloned_node), "expected: [[]]")

    adjList = []
    node = buildGraph(adjList)
    cloned_node = cloneGraph((node))
    print(graphToAdjList(cloned_node), "expected: [[]]")


if __name__ == "__main__":
    main()
