# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DataConsistencyChecker is a Python tool for automated data quality analysis and outlier detection. It performs approximately 150 interpretable tests on tabular datasets to identify patterns and exceptions, supporting both exploratory data analysis (EDA) and outlier detection workflows.

## Key Architecture

- **Single-file implementation**: The core functionality is contained in `check_data_consistency.py` (~1MB file)
- **DataConsistencyChecker class**: Main entry point with methods for data initialization, quality checking, and result display
- **Test-based architecture**: Each test examines specific patterns (single columns, column pairs, or larger column sets)
- **Scoring system**: Rows are scored based on number of exceptions flagged across tests

## Development Commands

### Running Tests
```bash
# Run all tests 
python3 -m pytest tests/

# Run specific test
python3 -m pytest tests/test_MISSING_VALUES.py

# Run tests with verbose output
python3 -m pytest -v tests/
```

### Basic Usage
```python
from check_data_consistency import DataConsistencyChecker
import pandas as pd

# Initialize and run analysis
dc = DataConsistencyChecker()
dc.init_data(df)  # df is your pandas DataFrame
dc.check_data_quality()

# View results
dc.display_detailed_results()
dc.summarize_patterns_and_exceptions()
```

## Project Structure

- `check_data_consistency.py` - Main implementation (single file)
- `tests/` - Extensive test suite with 150+ test files (one per test type)
- `docs/` - API documentation and additional guides
- `Demo Notebooks/` - Jupyter notebook examples
- `images/` - Example output images for documentation

## Dependencies

Required packages:
- `termcolor` (only external dependency beyond standard data science stack)
- Standard scientific Python: pandas, numpy, scipy, matplotlib, seaborn, sklearn

## Test Framework

- Uses pytest for testing
- Each test type has its own test file (`test_TESTNAME.py`)
- Tests use both synthetic and real datasets via OpenML
- Caching system (`dc_cache/`) speeds up repeated test runs
- Test configuration in `list_real_files.py` and `utils.py`

## Key APIs

- `init_data(df)` - Initialize with DataFrame
- `check_data_quality()` - Run all consistency tests  
- `display_detailed_results()` - Show detailed findings
- `summarize_patterns_and_exceptions()` - High-level summary
- `quick_report()` - Convenience method for overview
- `display_next()` - Iterate through results one test at a time

## Performance Notes

- Tool processes large datasets but can be computationally intensive
- Many tests share computations for efficiency
- Multiprocessing support available for large datasets
- Results can be saved to HTML files for offline viewing