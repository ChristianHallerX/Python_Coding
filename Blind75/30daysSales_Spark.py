"""
Let’s say you have a PySpark DataFrame called 'sales' with the following schema:

root
 |-- customer_id: string (nullable = true)
 |-- purchase_date: string (nullable = true)
 |-- amount: double (nullable = true)

Write a PySpark code snippet to calculate the total amount spent by each customer in the last 30 days.
"""

### Optional imports and session in Databricks
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TotalSpentLast30Days").getOrCreate()

### Load 'sales' table according to the environment

# Convert col `purchase_date` to a timestamp format
sales = sales.withColumn("purchase_date", F.to_timestamp("purchase_date", "yyyy-MM-dd"))

# Get the current TS
current_date = F.current_timestamp()

# Filter timestamp column >(current TS - 30) (date subtraction)
last_30_days_sales = sales.filter(
    F.col("purchase_date") >= F.date_sub(current_date, 30)
)

# Group by customer, aggregate sum the 'amount' (optional alias)
total_amount_per_customer = last_30_days_sales.groupBy("customer_id").agg(
    F.sum("amount").alias("total_amount")
)

# Show the result
total_amount_per_customer.show()
# display(total_amount_per_customer)

mapping

# 1. Write a sql query moving average on sales past 3 months
# 2. Two tables. Small table all filled in with 'ID' and 'Description'.
#   Big table with col 'ID' containing some Null and 'Description' containing some Null.
#   Fill in all cells.
#   Join and union question
