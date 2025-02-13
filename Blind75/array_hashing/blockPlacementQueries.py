"""
3161. Block Placement Queries (Hard)

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array 'queries', which contains two types of queries:

- For a query of type 1, queries[i] = [1, x].
    Build an obstacle at distance x from the origin.
    It is guaranteed that there is no obstacle at distance x when the query is asked.

- For a query of type 2, queries[i] = [2, x, sz].
    Check if it is possible to place a block of size 'sz' anywhere in the range [0, x] on the line,
    such that the block entirely lies in the range [0, x].
    A block cannot be placed if it intersects with any obstacle, but it may touch it.
    Note that you do not actually place the block. Queries are separate.

Return a boolean array results, where results[i] is True if you can place the block specified in the ith query of
type 2, and False otherwise.

Note: implementation fails performance requirements for very long queries.
"""


def getResults(queries: list[list[int]]) -> list[bool]:
    results = []
    obstacles = []

    for query in queries:
        if query[0] == 1:
            # Place an obstacle at the given position.
            obstacles.append(query[1])
        else:
            # For a block placement query: [2, x, size]
            x, size = query[1], query[2]

            # Sort obstacles and filter those within [0, x].
            obstacles.sort()
            obs = [pos for pos in obstacles if 0 <= pos <= x]

            canPlace = False
            if not obs:
                # No obstacles in [0, x] means the entire interval [0, x] is free.
                if x >= size:
                    canPlace = True
            else:
                # Check gap before the first obstacle.
                if obs[0] >= size:
                    canPlace = True

                # Check gaps between consecutive obstacles.
                for i in range(1, len(obs)):
                    if obs[i] - obs[i - 1] >= size:
                        canPlace = True
                        break

                # Check gap after the last obstacle.
                if x - obs[-1] >= size:
                    canPlace = True

            results.append(canPlace)

    return results


def main():
    queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]
    print(getResults(queries), "expected: [False, True, True]")

    queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
    print(getResults(queries), "expected: [True, True, False]")


if __name__ == "__main__":
    main()
