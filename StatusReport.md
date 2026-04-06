# Milestone 3: Interim Status Report

### Data Collection and Integration

We successfully collected two complementary datasets for this project. The first dataset is the industry-level profitability data from Damodaran, which provides net margin information across industries. The second dataset was constructed using the yfinance Python library to retrieve firm-level financial data for selected S&P 500 companies, including dividend yield, payout ratio, and industry classification.

We developed a Python script (scripts/pull_dividend_data.py) to automate data retrieval from Yahoo Finance. The collected data was saved as sp500_dividend_data.csv. 

To integrate the two datasets, we created a merging script (scripts/merge_data.py) that combines firm-level data with industry-level margin data.

### Changes to the Project Plan

During implementation, we found that the industry labels from Yahoo Finance did not directly match the industry classifications used in the Damodaran dataset. As a result, we adjusted our original plan by introducing a manual mapping step to align the two datasets.

This change improved the data integration process and allowed us to successfully merge the datasets.

### Updated Timeline

Data Acquisition: Download Damodaran’s "Margins by Industry" Excel file and write a Python script using yfinance to pull dividend data for S&P 500 firms.
Date: March 11 - Completed

Responsibility: Grace Jiang

Industry Mapping: Create a manual mapping table to align NYU Stern industry names with Yahoo Finance sector tags.
Date: March 20 - Modified and Completed in another way in terms of matching and joining.

Responsibility: Grace Jiang & Richard Li

Data Cleaning: Handle missing dividend values (NaNs), remove outliers, and convert all financial strings to numeric types in Pandas.
Date: March 24 - Completed

Responsibility: Grace Jiang

Statistical Analysis: Perform correlation analysis and regression between Net Margin (Industry) and Dividend Yield (Company).
Date: will be completed by April 12

Responsibility: Richard Li

Visualization: Create scatter plots and heatmaps to illustrate the profitability-yield relationship across sectors.
Date: will be completed by April 12

Responsibility: Richard Li

Report Validate analysis results, ensure data provenance is documented, and finalize the Project Report.
Date: will be completed by April 19

Responsibility: Grace Jiang & Richard Li

Presentation Prepare presentation slides and final compilation
Date: will be completed by May 1, currently not started

Responsibility: Grace Jiang & Richard Li

### Challenges and Solutions

A major challenge we encountered was the mismatch in industry classifications between the two datasets. The industry names from Yahoo Finance differ from those used in the Damodaran dataset, which initially resulted in missing values after merging.

To address this issue, we created a manual mapping dictionary to align industry names between the datasets. This significantly improved the merge results and reduced missing values.

Another challenge was handling missing values in the dividend data. Some firms do not pay dividends, leading to missing values in dividend yield and payout ratio. We addressed this by replacing missing values with zeros, assuming that non-dividend-paying firms have zero payout.

We also performed basic data cleaning, including converting all financial variables to numeric types and removing outliers to ensure data consistency.

### Artifacts

The following files were created and used in this milestone:

- data/marginGlobal.xls  
- data/sp500_dividend_data.csv  
- data/final_dataset.csv  
- data/clean_final_dataset.csv  
- scripts/pull_dividend_data.py  
- scripts/merge_data.py  
- scripts/clean_data.py  

### Individual Contribution (Grace)

In this milestone, I was responsible for implementing the data pipeline. I developed Python scripts to retrieve firm-level data using yfinance, processed and cleaned the data using Pandas, and performed dataset integration. I also identified and resolved industry classification mismatches by creating a manual mapping approach. Additionally, I handled missing values and performed data cleaning to prepare the dataset for further analysis.
