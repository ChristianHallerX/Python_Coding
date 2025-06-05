import numpy as np

"""
Given two arrays of x and y coordinates of points on a line, and an array of x_hat, return y_hat.
"""


class InterpolateNd:
    def __init__(self, x, y):
        # sort and store x and y
        sort_idx = np.argsort(x)
        self.x_sorted = x[sort_idx]
        self.y_sorted = y[sort_idx]

        # Convenience number of points
        self.n_pts = x.shape[0]

    def __call__(self, x_hat):
        """
        Evaluate the piecewise‐linear interpolant (with linear extrapolation outside the data range).
        x_hat: scalar or 1-D array of query points
        Returns: 1-D array of same shape as x_hat of interpolated (or extrapolated) values.
        """
        # Convert to numpy array in case it isn't
        x_hat_arr = np.asarray(x_hat, dtype=float)
        # Init empty results array
        y_hat = np.empty_like(x_hat_arr, dtype=float)

        # Shortcuts
        x_sorted = self.x_sorted
        y_sorted = self.y_sorted
        N = self.n_pts

        # For each query point, do piecewise linear interp/extrapolation
        for idx, x_query in np.ndenumerate(x_hat_arr):
            # If x_query is exactly one of the known x's, return its y immediately
            # np.searchsorted gives the insertion index in sorted xs
            i = np.searchsorted(x_sorted, x_query)

            if i == 0:
                # x_query <= x_sorted [0] → extrapolate using the first two points
                # (x_sorted[0], y_sorted[0]) and (x_sorted[1], y_sorted[1])
                x0, y0 = x_sorted[0], y_sorted[0]
                x1, y1 = x_sorted[1], y_sorted[1]
                # Find fractional position
                t = (x_query - x0) / (x1 - x0)
                # Multiply fraction vertically
                y_hat[idx] = y0 + t * (y1 - y0)

            elif i == N:
                # x_query > x_sorted [-1] → extrapolate using the last two points
                # (x_sorted[-2], y_sorted[-2]) and (x_sorted[-1], y_sorted[-1])
                x0, y0 = x_sorted[N - 2], y_sorted[N - 2]
                x1, y1 = x_sorted[N - 1], y_sorted[N - 1]
                # Find fractional position
                t = (x_query - x0) / (x1 - x0)
                # Multiply fraction vertically
                y_hat[idx] = y0 + t * (y1 - y0)

            else:
                # x_sorted[i-1] < x_query <= x_sorted[i]
                x0, y0 = x_sorted[i - 1], y_sorted[i - 1]
                x1, y1 = x_sorted[i], y_sorted[i]
                if x_query == x0:
                    y_hat[idx] = y0
                elif x_query == x1:
                    y_hat[idx] = y1
                else:
                    # Find fractional position
                    t = (x_query - x0) / (x1 - x0)
                    # Multiply fraction vertically
                    y_hat[idx] = y0 + t * (y1 - y0)

        return y_hat


def simple_interpolation_test():
    x = np.array([1, 0, 2])
    y = np.array([4, 5, 3])

    x_hat = np.array([0.5, 1.2, 1.0, 1.1])

    interpolant = InterpolateNd(x, y)
    y_hat = interpolant(x_hat)
    print("Interpolated: ", y_hat)
    expected = [4.5, 3.8, 4.0, 3.9]
    print("Expected: ", expected)
    np.testing.assert_allclose(y_hat, expected)


def second_interpolation_test():
    x = np.array([0, 1, 3, 4])
    y = np.array([0, 2, 6, 8])

    x_hat = np.array([2.0, 5.0, -1.0, 3.5])

    interpolant = InterpolateNd(x, y)
    y_hat = interpolant(x_hat)
    print("Interpolated: ", y_hat)
    expected = np.array([4.0, 10.0, -2.0, 7.0])
    print("Expected: ", expected)
    np.testing.assert_allclose(y_hat, expected)


if __name__ == "__main__":
    simple_interpolation_test()
    second_interpolation_test()
