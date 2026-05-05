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

We assessed data quality using a Python profiling script (`scripts/quality_report.py`) that computes missing values, duplicate rows, and summary statistics for the integrated dataset. This script provides a reproducible data quality assessment step in our workflow, as the same checks can be rerun to verify the condition of the dataset.

### Data Integrity (SHA-256)

To support data integrity and reproducibility, we computed a SHA-256 hash for the raw Damodaran dataset. SHA-256 acts as a unique fingerprint for the file: any modification to the file would result in a different hash value. This ensures that anyone reproducing our project can verify they are using the exact same dataset.

- `marginGlobal.xls`: `89fe631c20f3494bb8afbd6f4407bc2000e3c94e58603da1f2d1f3acd1113e79`

This step is particularly important because the Damodaran dataset is externally sourced and serves as a benchmark in our analysis.

### Completeness and Missingness

The profiling results indicate that the dataset is largely complete, with most variables containing very few missing values. However, `DividendYield` has 96 missing values, which likely reflects incomplete reporting for firms that do not pay dividends or for which data is unavailable in Yahoo Finance.

A small number of other fields contain only a single missing value, including industry-related variables and `NetMargin`. This issue arises from one firm whose original industry classification was missing, preventing it from being mapped to a Damodaran industry. Because industry classification and net margin are essential for our analysis, this observation was removed during data cleaning.

### Duplicates

The profiling script confirmed that there are zero duplicate rows in the dataset. This ensures that each observation represents a unique firm and prevents bias in summary statistics or downstream analysis.

### Consistency and Naming

A major data quality issue was inconsistency in industry naming across the two datasets. Yahoo Finance uses more granular and heterogeneous industry labels, while Damodaran uses broader and standardized categories. For example, Yahoo categories such as `Internet Retail` or `Software - Infrastructure` do not directly match Damodaran’s categories.

This inconsistency prevents direct merging and requires transformation to align the two classification systems.

### Granularity Differences

The two datasets also differ in classification granularity. Yahoo Finance provides detailed industry categories, while Damodaran aggregates industries into broader groups. As a result, multiple Yahoo categories must be mapped into a single Damodaran category. This introduces ambiguity during integration and requires careful grouping logic to preserve meaningful relationships.

### Summary Statistics

The numerical ranges of variables were reviewed using summary statistics generated by `scripts/quality_report.py`. The results indicate that values fall within reasonable ranges for financial data, and no implausible values were detected prior to cleaning.

### Conclusion

Overall, the dataset is of high quality and suitable for analysis after cleaning. The primary data quality issues include missing dividend values, a small number of missing industry classifications, and inconsistencies in industry naming and granularity between datasets. These issues are systematically addressed in the data cleaning stage using reproducible transformations.

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