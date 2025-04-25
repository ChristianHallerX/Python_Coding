import io
from unittest.mock import patch
import json
from collections import defaultdict, deque


# Helper: Simulate `open()`
def mock_open(*args, **kwargs):
    return mock_file


# DAG = acyclical Graph. NO CYCLES allowed.
def run_tasks(json_input):
    with open(json_input, "r") as file:
        data = json.load(file)

    # list
    tasks = data["tasks"]

    # list of lists
    dependencies = data["dependencies"]

    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    for dep in dependencies:
        before, after = dep
        graph[before].append(after)
        in_degree[after] += 1

    queue = deque([task for task in tasks if in_degree[task] == 0])

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # if all tasks are in result, we succeeded
    if len(result) == len(tasks):
        print("All tasks can be finished in this order", result)
    else:
        print("It is not possible to finish all tasks. Maybe there is a cycle?")


if __name__ == "__main__":
    # Convert dict to JSON string, then to a file-like object
    json_data = {"tasks": [0, 1, 2, 3], "dependencies": [[0, 1], [2, 3], [3, 0]]}
    mock_file = io.StringIO(json.dumps(json_data))

    with patch("builtins.open", mock_open):
        run_tasks("fake/path.json")

    json_data = {"tasks": [0, 1, 2, 3], "dependencies": [[0, 1], [1, 2], [2, 0]]}
    mock_file = io.StringIO(json.dumps(json_data))

    with patch("builtins.open", mock_open):
        run_tasks("fake/path.json")
