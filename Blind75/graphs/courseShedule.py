"""
207. Course Schedule (medium)

There are a total of 'numCourses' courses you have to take, labeled from '0' to 'numCourses - 1'.
You are given an array 'prerequisites' where prerequisites[i] = [ai, bi] indicates that you must take
course 'bi' first if you want to take course 'ai'.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return 'True' if you can finish all courses.
Otherwise, return 'False'.
"""


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Assume courses are nodes, prerequisites are edges connections between nodes [0,1] points from 0->1.
    The vector points at what you have to take first.

    Solve with DFS. And prereq dictionary. course -> prereq list (edges pointing at course)
    Prerequisites are edges that point from the current node to another prereq course node.
    Prereq cycles between two nodes make them impossible to complete
    """
    # Create dict with key = course number, value = empty list, global variable
    prereqDict = {i: [] for i in range(numCourses)}

    # Fill the dict values (empty lists) with the nodes that are pointed at (prereqs)
    # This bundles the information per node
    for course, prereq in prerequisites:
        prereqDict[course].append(prereq)

    # Tracking global variable
    visitSet = set()

    def dfs(course):
        """
        DFS runs recursively on a node's prereq nodes from the dict.
        """
        # Base case 1. Course cannot be completed. Course already in set -> circular order.
        if course in visitSet:
            return False
        # Base case 2. Course has no outward going edges. No prerequisites. Can definitely be completed.
        if not prereqDict[course]:
            return True

        visitSet.add(course)

        # Loop through the prereqs and run dfs on all of them. Stop loop and return False if any dfs returns False
        for pre in prereqDict[course]:
            if not dfs(pre):
                return False

        # Remove from global var when dfs() is run on the next course
        visitSet.remove(course)

        # Delete prereqs list after True, so in next visit(??) it returns True again immediately as base case 1
        prereqDict[course] = []

        # Not base case, and dfs() returned True, also return True here
        return True

    # Run dfs on all courses individually. If any return False, immediately return False (like inside the dfs())
    for course in range(numCourses):
        if not dfs(course):
            return False
    return True


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    print(canFinish(numCourses, prerequisites), "expected: True")

    # To finish course 0, we need to complete 1. But to complete 1, we need to complete 0 first. It's a cycle.
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(canFinish(numCourses, prerequisites), "expected: False")

    # To finish course 0, we need to complete 1. But to complete 1, we need to complete 0 first. It's a cycle.
    numCourses = 5
    prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    print(canFinish(numCourses, prerequisites), "expected: True")


if __name__ == main():
    main()
