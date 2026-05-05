# S&P 500 Dividend Policy and Industry Profitability Analysis

## Contributors
- Grace Jiang
- Richard Li

## Summary

This project investigates whether industry-level profitability, specifically Net Margin, can serve as a predictor of firm-level dividend payout ratios among S&P 500 companies.

To support this analysis, we constructed a reproducible data pipeline that integrates firm-level financial data with industry-level benchmarks. Firm-level data, including dividend yield, payout ratio, industry, and sector, was collected using the yfinance Python library. Industry-level Net Margin benchmarks were obtained from Damodaran’s “Margins by Industry” dataset.

A major challenge in this project was aligning industry classifications across the two datasets. Yahoo Finance uses highly granular industry labels, while Damodaran uses broader categories. To address this issue in a reproducible way, we used OpenRefine to implement rule-based transformations using GREL. These transformations include keyword-based grouping and prefix-based rules, ensuring that similar industries are consistently mapped to standardized categories.

The transformation process is fully reproducible, as all operations are recorded in the OpenRefine history file (history.json). This allows the entire mapping process to be replicated starting from the original dataset without manual intervention.

After standardizing industry labels, we merged the datasets and performed data cleaning operations, including handling missing values, converting variables to numeric types, and removing outliers. The final dataset contains 493 observations with no missing values and is ready for analysis.

Further statistical analysis (described in later sections) evaluates the relationship between industry profitability and firm-level dividend policies.

## Data Profile

We used two datasets:

1. `data/sp500_dividend_data.csv`  
Firm-level data collected using yfinance, including ticker, company, industry, sector, dividend yield, and payout ratio.

2. `data/marginGlobal.xls`  
Damodaran dataset providing industry-level Net Margin benchmarks.

These datasets are integrated using a standardized industry field created through OpenRefine.

## Data Quality

We assessed data quality using `scripts/quality_report.py`. This script performs both file integrity checks and data profiling. It computes SHA-256 hashes for the raw input files, and reports dataset dimensions, missing values, duplicate rows, and summary statistics for the raw Yahoo Finance dataset, the raw Damodaran dataset, the merged dataset, and the final cleaned dataset. This makes the data quality assessment fully reproducible.

### Data Integrity

To ensure reproducibility, we computed SHA-256 hashes for the raw input datasets:

- `data/sp500_dividend_data.csv`: `72c68f354a5b0f4f08bc8a84d9a8974fad65949c603dd1d5f80d7059389fb478`
- `data/marginGlobal.xls`: `89fe631c20f3494bb8afbd6f4407bc2000e3c94e58603da1f2d1f3acd1113e79`

These hashes act as file fingerprints. Any change to the file would result in a different hash, allowing others to verify they are using the exact same data.

### Raw Yahoo Finance Dataset

The raw Yahoo Finance dataset (collected using the `yfinance` library) contains 503 rows and 6 columns. The profiling output is summarized below:

| Column         | Missing Values |
|----------------|---------------|
| Ticker         | 0             |
| Company        | 0             |
| Industry       | 1             |
| Sector         | 1             |
| DividendYield  | 96            |
| PayoutRatio    | 1             |

The most significant issue is the 96 missing values in `DividendYield`. This is not treated as a data error because many firms do not pay dividends or do not report dividend yield. Instead, these values are handled during cleaning by filling them with 0.

The single missing value in `Industry` is more critical because it prevents mapping to Damodaran categories. This row cannot be properly integrated and is therefore removed later in the pipeline.

The script also confirms that there are 0 duplicate rows in this dataset.

### Raw Damodaran Dataset

The raw Damodaran dataset contains 105 rows and 19 columns. The profiling output shows missing values across several columns (typically 7–8 missing values per column). This is expected because the dataset is structured as a reporting table rather than a clean relational dataset.

We do not treat these missing values as a major issue because only a subset of columns (industry and net margin) is used for analysis. Unused columns are not fully cleaned, as doing so would not improve the final dataset.

There are also 0 duplicate rows in this dataset.

### Merged Dataset

After integration, the merged dataset contains 503 rows and 9 columns. The profiling results show:

| Issue                        | Count |
|-----------------------------|------|
| Missing DividendYield       | 96   |
| Missing DamodaranIndustry   | 1    |
| Missing NetMargin           | 1    |

The missing values in `DamodaranIndustry` and `NetMargin` correspond to a single observation that could not be matched due to missing industry information. This issue is not ignored because it affects the ability to assign industry-level benchmarks. The observation is removed during cleaning.

The missing values in `DividendYield` are treated differently. These are interpreted as absence of dividend data rather than integration errors, and are filled with 0 to preserve firms in the dataset.

The dataset also contains 0 duplicate rows.

### Summary Statistics and Plausibility

Key summary statistics from the profiling output:

| Variable        | Min   | Max     |
|----------------|------|---------|
| DividendYield  | 0.02 | 9.44    |
| PayoutRatio    | 0.00 | 12.20   |
| NetMargin      | -0.04| 0.35    |

The maximum `PayoutRatio` value of 12.20 is unusually high and indicates extreme observations that could distort analysis. These values are not ignored but are treated as outliers and filtered during the data cleaning stage.

The ranges for `DividendYield` and `NetMargin` are generally reasonable and consistent with expected financial behavior, so no additional filtering is applied to these variables beyond standard cleaning steps.

### Cleaned Dataset

After cleaning, the final dataset contains 493 rows and 9 columns, with:

- 0 missing values in all columns  
- 0 duplicate rows  

Outliers were removed by restricting `PayoutRatio` to values below 5. As a result, the maximum `PayoutRatio` decreased from 12.20 to 4.71.

### Data Quality Limitations

Not all data quality issues are treated equally. Some issues are intentionally not fully corrected:

- Missing values in `DividendYield` are not removed because they represent firms without dividend information rather than corrupted data.
- Missing values in the Damodaran dataset are not fully cleaned because only a subset of columns is used.
- Differences in industry granularity are not fully resolved, but are handled through mapping to broader categories.

These decisions are made to balance data completeness and analytical validity, ensuring that the dataset remains representative while minimizing bias.

### Conclusion

Overall, the data quality assessment shows that the datasets are usable but require cleaning. The main issues identified were missing values in dividend-related variables, one missing industry classification, inconsistent industry naming, and extreme values in payout ratios. These issues were systematically addressed through reproducible transformations, resulting in a clean and analysis-ready dataset.

## Data Cleaning

We performed data cleaning in two stages: industry alignment and numerical cleaning.

### Industry Alignment (OpenRefine)

We used OpenRefine to transform Yahoo Finance industry labels into Damodaran-compatible categories. Instead of manual mapping, we implemented rule-based transformations using GREL expressions such as keyword matching (e.g., contains(value.toLowercase(), "retail")) and prefix-based grouping (e.g., startsWith(value, "REIT -")).

This approach ensures that the entire mapping process is fully reproducible. All transformation steps are recorded in the OpenRefine operation history file (history.json).

### Numerical Cleaning (Python)

After merging datasets, we:

- Converted financial variables to numeric
- Filled missing values for Dividend Yield and Payout Ratio
- Removed rows with missing DamodaranIndustry or NetMargin
- Removed outliers using reasonable thresholds

The final dataset contains 493 observations with no missing values.

## Findings

## Future Work

## Challenges

The main challenge was aligning industry classifications between Yahoo Finance and Damodaran datasets.

Initial manual mapping approaches were not reproducible, which did not meet project requirements. We addressed this by implementing rule-based transformations in OpenRefine, ensuring that all steps are recorded and reproducible.

Another challenge was ensuring that transformations generalize to new unseen data rather than relying on hard-coded mappings.

## Reproducing

To reproduce this project:

1. Run `scripts/pull_dividend_data.py` to collect Yahoo Finance data
2. Load `data/sp500_dividend_data.csv` into OpenRefine
3. Apply transformations using `data/history.json`
4. Export the result as `data/sp500_yahoo_mapped_to_damodaran.csv`
5. Run `scripts/merge_data.py` to merge datasets
6. Run `scripts/clean_data.py` to generate `clean_final_dataset.csv`

## References

- Yahoo Finance (via yfinance)
- Damodaran, A. (Margins by Industry dataset)
- OpenRefine documentation