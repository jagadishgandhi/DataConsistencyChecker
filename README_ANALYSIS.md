# Sales Data Consistency Analysis

This guide explains how to run data consistency checks on your sales data files.

## Quick Start

### Prerequisites

Make sure UV is installed and dependencies are set up (already done):

```bash
# Dependencies have been installed via UV
# No additional setup needed
```

### Running the Analysis

To analyze a data file, simply run:

```bash
uv run python analyze_sales_data.py
```

The script will:
1. Load the sales data from `data/PWCSalesHistoryWithTrans100525-101125.txt`
2. Run 158 automated data quality tests
3. Generate an HTML report with visualizations
4. Save all outputs to the `analysis_output/` directory
5. **No popup windows** - all graphs are saved to files

## Output Files

After running the analysis, you'll find:

- **`analysis_output/Data_consistency.html`** - Main interactive report with all findings
  - Open this in your web browser
  - Includes embedded visualizations
  - Shows detailed patterns and exceptions

- **`analysis_output/output_*.png`** - Individual visualization images (7 images)
  - Distribution plots
  - Scatter plots
  - Heatmaps
  - Box plots

- **`sales_data_analysis_report.md`** - Summary report in markdown format
  - Executive summary
  - Key findings
  - Recommendations

## Understanding the Results

### HTML Report Structure

The HTML report includes:

1. **Patterns without Exceptions** - Data behaving consistently
2. **Patterns with Exceptions** - Issues identified with specific rows
3. **Visualizations** - Charts showing data distributions and outliers
4. **Examples** - Sample rows demonstrating patterns and exceptions

### Common Issue Types

The tool checks for:

- **Missing values** - Null or empty fields
- **Rare values** - Unusual or unexpected values
- **Outliers** - Values significantly different from the norm
- **Decimal patterns** - Inconsistent price formatting
- **String patterns** - Inconsistent text formatting (e.g., Color codes)
- **Relationship patterns** - Inconsistencies between related columns
- **Negative value patterns** - Unusual patterns in returns/refunds

## Customizing the Analysis

### Analyzing a Different File

Edit `analyze_sales_data.py` and change the `data_file` path:

```python
data_file = r"C:\Workspace\o9-Solutions\DataConsistencyChecker\data\YOUR_FILE.txt"
```

### Adjusting Output Options

You can modify the `display_detailed_results()` call in the script:

```python
dc.display_detailed_results(
    plot_results=True,           # Set to False to disable charts
    include_examples=True,       # Set to False to hide examples
    save_to_disk=True,          # Always True for HTML output
    output_folder=output_dir,   # Change output directory
    show_short_list_only=False  # Show all patterns (not just common ones)
)
```

### Filtering Results

To focus on specific issues, you can add filters:

```python
# Show only specific issue IDs
dc.display_detailed_results(
    issue_id_list=[0, 1, 5],    # Only show issues 0, 1, and 5
    save_to_disk=True,
    output_folder=output_dir
)

# Show only specific columns
dc.display_detailed_results(
    col_name_list=['Color', 'GrossSales'],  # Only Color and GrossSales columns
    save_to_disk=True,
    output_folder=output_dir
)
```

## Current Analysis Results

For the PWC Sales History data (100525-101125):

- **Total Rows Analyzed:** 5,449
- **Data Quality Score:** 98.99% (55 rows flagged)
- **Issues Found:** 11 different patterns with exceptions
- **Tests Passed:** 139 out of 158 tests

### Top Issues to Review

1. **Color Field** - 12 rows with single-character values (Issue ID: 6-9)
2. **Return Processing** - 27 rows with inconsistent negative patterns (Issue ID: 10)
3. **Zero-Quantity Mismatches** - 7 rows (Issue ID: 5)
4. **Price Outliers** - 3 very large values, 3 very small values (Issue ID: 2-4)

## Troubleshooting

### No Popups Appearing (Good!)

The script is configured with:
```python
matplotlib.use('Agg')  # Non-interactive backend
plt.ioff()             # Turn off interactive mode
```

This prevents popup windows and saves everything to files.

### Running on Different Operating Systems

- **Windows:** Use the commands as shown
- **Linux/Mac:** Same commands work with UV

### Memory Issues with Large Files

For very large datasets (>100,000 rows), you may want to:

1. Reduce verbosity:
   ```python
   dc = DataConsistencyChecker(verbose=0)
   ```

2. Disable plots:
   ```python
   dc.display_detailed_results(plot_results=False, ...)
   ```

## Additional Resources

- [Project Documentation](docs/) - API documentation
- [Demo Notebooks](Demo Notebooks/) - Jupyter notebook examples
- [Test Suite](tests/) - Comprehensive test examples
- Main implementation: [check_data_consistency.py](check_data_consistency.py)

## Support

For issues or questions about the DataConsistencyChecker tool, refer to the main project documentation in the `docs/` directory.
