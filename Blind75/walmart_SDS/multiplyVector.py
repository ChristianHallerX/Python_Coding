"""
Write a function that implements the vector cross product for a 2x2 vector. The vector is presented as list of lists.
No numpy. The parameters are 'A', the vector, and 'n' how many times the vector is multiplied with itself.

Cross Product

    Definition: Primarily defined in 3D (and, in a generalized sense, 7D). For vectors uu and vv in 3D,

    Result: Another vector (in 3D).

    Geometric interpretation: The magnitude of u×vu×v is ∥u∥∥v∥sin⁡θ∥u∥∥v∥sinθ, and the direction is perpendicular
    to both uu and vv (given by the right-hand rule).

    Applications:
        Torque (τ=r×Fτ=r×F).
        Finding a normal vector to a plane (e.g., in geometric or graphics calculations).
        Measuring area of a parallelogram spanned by two vectors.

"""


def cross_product_2d(A, n):
    """
    Computes the 2D cross product of two vectors (stored as a 2x2 list)
    and then applies it 'n times' by summing up that cross product n times.

    Parameters
    ----------
    A : list of lists
        A 2x2 list representing two 2D vectors in its rows:
        A = [[x1, y1],
             [x2, y2]]
    n : int
        How many times the cross product should be applied (summed).

    Returns
    -------
    float or int
        The cross product (x1*y2 - y1*x2), summed up n times.
    """
    # Extract components of each row
    x1, y1 = A[0]
    x2, y2 = A[1]

    # 2D cross product => scalar
    cross_val = x1 * y2 - y1 * x2

    # Summed n times (equivalent to cross_val * n)
    return cross_val * n


# Example usage:
A = [[1, 2], [3, 4]]
# cross_val = 1*4 - 2*3 = 4 - 6 = -2
# apply it 3 times => (-2 * 3) = -6
print(cross_product_2d(A, 3))
