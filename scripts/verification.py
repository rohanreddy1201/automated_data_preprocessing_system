import pandas as pd

def verify_data(data, tasks):
    results = []
    
    # 1. Check for missing values if "Handle Missing Data" was selected
    if "Missing Data Handling" in tasks:
        if data.isnull().sum().sum() == 0:
            results.append("Verification passed: No missing values.")
        else:
            missing_info = data.isnull().sum().to_dict()
            results.append(f"Verification failed: Missing values still present in columns: {missing_info}")
    
    # 2. Check for outliers if "Outliers Removal" was selected
    if "Outliers Removal" in tasks:
        num_cols = data.select_dtypes(include=['float64', 'int64']).columns
        outliers_exist = False
        for col in num_cols:
            if ((data[col] - data[col].mean()).abs() > 3 * data[col].std()).any():
                outliers_exist = True
                break
        if not outliers_exist:
            results.append("Verification passed: No outliers detected.")
        else:
            results.append("Verification failed: Outliers still present.")
    
    # 3. Check for proper normalization if "Data Normalization" was selected
    if "Data Normalization" in tasks:
        num_cols = data.select_dtypes(include=['float64', 'int64']).columns
        for col in num_cols:
            if not (data[col].min() >= 0 and data[col].max() <= 1):
                results.append(f"Verification failed: Column {col} not properly normalized.")
                break
        else:
            results.append("Verification passed: Data properly normalized.")
    
    # 4. Check for numerical data preprocessing if selected
    if "Numerical Data Preprocessing" in tasks:
        if data.select_dtypes(include=['float64', 'int64']).isnull().sum().sum() == 0:
            results.append("Verification passed: Numerical data preprocessing successful.")
        else:
            results.append("Verification failed: Issues found in numerical data preprocessing.")
    
    # 5. Check for categorical data preprocessing if selected
    if "Categorical Data Preprocessing" in tasks:
        if data.select_dtypes(include(['object'])).isnull().sum().sum() == 0:
            results.append("Verification passed: Categorical data preprocessing successful.")
        else:
            results.append("Verification failed: Issues found in categorical data preprocessing.")
    
    # 6. Check for text data preprocessing if selected
    if "Text Data Preprocessing" in tasks:
        if data.select_dtypes(include(['object'])).isnull().sum().sum() == 0:
            results.append("Verification passed: Text data preprocessing successful.")
        else:
            results.append("Verification failed: Issues found in text data preprocessing.")
    
    # 7. Check for time-series data preprocessing if selected
    if "Time-Series Data Preprocessing" in tasks:
        if 'timestamp' in data.columns:
            if pd.infer_freq(data.index) is not None:
                results.append("Verification passed: Time-series data preprocessing successful.")
            else:
                results.append("Verification failed: Issues found in time-series data preprocessing.")
    
    # 8. Check if PCA was applied correctly
    if "Feature Engineering" in tasks and "PCA" in tasks:
        pca_cols = [col for col in data.columns if 'pca_component' in col]
        if len(pca_cols) > 0:
            results.append("Verification passed: PCA applied successfully.")
        else:
            results.append("Verification failed: PCA not applied.")
    
    # 9. Check if polynomial features were applied correctly
    if "Feature Engineering" in tasks and "Polynomial Features" in tasks:
        poly_cols = [col for col in data.columns if 'poly_feature' in col]
        if len(poly_cols) > 0:
            results.append("Verification passed: Polynomial features applied successfully.")
        else:
            results.append("Verification failed: Polynomial features not applied.")
    
    # 10. Check if interaction features were applied correctly
    if "Feature Engineering" in tasks and "Interaction Features" in tasks:
        interaction_cols = [col for col in data.columns if 'interaction' in col]
        if len(interaction_cols) > 0:
            results.append("Verification passed: Interaction features applied successfully.")
        else:
            results.append("Verification failed: Interaction features not applied.")

    # If no results are added, return a default message
    if not results:
        results.append("No verification steps were performed or no issues were detected.")

    return "\n".join(results)
