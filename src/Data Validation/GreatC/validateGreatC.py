import great_expectations as ge

# Load the data
df = ge.read_csv("customer_data.csv")

# Load the expectation suite
df.load_expectation_suite("expectations/customer_data_expectations.json")

# Validate the data
results = df.validate()

# Print the validation results
print(results)
