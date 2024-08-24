# scripts/preprocessing_numerical.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_numerical(data):
    # Select numerical columns only, excluding columns that are meant to be categorical (like IDs)
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns

    # Apply MinMaxScaler to ensure all values are in the range [0, 1]
    scaler = MinMaxScaler()
    data[num_cols] = scaler.fit_transform(data[num_cols])

    # Ensure no invalid values (e.g., NaN) exist after transformation
    data[num_cols] = data[num_cols].fillna(0)

    return data
