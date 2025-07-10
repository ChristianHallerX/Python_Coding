import random
import heapq


def is_solvable(puzzle, n):
    """
    Check if a puzzle is solvable.
    The puzzle is represented as a flat list where 0 represents the empty cell.
    For odd n, the puzzle is solvable if the inversion count is even.
    For even n, the puzzle is solvable if:
      - the blank is on an even row from the bottom and the inversion count is odd, or
      - the blank is on an odd row from the bottom and the inversion count is even.
    """
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1

    if n % 2 == 1:  # Odd grid
        return inversions % 2 == 0
    else:  # Even grid: need to consider the row of the blank (0)
        blank_index = puzzle.index(0)
        blank_row_from_bottom = n - (blank_index // n)
        if blank_row_from_bottom % 2 == 0:  # blank on even row from bottom
            return inversions % 2 == 1
        else:  # blank on odd row from bottom
            return inversions % 2 == 0


def generate_random_grid(n):
    """
    Generates a random n x n sliding puzzle configuration.
    It continues shuffling until a solvable puzzle is found.
    """
    puzzle = list(range(n * n))  # 0 represents the empty cell.
    while True:
        random.shuffle(puzzle)
        if is_solvable(puzzle, n):
            break
    # Convert the flat list into an n x n grid
    grid = [puzzle[i * n : (i + 1) * n] for i in range(n)]
    return grid


def get_goal_state(n):
    """
    Returns the goal state as a tuple of tuples.
    The numbers are in ascending order with the empty (0) in the last cell.
    """
    goal_list = list(range(1, n * n)) + [0]
    goal_grid = tuple(tuple(goal_list[i * n : (i + 1) * n]) for i in range(n))
    return goal_grid


def manhattan_distance(state, n):
    """
    Computes the sum of Manhattan distances of the tiles from their goal positions.
    The state is a tuple of tuples.
    """
    distance = 0
    for i in range(n):
        for j in range(n):
            value = state[i][j]
            if value != 0:
                # The goal position for value (1-indexed) is:
                goal_row = (value - 1) // n
                goal_col = (value - 1) % n
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance


def get_neighbors(state):
    """
    Returns a list of neighbor states from the current state.
    Each neighbor is a tuple containing the move (as a string) and the new state.
    The state is a tuple of tuples. The blank is denoted by 0.
    """
    n = len(state)
    # Locate the blank (0)
    blank_row, blank_col = None, None
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                blank_row, blank_col = i, j
                break
        if blank_row is not None:
            break

    neighbors = []
    # Define possible moves with row, column offsets.
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    for move, (di, dj) in moves.items():
        new_row = blank_row + di
        new_col = blank_col + dj
        if 0 <= new_row < n and 0 <= new_col < n:
            # Create a new state by swapping the blank with the adjacent cell.
            new_state = [
                list(row) for row in state
            ]  # Copy state to a mutable list of lists.
            new_state[blank_row][blank_col], new_state[new_row][new_col] = (
                new_state[new_row][new_col],
                new_state[blank_row][blank_col],
            )
            # Convert back to tuple of tuples for immutability.
            neighbors.append((move, tuple(tuple(row) for row in new_state)))
    return neighbors


def a_star(start, goal, n):
    """
    Implements the A* algorithm to find a path from the start state to the goal state.
    Returns the list of moves (as strings) leading to the goal.
    """
    # The priority queue stores entries as (f_score, g_score, current_state, path_taken)
    open_set = []
    start_h = manhattan_distance(start, n)
    heapq.heappush(open_set, (start_h, 0, start, []))
    visited = {start: 0}  # Track the best g_score (cost so far) for each state.

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path  # Found the solution!

        for move, neighbor in get_neighbors(current):
            tentative_g = g + 1  # Each move has a cost of 1.
            if neighbor not in visited or tentative_g < visited[neighbor]:
                visited[neighbor] = tentative_g
                new_path = path + [move]
                f_score = tentative_g + manhattan_distance(neighbor, n)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, new_path))

    return (
        None  # If no solution is found (should not happen if the puzzle is solvable).
    )


def main():
    # 1. Generate Random Start (solvable)
    n = int(input("Enter grid size n (for example, 3 for a 3x3 grid): "))
    grid = generate_random_grid(n)
    print("\nRandomly generated puzzle:")
    for row in grid:
        print(row)

    # 2. Generate Goal. Represent the puzzle as a tuple of tuples for immutability.
    start_state = tuple(tuple(row) for row in grid)
    goal_state = get_goal_state(n)
    print("\nGoal state:")
    for row in goal_state:
        print(row)

    # 3. Run A* and order Start -> Goal
    solution = a_star(start_state, goal_state, n)
    if solution is None:
        print("\nNo solution found!")
    else:
        print("\nSolution found in", len(solution), "moves:")
        print(solution)


if __name__ == "__main__":
    main()
