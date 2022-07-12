"""
70. Climbing Stairs (easy)

You are climbing a staircase. It takes 'n' steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbStairs(n: int) -> int:
    '''This is a decision tree problem (left leaf=1 step, right leaf=2 steps) with recursive depth-first search.
    Dynamic programming component: save tree parts in a dictionary when the part gets repeated.
    Bottom of the tree up, but only the unique steps: Fibonacci-like addition of the previous two results.
    Shift the two variables ('one' and 'two') up the tree for n-1 times.

    Brute-Force time complexity O(n)=2^n. Two to power of height of tree.
    DP memoization time complexity: O(n)=n
    '''

    # the top of the stairs (bottom of tree) always has the same ways to get there
    one, two = 1, 1

    for i in range(n-1):
        # temporary variable that doesn't get overwritten by addition
        temp_one = one
        # add the two variables
        one = one + two
        # shift two becomes one
        two = temp_one

    return one


def main():
    print(climbStairs(n=2), "expected: 2")
    print(climbStairs(n=3), "expected: 3")


if __name__ == '__main__':
    main()
