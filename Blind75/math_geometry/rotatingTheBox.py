"""
1861. Rotating the Box (Medium)

You are given an m x n matrix of characters 'boxGrid' representing a side-view of a box.
Each cell of the box is one of the following:

- A stone '#'
- A stationary obstacle '*'
- Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect
the stones' horizontal positions.

It is guaranteed that each stone in 'boxGrid' rests on an obstacle, another stone, or the bottom of the box.

Return an 'n' * 'm' matrix representing the box after the rotation described above.
"""


def rotateTheBox(boxGrid: list[list[str]]) -> list[list[str]]:

    rowCount, colCount = len(boxGrid), len(boxGrid[0])

    # Initialize the rotated box with empty spaces
    rotatedBox = [["."] * rowCount for _ in range(colCount)]

    # Transpose the box and reverse each row to rotate 90 degrees clockwise
    for rowIndex in range(rowCount):
        for colIndex in range(colCount):
            rotatedBox[colIndex][rowCount - 1 - rowIndex] = boxGrid[rowIndex][colIndex]

    # Simulate gravity for each column in the rotated box
    for colIndex in range(rowCount):  # Adjusted to rowCount to fix misplaced rows
        emptyRow = colCount - 1  # Adjusted to colCount to correctly drop boxes

        for rowIndex in range(colCount - 1, -1, -1):
            if rotatedBox[rowIndex][colIndex] == "*":
                # Obstacle encountered, reset emptyRow position
                emptyRow = rowIndex - 1
            elif rotatedBox[rowIndex][colIndex] == "#":
                # Move the box down to the lowest available position
                rotatedBox[rowIndex][colIndex] = "."
                rotatedBox[emptyRow][colIndex] = "#"
                emptyRow -= 1

    return rotatedBox


def main():
    boxGrid = [["#", ".", "#"]]
    rotatedBox = rotateTheBox(boxGrid)
    for row in rotatedBox:
        print(row)
    print(
        """
expected:
[["."],
 ["#"],
 ["#"]] 
"""
    )

    boxGrid = [["#", ".", "*", "."], ["#", "#", "*", "."]]
    rotatedBox = rotateTheBox(boxGrid)
    for row in rotatedBox:
        print(row)
    print(
        """
expected:
[["#","."],
 ["#","#"],
 ["*","*"],
 [".","."]]
 """
    )

    boxGrid = [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."],
    ]
    rotatedBox = rotateTheBox(boxGrid)
    for row in rotatedBox:
        print(row)
    print(
        """
expected:
[[".","#","#"],
 [".","#","#"],
 ["#","#","*"],
 ["#","*","."],
 ["#",".","*"],
 ["#",".","."]]
 """
    )


if __name__ == "__main__":
    main()
