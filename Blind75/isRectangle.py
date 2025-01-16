from math import sqrt


def helper_distance(p1, p2):
    """
    Calculate the Euclidean distance between two points.
    square_root((x1 - x2)^2 + (y1 - y2)^2)
    """
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def is_rectangle(p1, p2, p3, p4):
    """
    Check if four points can form a rectangle calculating 6 point distances.
    - Square 2 pairs: 4 equal, 2 diagonals
    - Rectangle 3 pairs: 2 long, 2 short, 2 diagonals
    - No rectangle: 4-6 unique lengths, no pairs?
    """
    # Calculate all pairwise distances.
    distances = [
        helper_distance(p1, p2),
        helper_distance(p1, p3),
        helper_distance(p1, p4),
        helper_distance(p2, p3),
        helper_distance(p2, p4),
        helper_distance(p3, p4),
    ]

    # Count distances in a dictionary/hash map {distance: count}
    unique_distances = {}
    for dist in distances:
        unique_distances[dist] = unique_distances.get(dist, 0) + 1

    #  More than 3 counts (items) in dict is not a rectangle. Squares have only two counts (items).
    if len(unique_distances.values()) > 3:
        return print("The points do NOT form a rectangle.")
    else:
        return print("The points form a rectangle.")


if __name__ == "__main__":
    p1 = (0, 0)
    p2 = (0, 2)
    p3 = (3, 0)
    p4 = (3, 2)
    is_rectangle(p1, p2, p3, p4)

    p1 = (0, 0)
    p2 = (1, 2)
    p3 = (3, 0)
    p4 = (4, 5)
    is_rectangle(p1, p2, p3, p4)
