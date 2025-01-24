"""
Statistics Challenge Imputation

You are provided with a dataset containing personal attributes of individuals. Some columns, notably Eye Color
and Height, have missing values. Your task is to implement
- mode imputation for the 'Eye Color' column and
- KNN imputation for the 'Height' column.

For the KNN imputation, use the features of "Weight" and "Age" to better estimate missing "Height" values.
Do not scale the features before using them. Use KNNImputer from skleanrn.impute with the following settings:

- neighbors: 5
- weights: 'uniform'
- metric: 'nan_euclidean'

When imputing height values, please round the values to one decimal place. After performing the imputations, print
the processed data as a list of lists, where each inner list represents an individual's data.

Example output:

[[1, 'Harry', 23, 172.0, 65, 'Brown'], [2, 'Sally', 45, 171,8, 75, 'Green'], [3, 'Sabrina', 31, 148,0, 58, 'Brown'],
[4, 'Alex', 28, 184.0, 68, 'Brown'], [5, 'Jon', 37, 183.0, 70, 'Brown']]
"""

import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer
from io import StringIO

# Define the dataset as a multi-line string
data_file = """ID,Name,Age,Height,Weight,Eye_Color
1,Harry,23,172,65,
2,Sally,45,,75,Green
3,Sabrina,31,148,58,Brown
4,Alex,29,184,68,
5,Jon,37,183,70,Brown"""

# Use StringIO to simulate a file object
# data_file = "data_missing_values.csv"
# data = pd.read_csv(file_path)
data = pd.read_csv(StringIO(data_file))

# Display initial data for reference
# print("Initial Data:\n", data)

# Configure the KNN imputer for Height and Weight
knn_imputer = KNNImputer(n_neighbors=5, weights="uniform", metric="nan_euclidean")

# Select features for imputing Height (Age and Weight) but do not impute Weight itself
features = data[["Age", "Weight", "Height"]]

# Apply KNN imputation
imputed_data = knn_imputer.fit_transform(features)

# Update the "Height" column with imputed values only
data["Height"] = imputed_data[:, 2]  # The third column corresponds to Height

# Round "Height" to one decimal place
data["Height"] = data["Height"].round(1)

# Configure the mode imputer for Eye Color
mode_imputer = SimpleImputer(strategy="most_frequent")
data["Eye_Color"] = mode_imputer.fit_transform(data[["Eye_Color"]]).flatten()

# Convert the final dataframe to a list of lists
result = data.values.tolist()

# Display the processed result
print(result)
