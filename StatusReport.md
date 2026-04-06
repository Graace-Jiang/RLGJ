# Status Report

## Overview

In this project, we aimed to integrate firm-level financial data with industry-level benchmarks to create a clean and consistent dataset for analysis. We collected company data using yfinance and combined it with Damodaran’s industry margin data. A key challenge in this process was aligning industry classifications across the two datasets.

---

## Data Collection

We collected firm-level data for S&P 500 companies using the yfinance Python library. The dataset includes key variables such as ticker symbol, company name, industry, sector, dividend yield, and payout ratio.

In addition, we downloaded Damodaran’s “Margins by Industry” dataset, which provides industry-level net margin benchmarks. This dataset serves as a reference for comparing firm performance within each industry.

---

## Industry Alignment

One of the main challenges in this project was that the industry labels from Yahoo Finance and Damodaran were not directly compatible. There were two key issues:

1. **Naming inconsistencies**  
   Some industries had different names across the datasets (e.g., “Semiconductors” vs. “Semiconductor”).

2. **Different levels of granularity**  
   Yahoo Finance often uses more detailed industry categories, while Damodaran uses broader groupings.

To address this, we created a manual mapping table (`industry_mapping.csv`) to standardize industry labels. This mapping performed two functions:
- Aligning different naming conventions across datasets
- Grouping highly specific industries into broader categories when necessary

### Example Mapping Table

| Yahoo Industry                  | Mapped Industry (Damodaran)        | Reason |
|--------------------------------|------------------------------------|--------|
| Software - Infrastructure       | Computer Services                  | Naming difference |
| Internet Retail                | Retail (General)                   | Grouped into broader category |
| REIT - Industrial              | R.E.I.T.                           | Grouped into broader category |
| Communication Equipment        | Telecom. Equipment                 | Naming difference |
| Asset Management               | Investments & Asset Management     | Naming difference |

---

## Iterative Refinement

After applying the initial mapping, we merged the datasets and identified unmatched industries. We then iteratively refined the mapping table by reviewing unmatched cases and updating the mappings.

This iterative process significantly reduced the number of unmatched observations. After refinement, only one observation remained unmatched due to missing industry information in the source data.

---

## Data Merging

We merged the firm-level dataset with the Damodaran dataset using the standardized industry labels. This resulted in a combined dataset that includes both firm-specific variables and industry-level net margin benchmarks.

---

## Data Cleaning

After merging, we performed several data cleaning steps:

- Converted financial variables (Dividend Yield, Payout Ratio, Net Margin) to numeric types
- Handled missing values by removing observations with missing critical fields
- Removed outliers by applying reasonable bounds:
  - Payout Ratio between 0 and 5
  - Dividend Yield between 0 and 20

After cleaning, the final dataset contains 493 observations with no missing values.

---

## Final Dataset

The final dataset (`clean_final_dataset.csv`) is fully cleaned and ready for analysis. It includes:

- Firm-level financial data
- Standardized industry classifications
- Industry-level net margin benchmarks

This dataset provides a consistent foundation for further financial and strategic analysis.

---

## Conclusion

The core challenge of this project was aligning industry classifications across two datasets with different naming conventions and levels of detail. We addressed this through manual mapping and iterative refinement, resulting in a clean and integrated dataset suitable for analysis.