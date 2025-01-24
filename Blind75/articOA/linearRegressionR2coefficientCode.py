"""
Linear Regression R2 Coefficient

In the Python file, write a script that will perform a linear regression on the data in the 'data.txt' and then
calculate the coefficient of determination (R2) of the prediction.

The first line in the 'data.txt' represents the X column, and the second represents the Y column.
Your output should be in the following format:

'coefficient: 0.353412...'
"""

# Perform linear regression
from sklearn.linear_model import LinearRegression
import numpy as np

# with open("data.txt", "r") as file:
#     lines = file.readlines()

x_line = "5 15 25 35 45 55"
y_line = "10 12 25 6 27 36"

# Parse the data into x and y lists
x = list(map(int, x_line.strip().split()))
y = list(map(int, y_line.strip().split()))

# Reshape x for scikit-learn compatibility
x = np.array(x).reshape(-1, 1)
y = np.array(y)

# Fit the linear regression model
model = LinearRegression()
model.fit(x, y)

# Calculate the coefficient of determination (R^2)
r_squared = model.score(x, y)

# Output the result
print(f"coefficient: {r_squared}")
