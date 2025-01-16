"""
1.
Calculate the average transaction value for customers
who have made more than 10 purchases in the last 90 days
"""

# SQL answer
"""
SELECT
    customer_id,
    AVG(transaction_value) AS avg_transaction_value
FROM transactions
WHERE transaction_date >= CURRENT_DATE - 90
GROUP BY customer_id
HAVING COUNT(*) > 10;
"""

# Spark Answer
from pyspark.sql.functions import col, avg, count, current_date, date_sub

# 1) Filter transactions to the last 90 days
recent_transactions_df = transactions_df.filter(
    col("transaction_date") >= date_sub(current_date(), 90)
)

# 2) Group by customer_id, then calculate counts & average transaction value
result_df = (
    recent_transactions_df.groupBy("customer_id")
    .agg(
        count("*").alias("purchase_count"),
        avg("transaction_value").alias("avg_transaction_value"),
    )
    .filter(col("purchase_count") > 10)  # 3) Keep only customers with > 10 purchases
)

result_df.show()


"""
2.
How would you use data obtained from an A/B test to determine the difference in campaign effectiveness
and estimate the significance of the outcomes?
"""

"""
1) Setup
- Identify the Goal or Metric (CTR, purchase amount, sign-up rate...)
- Random split users into Baseline and Treatment
- Collect Data, Measure average metric in group

2) Campaign Effectiveness
- Difference in Metrics (DeltaM) between GroupA/B
- Confidence intervals (95% CI) around DeltaM

3) Significance of outcomes
- Hypetheses. h0: no difference between GrupA and B. Alternative hypo
- Choose significance level alpha = 0.05
- Stats Test:
    Means: two-sample t-test or z-test
    Proportions: two-proportion z-test
    Non-Parametric: if skewed distribution
- P value: reject h0 (no difference) if p < alpha

5) Practical considerations:
- Sample Size + Power. large sample to get enough power for small differences
- Data Quality. Biases, random assignment, outliers
- Duration. Account for day-of-week, seasonality
- Multiple Testing
- Practical vs. Statistical difference. Doeas statistical significance have business use?
    Does practical change require statistical significance?

"""


"""
3.
Detail the operational process of a 1D CNN (Convolutional Neural Network).
"""

"""
Key Points:
- 1D vs 2D: only difference is the convolutional kernel dimension and axis. Other concepts ramin the same.
- Use cases: Time Series (forecasting, anomaly detection), Signal Processing (audio...)

1 Input: Sequence of values
2A Conv layer: Kernel Filter with k size, defined function applied across channels.
2B Conv layer: Sliding Window, filter slides along sequence axis from first TS to last TS,
    Dot product between kernel weights and segment
2C Stride (1 or more) and Padding (handling of edges)
3 Non-linear Activation (ReLU, Sigmoid, Tanh)
4 Pooling (optional). Max pooling, average pooling

--- Repeat 2 and 3 as needed ---

5 Stacking Multiple Layers. Early layers = local features. Deep layers = high-level features.
6 Flattening/Global average pooling. Flatten features across temporal dimension for classification output.
7 Output Layer / Fully Connected Dense Layer. Regression. Classification = Softmax 

"""

"""
4.
Explain what the training and loss graphs are for a neural network.
What are some common loss functions used in neural networks, and how do they impact the shape of the loss graph?
Can you compare and contrast the training and loss graphs for neural networks?
How do they inform the optimization and performance of a model?
"""
