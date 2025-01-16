from pyspark.sql.functions import col, coalesce
from pyspark.sql import SparkSession

"""
Intuition:
1. Filter down to Null values for performance and NOT Null values
2. Left join and horizontally coalesce new columns
3. Union the filled DF and the the NOT Null df
"""

# Create DFs
key_data = [(1, "Description A"), (2, "Description B"), (3, "Description C")]
key_df = spark.createDataFrame(key_data, ["ID", "Description"])

big_data = [
    (1, None),
    (2, "Description B"),
    (None, "Description X"),
    (None, None),
    (3, None),
    (4, None),
    (None, "Description Y"),
    (5, None),
    (6, "Description F"),
    (None, None),
    (7, None),
    (None, "Description Z"),
    (8, "Description H"),
    (None, None),
    (9, None),
    (10, None),
    (None, "Description W"),
    (11, None),
    (12, None),
    (None, None),
]
big_df = spark.createDataFrame(big_data, ["ID", "Description"])

# Filter rows where ID or Description is NULL
rows_with_nulls = big_df.filter((col("ID").isNull()) | (col("Description").isNull()))

# Filter rows where both ID and Description are not NULL
rows_without_nulls = big_df.filter(
    (col("ID").isNotNull()) & (col("Description").isNotNull())
)

# Perform the join and fill nulls on the filtered rows
filled_rows = rows_with_nulls.join(
    key_df, rows_with_nulls["ID"] == key_df["ID"], how="left"
).select(
    coalesce(rows_with_nulls["ID"], key_df["ID"]).alias("ID"),
    coalesce(rows_with_nulls["Description"], key_df["Description"]).alias(
        "Description"
    ),
)

# Combine the updated rows with the unchanged rows
final_df = filled_rows.union(rows_without_nulls)

# Show the final DataFrame
final_df.show()
