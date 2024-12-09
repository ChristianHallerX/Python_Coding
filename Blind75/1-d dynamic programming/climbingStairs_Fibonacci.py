"""
70. Climbing Stairs (easy)

You are climbing a staircase. It takes 'n' steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs(n: int) -> int:
    """
    #Solve recursively with DFS decision tree that explores all step possibility paths.
    #With bottom up dynamic programming.

    #Base case: steps add up exactly to total stair height.
    #Base case: steps add up to more than stair height.
    #Some branches (intermediate steps) of the decision tree are going to be solved multiple times
    #-> store repeated work in memory (memoization), solve each sub-problem once.

    Plot twist: Bottom up totals of this problem calculate like Fibonacci sequence. 1, 1, 2, 3...
    Time complexity: O(n)
    Memory complexity: O(1) three values
    """

    # Starting totals for Fibonacci
    one, two = 1, 1

    # Update vars one and two for n times
    for i in range(n - 1):
        temp_one = one
        one = one + two
        two = temp_one
    return one


def main():
    n = 2
    print(climbStairs(n), "expected: 2, explanation: 1+1 or 2")

    n = 3
    print(climbStairs(n), "expected: 3, explanation: 1+1+1 or 1+2 or 2+1")

    n = 5
    print(climbStairs(n), "expected: 8")


if __name__ == "__main__":
    main()
