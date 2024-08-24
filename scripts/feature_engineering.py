# scripts/feature_engineering.py
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from itertools import combinations
import numpy as np

def apply_feature_engineering(data, apply_pca=False, apply_poly=False, apply_interaction=False):
    # Select numerical columns for feature engineering
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns

    # 1. Handle missing values before applying PolynomialFeatures or InteractionFeatures
    data[num_cols] = data[num_cols].fillna(data[num_cols].mean())  # Impute missing values with mean

    # 2. Apply PCA if selected
    if apply_pca and len(num_cols) > 0:
        pca = PCA(n_components=min(len(num_cols), 3))  # Apply PCA with up to 3 components
        transformed_data = pca.fit_transform(data[num_cols])

        # Normalize PCA results to range [0, 1]
        scaler = MinMaxScaler()
        transformed_data = scaler.fit_transform(transformed_data)

        # Add the new PCA components as columns
        for i in range(transformed_data.shape[1]):
            data[f'pca_component_{i+1}'] = transformed_data[:, i]

    # 3. Apply Polynomial Features if selected
    if apply_poly and len(num_cols) > 0:
        poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
        try:
            poly_features = poly.fit_transform(data[num_cols])  # Apply polynomial features
            for i in range(poly_features.shape[1]):
                data[f'poly_feature_{i+1}'] = poly_features[:, i]
        except ValueError as e:
            print(f"Error during Polynomial Features: {e}")

    # 4. Apply Interaction Features if selected
    if apply_interaction and len(num_cols) > 0:
        for col1, col2 in combinations(num_cols, 2):
            try:
                data[f'interaction_{col1}_{col2}'] = data[col1] * data[col2]
            except ValueError as e:
                print(f"Error during Interaction Features: {e}")

    return data
