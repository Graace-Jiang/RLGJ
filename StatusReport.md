# Status Report

## Overview

In this project, we aimed to integrate firm-level financial data with industry-level benchmarks to create a clean and consistent dataset for analysis. We collected company data using yfinance and combined it with Damodaran’s industry margin data. A key challenge in this process was aligning industry classifications across the two datasets in a reproducible way.

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

To address this, we used OpenRefine to implement rule-based transformations that map Yahoo Finance industry labels to Damodaran industry categories. Instead of manually editing values, we defined reusable rules based on patterns such as keyword matching (e.g., “contains('retail')”) and category grouping (e.g., mapping all “REIT - *” categories to “R.E.I.T.”).

This approach allowed us to:

- Standardize naming differences across datasets  
- Aggregate more detailed industries into broader Damodaran categories  
- Ensure that the entire mapping process is fully reproducible  

The complete transformation process is documented in the exported OpenRefine operation history (`openrefine_operations.json`), which allows every step to be reproduced from the original dataset.

### Example Mapping Logic

| Yahoo Industry                  | Damodaran Industry                | Logic |
|--------------------------------|----------------------------------|-------|
| Software - Infrastructure       | Computer Services                | Keyword-based rule |
| Internet Retail                | Retail (General)                 | Keyword-based grouping |
| REIT - Industrial              | R.E.I.T.                         | Prefix-based rule |
| Communication Equipment        | Telecom. Equipment               | Naming normalization |
| Asset Management               | Investments & Asset Management   | Keyword-based rule |

---

## Reproducibility

A key requirement of this project is reproducibility. To ensure that our data processing pipeline can be fully reproduced:

- All industry mapping was performed in OpenRefine using rule-based transformations  
- The cleaned dataset was exported as `industry_mapped_openrefine.csv`  
- The full sequence of transformations was exported as `openrefine_operations.json`  

Using these files, the entire mapping process can be reproduced starting from the original raw dataset without any manual intervention.

---

## Data Merging

We merged the processed company dataset with Damodaran’s industry dataset using the standardized `DamodaranIndustry` field. This allowed us to attach industry-level net margin benchmarks to each firm.

The merging process successfully matched 502 out of 503 observations. One observation could not be matched because the original dataset did not contain industry information.

---

## Data Cleaning

After merging, we performed several data cleaning steps:

- Converted financial variables (Dividend Yield, Payout Ratio, Net Margin) to numeric types  
- Filled non-critical missing values (e.g., Dividend Yield and Payout Ratio) with zeros  
- Removed observations with missing critical fields (DamodaranIndustry or NetMargin)  
- Removed outliers by applying reasonable bounds:
  - Payout Ratio between 0 and 5  
  - Dividend Yield between 0 and 20  

One observation with missing industry information (from the original dataset) was removed during this step.

After cleaning, the final dataset contains 493 observations with no missing values.

---

## Final Dataset

The final dataset (`clean_final_dataset.csv`) is fully cleaned and ready for analysis. It includes:

- Firm-level financial data  
- Standardized industry classifications (Damodaran)  
- Industry-level net margin benchmarks  

This dataset provides a consistent and reproducible foundation for further financial and strategic analysis.

---

## Conclusion

The core challenge of this project was aligning industry classifications across two datasets with different naming conventions and levels of detail. Instead of relying on manual mapping, we implemented a reproducible, rule-based transformation process using OpenRefine. This approach ensured consistency, scalability, and full reproducibility, resulting in a clean and integrated dataset suitable for analysis.