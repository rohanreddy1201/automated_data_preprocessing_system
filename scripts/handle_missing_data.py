# scripts/handle_missing_data.py
import pandas as pd
import numpy as np

def handle_missing_data(data):
    # Replace non-standard missing values like "?" with NaN
    data.replace("?", np.nan, inplace=True)

    # Separate numerical and categorical columns
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns
    cat_cols = data.select_dtypes(include=['object']).columns

    # 1. Handle missing values in numerical columns by filling with the mean
    data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

    # 2. Handle missing values in categorical columns by filling with the most frequent value (mode)
    for col in cat_cols:
        data[col].fillna(data[col].mode()[0], inplace=True)

    return data
