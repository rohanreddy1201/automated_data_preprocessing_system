# app/main.py
import streamlit as st
import pandas as pd
import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import preprocessing and verification scripts
from scripts.preprocessing_common import common_preprocessing
from scripts.preprocessing_numerical import preprocess_numerical
from scripts.preprocessing_categorical import preprocess_categorical
from scripts.preprocessing_text import preprocess_text
from scripts.preprocessing_time_series import preprocess_time_series
from scripts.feature_engineering import apply_feature_engineering
from scripts.handle_missing_data import handle_missing_data
from scripts.remove_outliers import remove_outliers
from scripts.normalization import normalize_data
from scripts.verification import verify_data

# Set up the title and file uploader
st.title("Automated Data Cleaning and Feature Engineering System")

# File upload section
uploaded_file = st.file_uploader("Upload your data file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    # Display the uploaded data
    st.subheader("Uploaded Data")
    st.dataframe(data.head())

    # User selects preprocessing tasks
    st.subheader("Select Preprocessing and Feature Engineering Tasks")
    
    # Capture selections, but don't trigger processing until "Run Preprocessing" is clicked
    common_preprocess = st.checkbox("Common Preprocessing")
    handle_missing = st.checkbox("Handle Missing Data")
    remove_outliers_opt = st.checkbox("Remove Outliers")
    preprocess_num = st.checkbox("Numerical Data Preprocessing")
    preprocess_cat = st.checkbox("Categorical Data Preprocessing")
    preprocess_txt = st.checkbox("Text Data Preprocessing")
    preprocess_ts = st.checkbox("Time-Series Data Preprocessing")
    normalize = st.checkbox("Normalize Data")
    
    # Feature Engineering options
    st.subheader("Select Feature Engineering Methods")
    feature_pca = st.checkbox("Apply PCA (Principal Component Analysis)")
    feature_poly = st.checkbox("Apply Polynomial Features")
    feature_interaction = st.checkbox("Apply Interaction Features")

    # Initialize a list to track performed tasks
    performed_tasks = []

    # Only run preprocessing and feature engineering when the button is clicked
    if st.button("Run Preprocessing and Feature Engineering"):
        # Step 1: Common Preprocessing
        if common_preprocess:
            data = common_preprocessing(data)
            performed_tasks.append("Common Preprocessing")

        # Step 2: Data Cleaning
        if handle_missing:
            data = handle_missing_data(data)
            performed_tasks.append("Missing Data Handling")
        if remove_outliers_opt:
            data = remove_outliers(data)
            performed_tasks.append("Outliers Removal")
        
        # Step 3: Data Preprocessing
        if preprocess_num:
            data = preprocess_numerical(data)
            performed_tasks.append("Numerical Data Preprocessing")
        if preprocess_cat:
            data = preprocess_categorical(data)
            performed_tasks.append("Categorical Data Preprocessing")
        if preprocess_txt:
            data = preprocess_text(data)
            performed_tasks.append("Text Data Preprocessing")
        if preprocess_ts:
            data = preprocess_time_series(data)
            performed_tasks.append("Time-Series Data Preprocessing")
        
        # Step 4: Data Normalization
        if normalize:
            data = normalize_data(data)
            performed_tasks.append("Data Normalization")
        
        # Step 5: Feature Engineering
        if feature_pca or feature_poly or feature_interaction:
            data = apply_feature_engineering(data, feature_pca, feature_poly, feature_interaction)
            performed_tasks.append("Feature Engineering")
        
        st.subheader("Processed Data")
        st.dataframe(data.head())

    # Verification runs only after preprocessing
    if st.button("Run Verification"):
        verification_results = verify_data(data, performed_tasks)
        st.subheader("Verification Results")
        st.write(verification_results)
