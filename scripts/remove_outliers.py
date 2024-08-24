# scripts/remove_outliers.py
import pandas as pd
import numpy as np

def remove_outliers(data):
    # Apply outlier removal only on numerical columns
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns

    for col in num_cols:
        # Use Z-scores to identify outliers
        z_scores = np.abs((data[col] - data[col].mean()) / data[col].std())
        data = data[(z_scores < 3)]  # Retain data points within 3 standard deviations

    return data
