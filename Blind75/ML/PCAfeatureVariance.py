"""
Give an example how to use PCA on a dataset of 100 columns to find the highest variance.
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# 1. Generate random dataset in numpy and convert to pandas (1000 features, 100 rows)
np.random.seed(42)  # for reproducibility
data = np.random.randn(1000, 100)
df = pd.DataFrame(data, columns=[f"feature_{i+1}" for i in range(100)])


# 2. Standardize the features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)


# 3. Apply PCA
# We define PCA how many components
pca = PCA(n_components=100)
pca.fit(df_scaled)


# 4. Check explained variance results
explained_variances = pca.explained_variance_
explained_variance_ratios = pca.explained_variance_ratio_

# Print variance and relative % of total variance together
print("Explained Variance and Variance Ratio for each principal component:")
for i, (var, var_ratio) in enumerate(
    zip(explained_variances, explained_variance_ratios)
):
    print(f"PC{i+1}: Variance = {var:.4f}, Ratio = {var_ratio:.4%}")


# 5. Identify highest variance
# The first principal component is the one with the highest variance (PC1),
# but here is how you'd programmatically find which PC has the max variance:
max_variance_component = np.argmax(explained_variances) + 1  # +1 for 1-based index
print(
    f"\nHighest variance is in PC{max_variance_component} with variance = "
    f"{explained_variances[max_variance_component - 1]:.4f}\n"
)


# 6. Find the highest loadings feature contributors for PC1 (strongest weight)
loadings = pca.components_  # shape: (n_components, n_features)

# PC1 loadings
pc1_loadings = loadings[0]

# Pair each feature name with its loading
feature_names = df.columns  # assume df is your original DataFrame with 100 columns
pc1_dict = dict(zip(feature_names, pc1_loadings))

# Sort by absolute loading magnitude (highest contributors first)
sorted_pc1 = sorted(pc1_dict.items(), key=lambda x: abs(x[1]), reverse=True)

print("Top 10 loadings/contributors to PC1:")
for feature, loading in sorted_pc1[:10]:
    print(f"{feature}: {loading:.4f}")
