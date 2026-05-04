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

We assessed data quality using a Python script (`scripts/quality_report.py`) that computes missing values, duplicates, and summary statistics.

### Completeness and Missingness

The dataset is largely complete, with most variables having very few missing values. However, Dividend Yield has a higher number of missing values (96 observations), reflecting incomplete data availability from the source.

A small number of missing values (typically 1 observation) appear in variables such as DamodaranIndustry and NetMargin, mainly due to unmatched industry classifications during the integration process.

### Duplicates

No duplicate rows were found in the dataset, indicating that each observation represents a unique firm.

### Consistency

Industry classification inconsistencies were observed between Yahoo Finance and Damodaran datasets. These differences required transformation before merging.

### Summary Statistics

Numerical variables fall within reasonable ranges, and no extreme or implausible values were detected prior to cleaning.

### Conclusion

Overall, the dataset is of high quality, with the primary issue being missing values in Dividend Yield and minor mismatches in industry classification, both of which are addressed in the data cleaning stage.

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