# scripts/preprocessing_time_series.py
import pandas as pd

def preprocess_time_series(data):
    # Assume time-series data has a datetime index or a timestamp column
    if 'timestamp' in data.columns:
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data.set_index('timestamp', inplace=True)

    # Ensure data has a consistent frequency (e.g., daily) and handle missing timestamps
    data = data.asfreq('D')  # Convert to daily frequency (modify as needed)

    # Impute missing values for numeric columns
    data = data.fillna(method='ffill').fillna(method='bfill')

    return data
