import pandas as pd
import numpy as np
import os
import sqlalchemy
import great_expectations as ge
from great_expectations.dataset import PandasDataset

# Install necessary packages
# %pip install pandas openpyxl great_expectations sqlalchemy pymysql

# Create directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Create sample CSV data
csv_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'age': [25, np.nan, 35, 40, 28],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', np.nan]
})
csv_data.to_csv('tmp/sample_data.csv', index=False)

# Create sample Excel data
excel_data = pd.DataFrame({
    'id': [6, 7, 8, 9, 10],
    'name': ['Eve', 'Frank', 'Grace', np.nan, 'Ivy'],
    'age': [30, 45, np.nan, 38, 27],
    'email': ['eve@example.com', 'frank@example.com', 'grace@example.com', np.nan, 'ivy@example.com']
})
excel_data.to_excel('tmp/sample_data.xlsx', index=False)

# Create sample JSON data
json_data = pd.DataFrame({
    'id': [11, 12, 13, 14, 15],
    'name': ['Jack', 'Karen', 'Leo', 'Mona', np.nan],
    'age': [np.nan, 50, 32, 29, 41],
    'email': [np.nan, 'karen@example.com', 'leo@example.com', 'mona@example.com', 'jack@example.com']
})
json_data.to_json('tmp/sample_data.json', orient='records', lines=True)

# Read CSV data
csv_data = pd.read_csv('tmp/sample_data.csv')

# Read Excel data
excel_data = pd.read_excel('tmp/sample_data.xlsx')

# Read JSON data
json_data = pd.read_json('tmp/sample_data.json', lines=True)

# Define a common schema with additional mappings
common_schema = {
    'id': 'int64',
    'name': 'object',
    'age': 'float64',
    'email': 'object',
    'age_group': 'object'  # New column to categorize age
}

# Data Cleaning and Transformation
def clean_and_transform(df):
    df = df.dropna()  # Drop rows with null values
    df['age_group'] = df['age'].apply(lambda x: 'child' if x < 18 else ('adult' if x < 65 else 'senior'))
    return df

csv_data = clean_and_transform(csv_data)
excel_data = clean_and_transform(excel_data)
json_data = clean_and_transform(json_data)

# Data Integration
combined_data = pd.concat([csv_data, excel_data, json_data], ignore_index=True)

# Ensure the combined data conforms to the common schema
for column, dtype in common_schema.items():
    combined_data[column] = combined_data[column].astype(dtype)

# Save the combined dataset
combined_data.to_csv('tmp/combined_data.csv', index=False)

# Create a Great Expectations DataFrame
ge_df = PandasDataset(combined_data)

# Define Expectations
ge_df.expect_column_to_exist('id')
ge_df.expect_column_to_exist('name')
ge_df.expect_column_to_exist('age')
ge_df.expect_column_to_exist('email')
ge_df.expect_column_to_exist('age_group')

ge_df.expect_column_values_to_be_of_type('id', 'int64')
ge_df.expect_column_values_to_be_of_type('name', 'object')
ge_df.expect_column_values_to_be_of_type('age', 'float64')
ge_df.expect_column_values_to_be_of_type('email', 'object')
ge_df.expect_column_values_to_be_of_type('age_group', 'object')

ge_df.expect_column_values_to_be_between('age', min_value=0)

ge_df.expect_column_values_to_not_be_null('id')
ge_df.expect_column_values_to_not_be_null('name')
ge_df.expect_column_values_to_not_be_null('email')
ge_df.expect_column_values_to_not_be_null('age_group')

ge_df.expect_column_values_to_be_unique('id')

# Validate the data
validation_results = ge_df.validate()

# Print validation results
print(validation_results)

# Database connection
#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@host/dbname')

# Data Insertion
# combined_data.to_sql('table_name', con=engine, if_exists='replace', index=False)
