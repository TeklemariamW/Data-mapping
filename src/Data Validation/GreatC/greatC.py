# pip install great_expectations
import great_expectations as ge

# Load the data
df = ge.read_csv("customer_data.csv")

# Create a new expectation suite
df.expect_column_to_exist("customer_id")
df.expect_column_values_to_not_be_null("customer_id")
df.expect_column_values_to_be_unique("customer_id")

df.expect_column_to_exist("email")
df.expect_column_values_to_match_regex("email", r"[^@]+@[^@]+\.[^@]+")

df.expect_column_to_exist("age")
df.expect_column_values_to_be_between("age", 18, 99)

# Save the expectation suite
df.save_expectation_suite("expectations/customer_data_expectations.json")
