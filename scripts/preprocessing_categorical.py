# scripts/preprocessing_categorical.py
import pandas as pd

def preprocess_categorical(data):
    # Select categorical columns
    cat_cols = data.select_dtypes(include=['object']).columns

    for col in cat_cols:
        # Normalize categorical values (convert to lowercase, strip spaces)
        data[col] = data[col].str.lower().str.strip()
        
        # If there are binary categories (e.g., Yes/No), map them to numeric values
        binary_map = {"yes": 1, "no": 0}
        if data[col].nunique() == 2:
            data[col] = data[col].map(binary_map)

    return data
