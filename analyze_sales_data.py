"""
Script to analyze PWC Sales History data using DataConsistencyChecker
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from check_data_consistency import DataConsistencyChecker
import os

# Disable matplotlib popups - use non-interactive backend
matplotlib.use('Agg')
plt.ioff()  # Turn off interactive mode

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

# Create output directory for HTML and images
output_dir = os.path.join(os.getcwd(), "analysis_output")
os.makedirs(output_dir, exist_ok=True)

# Display detailed results and save to HTML with plots
print("\n" + "="*80)
print("GENERATING DETAILED RESULTS WITH VISUALIZATIONS")
print("="*80)
print(f"\nSaving results to: {output_dir}")

# Generate HTML report with plots
dc.display_detailed_results(
    plot_results=True,           # Include plots
    include_examples=True,       # Include examples
    save_to_disk=True,          # Save to HTML file
    output_folder=output_dir    # Output directory
)

print(f"\n[SUCCESS] HTML report saved to: {os.path.join(output_dir, 'Data_consistency.html')}")
print(f"[SUCCESS] Images saved to: {output_dir}")

# Also display summary to console
print("\n" + "="*80)
print("PATTERNS AND EXCEPTIONS SUMMARY")
print("="*80)
dc.summarize_patterns_and_exceptions()

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
print(f"\nTo view the full report with visualizations:")
print(f"  Open: {os.path.join(output_dir, 'Data_consistency.html')}")
print(f"\nAll generated images are in: {output_dir}")
