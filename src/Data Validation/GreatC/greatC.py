# pip install great_expectations
import os
import pandas as pd
import great_expectations as ge
from great_expectations.dataset.pandas_dataset import PandasDataset

# Load the data
# df = ge.read_csv("customer_data.csv")
df = pd.read_csv("tmp/combined_data.csv")
df = PandasDataset(df)
# Create a new expectation suite
df.expect_column_to_exist("combined_id")
df.expect_column_values_to_not_be_null("id")
df.expect_column_values_to_be_decreasing("id")
df.expect_column_values_to_be_unique("id")

df.expect_column_to_exist("email")
df.expect_column_values_to_match_regex("email", r"[^@]+@[^@]+\.[^@]+")

df.expect_column_to_exist("age")
df.expect_column_values_to_be_between("age", 18, 99)

df.expect_table_row_count_to_equal(10)


# Ensure the directory exists
expectations_dir = "expectations"
if not os.path.exists(expectations_dir):
    os.makedirs(expectations_dir)

# Save the expectation suite
expectation_suite_path = os.path.join(expectations_dir, "customer_data_expectations.json")
try:
    df.save_expectation_suite(expectation_suite_path)
except Exception as e:
    print(f"Error saving expectation suite to {expectation_suite_path}: {e}")

print(df.validate())
