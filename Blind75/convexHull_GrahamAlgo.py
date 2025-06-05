import pandas as pd


def find_convex_hull_points(input_points):
    """
    Find the convex hull of a set of points in a Euclidean space.
    The convex hull is the smallest convex polygon that encloses all the points,
    forming a convex polygon in 2D.
    Args:
        input_points: DataFrame with columns representing coordinates
    Returns:
        DataFrame containing only the points that form the convex hull
    """

    # Graham scan algorithm
    if len(input_points.columns) == 2:
        # Rename columns for easier access
        points_df = input_points.copy()
        points_df.columns = ["x", "y"]

        # Find the point with lowest y-coordinate (and leftmost if tie)
        start_idx = points_df["y"].idxmin()
        if points_df["y"].value_counts()[points_df.loc[start_idx, "y"]] > 1:
            # If there are ties, pick the leftmost
            min_y_points = points_df[points_df["y"] == points_df.loc[start_idx, "y"]]
            start_idx = min_y_points["x"].idxmin()

        start_point = points_df.loc[start_idx]

        # Calculate polar angles with respect to start point
        def polar_angle(row):
            dx = row["x"] - start_point["x"]
            dy = row["y"] - start_point["y"]
            return np.arctan2(dy, dx)

        points_df["angle"] = points_df.apply(polar_angle, axis=1)
        points_df["distance"] = (
            (points_df["x"] - start_point["x"]) ** 2
            + (points_df["y"] - start_point["y"]) ** 2
        ) ** 0.5

        # Sort by angle, then by distance
        sorted_points = points_df.sort_values(["angle", "distance"])
        sorted_points = sorted_points[
            sorted_points.index != start_idx
        ]  # Remove start point

        # Cross product to determine if three points make a counter-clockwise turn
        def ccw(p1, p2, p3):
            return (p2["x"] - p1["x"]) * (p3["y"] - p1["y"]) - (p2["y"] - p1["y"]) * (
                p3["x"] - p1["x"]
            )

        # Graham scan
        hull = [start_point]

        for _, point in sorted_points.iterrows():
            # Remove points that make clockwise turn
            while len(hull) > 1 and ccw(hull[-2], hull[-1], point) <= 0:
                hull.pop()
            hull.append(point)

        # Convert hull points back to original format
        hull_indices = [p.name for p in hull]
        return input_points.loc[hull_indices]

    else:
        return input_points


if __name__ == "__main__":
    # Test with example data
    import numpy as np

    points1 = pd.DataFrame([(0, 0), (0, 4), (-4, 0), (5, 0), (0, -6), (1, 0)])
    print("\npoints1 =", points1.values.tolist())
    convex_hull1 = find_convex_hull_points(points1)
    print("convex_hull1 =", convex_hull1.values.tolist())

    points2 = pd.DataFrame([(1, 2), (3, 1), (5, 6)])
    print("\npoints2 =", points2.values.tolist())
    convex_hull2 = find_convex_hull_points(points2)
    print("convex_hull2 =", convex_hull2.values.tolist())
