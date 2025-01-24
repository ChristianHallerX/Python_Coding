"""
Tensor Singular Value Decomposition

In the Python file, write a PyTorch program to create a 2-dimensional tensor of size 5x5, initialized with
random values between -1 and 1. Be sure to set torch seed to 0.

Next, compute this tensor's singular value decomposition (SVD) using the torch.svd() function and square each of the
singular values to the eigenvalues of the original tensor and print it. Finally, convert the eigenvalues to
a Python list and Print it.
"""

import torch

# Set the random seed for reproducibility
torch.manual_seed(0)

# Create a 2-dimensional tensor of size 5x5 with random values between -1 and 1
tensor = (torch.rand((5, 5)) * 2) - 1

# Perform singular value decomposition (SVD)
u, s, v = torch.svd(tensor)

# Square each of the singular values to compute the eigenvalues
eigenvalues = s**2

# Convert eigenvalues to a Python list and print
eigenvalues_list = eigenvalues.tolist()
print(eigenvalues)
print(eigenvalues_list)
