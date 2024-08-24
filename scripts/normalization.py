# scripts/normalization.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data(data):
    # Select numerical columns only
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns

    # Check if there are any numerical columns and they contain data
    if len(num_cols) > 0 and not data[num_cols].empty:
        # Apply MinMaxScaler to scale all numerical data between 0 and 1
        scaler = MinMaxScaler()

        try:
            data[num_cols] = scaler.fit_transform(data[num_cols])
        except ValueError as e:
            print(f"Error during normalization: {e}")

    return data
