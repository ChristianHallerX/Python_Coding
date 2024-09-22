"""
261. Graph Valid Tree (medium)

Given 'n' nodes labeled from 0 to n-1 and a list of undirected 'edges' (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
"""


def validTree(n: int, edges: list[list[int]]) -> bool:
    return None


def main():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(n, edges), "expected: True")

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(validTree(n, edges), "expected: False")


if __name__ == "__main__":
    main()
