# Status Report

## Overview

In this project, we aimed to integrate firm-level financial data with industry-level benchmarks to create a clean and consistent dataset for analysis on the relationship of industry margin and payout ratios.  By integrating industry-level net margin benchmarks with company-specific dividend data, we explore how an industry's overall profitability influences the payout ratios of its top-performing constituents in the S&P 500. Our primary research question asks whether high-margin industries (e.g., Technology) exhibit systematically different dividend behaviors compared to low-margin industries (e.g., Retail). Through the first half of the project, we collected company data using yfinance and combined it with Damodaran’s industry margin data. We have successfully moved from conceptual planning to a functional data pipeline. We have navigated significant data curation challenges, particularly regarding semantic alignment across disparate financial datasets. A key challenge so far in this process was aligning industry classifications across the two datasets. Also, as we moved into the statistical analysis first phase led by Richard, we encountered significant modeling challenges that have forced us to re-evaluate our analytical approach. This report outlines our progress, the artifacts generated, and a significant methodological pivot necessitated by initial statistical findings. 

---

## Data Collection

We have aligned our project with the data lifecycle models discussed in class, focusing heavily on the collection, extraction, and cleaning phases.

#### Programmatic Acquisition (pull_dividend_data.py)

To satisfy the requirement for at least two different datasets, we developed a Python script that programmatically retrieves data for all S&P 500 components.

Source: 

Yahoo Finance via the yfinance API.

Artifact: 

data/sp500_dividend_data.csv.

Curation Action: The script loops through 500+ tickers, handling API timeouts and missing values to ensure a complete snapshot of current dividend yields and payout ratios.


#### Benchmark Acquisition (marginGlobal.xls)

We acquired industry-level benchmarks from Professor Aswath Damodaran (NYU Stern). This dataset provides the "Net Margin" variable used as our primary independent predictor.

Direct download: marginGlobal.xls

#### Merge and Clean

We merged and cleaned datasets for future usage.

Artifact: 

clean_data.py

list_industries.py

merge_data.py

pull_dividend_data.py

clean_final_dataset.csv

Format: Semi-structured Excel data requiring significant structural cleaning to isolate US-based industry averages.
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

We merged the firm-level dataset with the Damodaran dataset using the standardized industry labels created in the previous step. We performed a left join in Pandas, using the mapped industry column as the primary key. This resulted in a combined dataset that includes both firm-specific variables (like Ticker and Payout Ratio) and industry-level net margin benchmarks.

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

- Firm-level financial data (493 observations with missing values properly processed)
- Standardized industry classifications
- Industry-level net margin benchmarks

This dataset provides a consistent foundation for further financial and strategic analysis.

---



## Challenges and Solutions

As the lead for statistical analysis, Richard implemented the first rounds of regression testing using the cleaned dataset (also with artifact testing scripts). Our goal was to validate the hypothesis that industry profitability correlates with payout ratios. However, the primary challenge encountered during the analysis phase involved the lack of predictive effectiveness in our cross-industry model. While our technical pipeline for merging the datasets is successful, our initial regression analysis across industries yielded very poor results. Despite aggregating the data to the industry level to find broader trends, the R-squared values remained exceptionally low ($R^2 < 0.10$). This indicates that Industry Net Margin alone is an insufficient predictor for the payout ratios of S&P 500 companies. This lack of predictive power suggests that our current variables do not capture the complexity of corporate dividend decisions.

---

## Gaps and Request for Guidance

In accordance with the "Gaps" requirement of our project plan, we are seeking instructor feedback on our analytical direction:

#### Research Question for Instructors/TAs:

Should we complete our current model and document the finding that no significant relationship exists between these specific variables, or should we seek to identify and add additional factors (such as Free Cash Flow or Market Capitalization) to our model to see if we can better learn and predict the relationship? We are prepared to enrich our dataset further if a "no relationship" finding is considered insufficient for the final project submission.


---

## Individual Contributions

#### Grace Jiang

Grace was responsible for the core data curation and acquisition workflow. She implemented the Python scripts for data retrieval (pull_dividend_data.py e.g.) and integration (merge_data.py e.g.). Grace also led the iterative refinement of the industry mapping table and the systematic cleaning of the final dataset to ensure all numeric values were standardized and outliers were managed.

#### Richard Li

Richard's contribution focused on the data analysis, modeling, and documentation phases. He developed the analysis_modification_tried.py and analysis_visualization.py scripts to test our research questions. Richard identified the poor effectiveness of the current model and have been responsible for documenting these challenges in this report and updating our project timeline to reflect our current analytical pivot. Richard also helped in the construction of industry mapping and data downloading.

---

## Conclusion

The core challenge of this project was aligning industry classifications across two datasets with different naming conventions and levels of detail. We addressed this through manual mapping and iterative refinement, resulting in a clean and integrated dataset suitable for analysis.
