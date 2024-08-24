# Automated Data Cleaning and Feature Engineering System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-green)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Overview

The **Automated Data Cleaning and Feature Engineering System** is a powerful tool designed to streamline and simplify the process of preparing datasets for machine learning tasks. It offers automated cleaning, handling of missing data, outlier detection, and feature engineering techniques such as **PCA**, **polynomial features**, and **interaction terms**.

This tool is built using **Streamlit** and **scikit-learn**, providing a user-friendly interface for data preprocessing and feature engineering with robust verification mechanisms.

## Features

- **Data Preprocessing**:
  - Handle missing values (mean, mode imputation).
  - Normalize numeric data.
  - Categorical data cleaning and encoding.
  - Text data preprocessing.
  - Time-series preprocessing with consistent frequency.
  
- **Feature Engineering**:
  - Apply **PCA** (Principal Component Analysis) for dimensionality reduction.
  - Generate **polynomial features** and **interaction features**.
  
- **Outlier Detection**:
  - Detect and remove outliers based on standard deviation.

- **Verification**:
  - Verify the success of preprocessing tasks such as missing value handling, normalization, outlier removal, and feature engineering.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/automated-data-cleaning-feature-engineering-system.git
   ```
   
2. Navigate to the project directory:
    ```bash
    cd automated-data-cleaning-feature-engineering-system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. To run the Streamlit app, use the following command:
  ```bash
  streamlit run app/main.py
  ```
2. Upload your dataset (CSV or Excel format) and select the preprocessing tasks and feature engineering methods you want to apply.
3. Review the processed data and verification results directly in the app.

### Example Workflow
Upload Dataset: Start by uploading your dataset in .csv or .xlsx format.
Select Preprocessing Tasks: Choose tasks such as handling missing data, outlier removal, normalization, and text processing.
Feature Engineering: Apply PCA, Polynomial Features, or Interaction Features.
Verify Results: Run the verification process to check if the data was processed successfully.

### Project Structure
```bash
├── app/
│   ├── main.py              # Main Streamlit app
├── scripts/
│   ├── handle_missing_data.py  # Handles missing data imputation
│   ├── preprocessing_common.py # Common preprocessing tasks
│   ├── preprocessing_numerical.py # Numerical data preprocessing
│   ├── preprocessing_categorical.py # Categorical data preprocessing
│   ├── preprocessing_text.py   # Text data preprocessing
│   ├── preprocessing_time_series.py # Time-series data preprocessing
│   ├── remove_outliers.py      # Outlier detection and removal
│   ├── normalization.py        # Data normalization
│   ├── feature_engineering.py  # Feature engineering (PCA, Polynomial, etc.)
│   ├── verification.py         # Verification of preprocessing steps
├── requirements.txt            # Project dependencies
└── README.md                   # Project description
```

### Dependencies
This project requires the following Python packages:

Streamlit: To build the interactive web application.
pandas: For data manipulation.
numpy: For numerical computations.
scikit-learn: For preprocessing, feature engineering, and machine learning utilities.
Install the required packages via pip:

```bash
pip install -r requirements.txt
```

### Disclaimer: 
This tool is for learning and building purposes only. It is not meant for production or real-time data applications, and the accuracy of results depends on the data quality and methods used. Use it for experimentation and improvement of your machine learning pipeline knowledge.
