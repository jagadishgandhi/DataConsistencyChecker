"""
Script to analyze PWC Sales History data using DataConsistencyChecker
"""
import pandas as pd
from check_data_consistency import DataConsistencyChecker

# Load the data
data_file = r"C:\Workspace\o9-Solutions\DataConsistencyChecker\data\PWCSalesHistoryWithTrans100525-101125.txt"
print(f"Loading data from: {data_file}")

# Read the CSV file
df = pd.read_csv(data_file)

print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumns: {list(df.columns)}")
print(f"\nFirst few rows:")
print(df.head(10))

print("\n" + "="*80)
print("DATA CONSISTENCY ANALYSIS")
print("="*80)

# Initialize DataConsistencyChecker
dc = DataConsistencyChecker()

# Initialize with the dataframe
dc.init_data(df)

# Run data quality checks
print("\nRunning data quality checks...")
dc.check_data_quality()

# Display detailed results
print("\n" + "="*80)
print("DETAILED RESULTS")
print("="*80)
dc.display_detailed_results()

# Display summary
print("\n" + "="*80)
print("PATTERNS AND EXCEPTIONS SUMMARY")
print("="*80)
dc.summarize_patterns_and_exceptions()
