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

### Completeness and Missingness

The raw Yahoo Finance dataset contains 503 rows and 6 columns. Most fields are complete, but `DividendYield` has 96 missing values. This reflects incomplete data availability rather than data corruption, since not all firms pay dividends or report dividend yield. There is also one missing value in `Industry`, `Sector`, and `PayoutRatio`.

The raw Damodaran dataset contains 105 rows and 19 columns and includes missing values across multiple columns. This is expected because the Excel file is formatted for reporting industry benchmarks rather than being a clean tabular dataset. Only the relevant columns were used during integration.

The merged dataset contains 503 rows and 9 columns. It has one missing value in `DamodaranIndustry`, `Industry_y`, and `NetMargin`, caused by one firm whose industry classification was missing in the Yahoo dataset and therefore could not be mapped.

The final cleaned dataset contains 493 rows and 9 columns, with no missing values remaining. Observations with missing critical fields were removed during cleaning.

### Duplicates

The profiling script found zero duplicate rows across all datasets (raw Yahoo, raw Damodaran, merged, and cleaned). This confirms that each observation represents a unique firm and that no duplicate records bias the analysis.

### Consistency and Industry Classification

The most significant data quality issue was inconsistency in industry classification between Yahoo Finance and Damodaran. Yahoo Finance uses highly granular and heterogeneous industry labels, while Damodaran uses broader standardized categories.

This mismatch prevents direct merging. For example, Yahoo categories such as “Internet Retail” or “Software - Infrastructure” do not directly correspond to Damodaran categories. This inconsistency required transformation before integration.

### Granularity Differences

The two datasets differ in classification granularity. Yahoo Finance provides detailed industry categories, while Damodaran aggregates industries into broader groups. As a result, multiple Yahoo categories must be mapped to a single Damodaran category.

This introduces ambiguity and is the primary source of integration complexity in the dataset.

### Summary Statistics and Plausibility

The profiling script generated summary statistics for numerical variables. In the merged dataset, `PayoutRatio` reaches a maximum value of 12.2003, which is unusually high and may distort analysis.

During cleaning, we applied thresholds to remove outliers, restricting `PayoutRatio` to values below 5 and bounding `DividendYield` within a reasonable range. After cleaning, the final dataset has a maximum `PayoutRatio` of 4.7143 and no missing values.

### Conclusion

Overall, the data quality assessment shows that the datasets are usable but require cleaning. The main issues are missing values in dividend-related variables, differences in industry classification systems, and the presence of outliers. These issues were systematically addressed through reproducible transformations and filtering steps, resulting in a clean dataset suitable for analysis.

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