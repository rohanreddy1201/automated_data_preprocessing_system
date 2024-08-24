# scripts/preprocessing_common.py
import pandas as pd
import numpy as np

def common_preprocessing(data):
    # 1. Convert non-standard missing values like "?" to NaN
    data.replace("?", np.nan, inplace=True)
    
    # 2. Normalize categorical data (convert to lowercase, strip spaces)
    cat_cols = data.select_dtypes(include=['object']).columns
    data[cat_cols] = data[cat_cols].apply(lambda x: x.str.lower().str.strip())
    
    # 3. Convert age ranges into numeric midpoints
    if 'age' in data.columns:
        age_map = {
            '[0-10)': 5, '[10-20)': 15, '[20-30)': 25, '[30-40)': 35, '[40-50)': 45,
            '[50-60)': 55, '[60-70)': 65, '[70-80)': 75, '[80-90)': 85, '[90-100)': 95
        }
        data['age'] = data['age'].map(age_map)
    
    # 4. Convert binary categorical columns with "Yes"/"No" or "Male"/"Female" to binary values
    binary_map = {"yes": 1, "no": 0, "male": 1, "female": 0}
    for col in data.columns:
        if data[col].nunique() == 2:  # Check if column has only 2 unique values
            data[col] = data[col].map(binary_map)
    
    # 5. Remove duplicate rows if any
    data.drop_duplicates(inplace=True)
    
    # 6. Fill missing values in numeric columns with their mean
    data_numeric = data.select_dtypes(include=['number']).fillna(data.mean(numeric_only=True))
    
    # 7. Fill remaining missing values in non-numeric columns with forward fill
    data_non_numeric = data.select_dtypes(exclude=['number']).fillna(method='ffill')
    
    # Combine back numeric and non-numeric columns
    data = pd.concat([data_non_numeric, data_numeric], axis=1)
    
    return data
