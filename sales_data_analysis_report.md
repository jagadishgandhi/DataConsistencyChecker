# Data Consistency Analysis Report
## PWC Sales History Data (100525-101125)

**Analysis Date:** Generated using DataConsistencyChecker
**Dataset:** `PWCSalesHistoryWithTrans100525-101125.txt`
**Full Interactive Report:** [Data_consistency.html](analysis_output/Data_consistency.html) (includes visualizations)

---

## Quick Links

- [Full HTML Report with Visualizations](analysis_output/Data_consistency.html) - Open in browser for interactive analysis with charts and graphs
- [Generated Images](analysis_output/) - 7 visualization images showing data patterns and exceptions

---

## Dataset Overview

- **Total Rows:** 5,449
- **Total Columns:** 10
- **Columns:** TransactionNo, store_no, transaction_date, upc_no, SoldUnits, NetSales, GrossSales, Style, Color, Size
- **Tests Executed:** 158 automated consistency tests

---

## Executive Summary

The DataConsistencyChecker executed 158 automated tests and identified:

- **30 patterns without exceptions** - Data behaves consistently as expected
- **11 patterns with exceptions** - Identified 55 rows with data quality issues
- **10 columns flagged** - Various consistency issues across different fields

---

## Key Findings

### 1. Data Completeness ✓
- **No missing values** found in any column
- All rows have complete data across all 10 fields

### 2. Numeric Consistency Issues

#### a. Decimal Patterns (GrossSales)
- **Issue ID 0 - RARE_DECIMALS**
- 13 rows (0.24%) have unusual decimal endings
- Most values end in .99, .97, .98, or .00
- **Exceptions found:** Values with decimals like .94, .01, etc.
- **Examples:** -93.75, -66.50, -40.28, 19.94

#### b. Unusual Sales Values
- **Issue ID 2 - VERY_LARGE (NetSales)**
  - 1 row with exceptionally large value: $224.97
  - 75th percentile: $62.99, threshold: $213.49

- **Issue ID 3 - VERY_LARGE (GrossSales)**
  - 2 rows with very large values: $259.96, $269.97
  - 75th percentile: $84.99, threshold: $242.49

- **Issue ID 4 - GREATER_THAN_ONE (NetSales)**
  - 3 rows (0.06%) with values less than $1.00
  - **Values:** $0.04, $0.25, $0.84

#### c. Sold Units Outlier
- **Issue ID 1 - FEW_NEIGHBORS**
- 1 row with SoldUnits = 3.0 (isolated value)
- Most transactions have 1 or 2 units

### 3. Negative Values Pattern
- **Issue ID 10 - NEGATIVE_VALUES_PER_ROW**
- 27 rows (0.50%) with unexpected negative value patterns
- Typically have 0 or 3 negative values per row
- **Flagged rows** have 1 or 2 negative values (unusual pattern)
- Likely represents **returns/refunds** with incomplete data

### 4. Zero Value Mismatches
- **Issue ID 5 - MATCHED_ZERO**
- 7 rows (0.13%) where SoldUnits = 0 but GrossSales ≠ 0
- **Pattern:** When units are zero, both should typically be zero
- **Flagged examples:**
  - SoldUnits: 0, GrossSales: -$5.00
  - SoldUnits: 0, GrossSales: -$25.00
  - SoldUnits: 0, GrossSales: -$10.01

### 5. String Field Issues (Color Column)

Multiple related issues with the Color field:

- **Issue ID 6 - NUMBER_ALPHA_CHARS:** 12 rows (0.22%)
- **Issue ID 7 - NUMBER_ALPHANUMERIC_CHARS:** 12 rows (0.22%)
- **Issue ID 8 - NUMBER_CHARS:** 12 rows (0.22%)
- **Issue ID 9 - FEW_CHARS:** 12 rows (0.22%)

**Problem:** Most Color values are 3-4 characters (e.g., "BLK", "WHT", "BKCC")
**Exceptions:** 12 rows have single-character values ("W" or "B")

**Affected Rows:** 568, 1291, 1602, 1706, 1854, 1966, 2756, 3091, 3424, 4124

---

## Patterns Identified (Working Correctly)

### Strong Patterns ✓

1. **TransactionNo is always ascending** - Data is properly sorted
2. **No missing values** in any field
3. **Color is uppercase** - Consistent formatting
4. **Style is uppercase** - Consistent formatting
5. **Color is suffix of Style** - Strong relationship between fields (e.g., Style: "SK7NVY" → Color: "NVY")
6. **First character of Color is uppercase** - Formatting consistency

---

## Recommendations

### High Priority

1. **Investigate Color Field Issues**
   - Review 12 rows with single-character Color values ("W", "B")
   - Determine if these are:
     - Data entry errors
     - Abbreviated codes needing expansion
     - Valid codes that should be standardized

2. **Review Return/Refund Processing**
   - Examine 27 rows with inconsistent negative value patterns
   - Ensure return transactions are properly recorded with all fields updated

3. **Validate Zero-Quantity Transactions**
   - Review 7 rows where SoldUnits = 0 but GrossSales ≠ 0
   - May indicate processing errors or incomplete refunds

### Medium Priority

4. **Review Outlier Transactions**
   - Validate the transaction with SoldUnits = 3 (unusual quantity)
   - Verify large sales values ($224.97, $259.96, $269.97)
   - Confirm small NetSales values ($0.04, $0.25, $0.84)

5. **Standardize Decimal Patterns**
   - Review 13 rows with non-standard decimal endings
   - Ensure pricing consistency across the dataset

---

## Technical Details

### Test Execution Summary
- **Total Tests:** 158
- **Successful:** 139 tests completed without errors
- **With Errors:** 19 tests encountered NumPy 2.0 compatibility issues (deprecated np.NaN)
- **Tests Finding Patterns:** 14 tests (8.86%)
- **Tests Finding Exceptions:** 10 tests (6.33%)

### Affected Columns
1. TransactionNo
2. SoldUnits
3. NetSales
4. GrossSales
5. Color
6. Style

---

## Data Quality Score

- **Overall Quality:** 98.99% (5,394 clean rows out of 5,449)
- **Rows with at least one exception:** 55 (1.01%)
- **Completeness:** 100% (no missing values)
- **Format Consistency:** 99.78% (Color field exceptions)

---

## Next Steps

1. Export list of flagged rows for manual review
2. Implement data validation rules for:
   - Color field length (min 2-3 characters)
   - NetSales minimum threshold
   - Zero-quantity transaction rules
3. Review return/refund processing workflow
4. Update data entry guidelines for Color codes
