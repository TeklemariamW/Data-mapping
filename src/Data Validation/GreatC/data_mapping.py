import pandas as pd
import numpy as np
import os
import sqlalchemy
import great_expectations as ge
from great_expectations.dataset import PandasDataset

# Install necessary packages
# %pip install pandas openpyxl great_expectations sqlalchemy pymysql

# Create directory if it doesn't exist
os.makedirs('mapping', exist_ok=True)

# Create sample CSV data
csv_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'first_name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'last_name': ['AAA', 'BBB', 'CCC', 'DDD', "EEE"],
    'age': [25, np.nan, 35, 40, 28],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', np.nan]
})
#csv_data.to_csv('mapping/sample_data.csv', index=False)

# Create sample Excel data
excel_data = pd.DataFrame({
    'identifier': [6, 7, 8, 9, 10],
    'full_name': ['Eve', 'Frank', 'Grace', np.nan, 'Ivy'],
    'age_years': [30, 45, np.nan, 38, 27],
    'email': ['eve@example.com', 'frank@example.com', 'grace@example.com', np.nan, 'ivy@example.com']
})
#excel_data.to_excel('mapping/sample_data.xlsx', index=False)

# Create sample JSON data
json_data = pd.DataFrame({
    'user_id': [11, 12, 13, 14, 15],
    'name': ['Jack', 'Karen', 'Leo', 'Mona', np.nan],
    'years': [np.nan, 50, 32, 29, 41],
    'email': [np.nan, 'karen@example.com', 'leo@example.com', 'mona@example.com', 'jack@example.com']
})
#json_data.to_json('mapping/sample_data.json', orient='records', lines=True)

## Data Mapping

# Extract data from CSV
df_csv = pd.read_csv("mapping/sample_data.csv")

# Extract data from JSON
df_json = pd.read_json("mapping/sample_data.json")

# Extract data from Excel
df_excel = pd.read_excel("mapping/sample_data.xlsx")

# Tranform csv data to common schema
df_csv['full_name'] = df_csv['first_name'] + ' ' + df_csv['last_name']
df_csv = df_csv[['id', 'full_name', 'age', 'email']]

# Tranform json data to common schema
df_json = df_json.rename(columns={'user_id': 'id', 'name': 'full_name', 'years': 'age'})
df_json = df_json[['id', 'full_name', 'age', 'email']]

# Tranform Excel data to common schema
df_excel = df_excel.rename(columns={'identifier': 'id', 'age_years': 'age'})
df_excel = df_excel[['id', 'full_name', 'age', 'email']]

# Combine all dat into a single Dataframe
df_combined = pd.concat([df_csv, df_json, df_excel], ignore_index=True)
print(df_combined)

print('######################################')
## Data cleaning Tranformations
df_combined['age'] = df_combined['age'].fillna(df_combined['age'].mean())
df_combined['email'] = df_combined['email'].fillna('unknown@mycompany.com')

df_combined['full_name'] = df_combined['full_name'].fillna('Unknown')

df_combined = df_combined.drop_duplicates()

print(df_combined)

df_combined.to_csv('mapping/df_combined.csv', index=False)