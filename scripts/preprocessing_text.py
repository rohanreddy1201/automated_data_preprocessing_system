# scripts/preprocessing_text.py
import pandas as pd
import string

def preprocess_text(data):
    # Select text columns (assuming these are 'object' type)
    text_cols = data.select_dtypes(include=['object']).columns

    for col in text_cols:
        # Convert text to lowercase and strip spaces
        data[col] = data[col].str.lower().str.strip()
        
        # Remove punctuation from text columns
        data[col] = data[col].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)) if isinstance(x, str) else x)

        # Handle missing values in text columns (e.g., forward fill or fill with 'unknown')
        data[col] = data[col].fillna('unknown')

    return data
