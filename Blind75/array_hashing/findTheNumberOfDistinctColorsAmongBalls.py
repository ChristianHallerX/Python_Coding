"""
3160. Find the Number of Distinct Colors Among the Balls (Medium)

You are given an integer 'limit' and a 2D array 'queries' of size 'n' * 2.

There are 'limit' + 1 balls with distinct labels in the range [0, 'limit'].
Initially, all balls are uncolored.
For every query in 'queries' that is of the form [x, y], you mark ball 'x' with the color 'y'.
After each query, you need to find the number of distinct colors among the balls.

-> Return an array 'result' of length 'n', where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.
"""


def queryResults(limit: int, queries: list[list[int]]) -> list[int]:
    """
    limit (int)    limit + 1 = number of balls, not really used
    queries (list of lists)    instructions which ball to paint in what color id

    Time Complexity:    O(n) number of queries
    Space Complexity:    O(limit), i.e., balls for both, ball_colors list and color_count dictionary
    """
    # dict to document latest color for balls that were painted (only those!)
    ball_colors = {}
    # dict to track freq of each color. color: count
    color_count = {}
    result = []

    # go over all queries and paint/over paint the balls, document in the color_count dict and ball_colors list
    for ball, color in queries:
        # has been colored previously, old color gets overwritten
        if ball in ball_colors:
            old_color = ball_colors[ball]

            # decrease or delete count of old color from dict before over-painting
            color_count[old_color] -= 1
            if color_count[old_color] == 0:
                del color_count[old_color]

        # Color the ball with the new color in th list
        ball_colors[ball] = color
        # Increment frequency in dict
        color_count[color] = color_count.get(color, 0) + 1

        # after updating colors of this query, get the unique colors from the number of dict keys
        result.append(len(color_count))

    return result


def main():
    limit = 4
    queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
    print(queryResults(limit, queries), "expected: [1,2,2,3]")

    limit = 4
    queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    print(queryResults(limit, queries), "expected: [1,2,2,3,4]")


if __name__ == "__main__":
    main()
