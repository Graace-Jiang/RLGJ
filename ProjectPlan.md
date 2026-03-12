# Project plan

# Overview
The objective of this study is to examine the correlation between the profitability of an industry and the payout ratios of the S&P 500 companies within that industry. We want to see how the average net margin of an industry influences the payout ratios of the top S&P 500 companies. Knowing this information can help us understand how the health of an industry as a whole affects investor returns and corporate policies.
To achieve this goal, we plan on collecting financial data at two different levels. First, we will use Net Margin data to establish industry-level profitability benchmarks (Aswath Damodaran, NYU Stern). Second, we will programmatically scrape current dividend yields and payout ratios for all S&P 500 components using the yfinance API. We will then merge/clean these datasets and map each S&P 500 company to their respective NYU Stern industry. Finally, we will use exploratory data analysis and statistical visualization to find trends between industry-wide health and company dividend performance.

# Team
Grace Jiang

Identify and collect relevant financial data

Clean and preprocess financial data

Integrate datasets at the industry and company levels

Richard Li

Conduct statistical analysis and data exploration

Develop visualizations to illustrate findings

Contribute to interpretation of results

Both members will collaborate on defining the research questions, validating the analysis results, and preparing the final project deliverables.

# Research Questions
The primary goal is to explore the relationship between industry-level Net Margin and dividend payout ratio behavior within the S&P 500.

•	How is the average profitability (Net Margin) of an industry correlated with the dividend payout ratios of the S&P 500 companies within that industry?

•	Is there any obvious difference in dividend payout ratios between high-margin industries (such as Technology) and low-margin industries (such as Retail)?

•	How much does industry-level performance affect the "Dividend Payout Ratio" of top S&P 500 companies?
By answering these questions, we hope to gain insights on how the profitability of an industry as a whole may influence dividend policies and investor income.

# Dataset
In order to answer our research questions, we will be combining two different data sources that provide information on financial performance at industry and company levels.
## Dataset 1: Industry Benchmarks
The first data source is from the NYU Stern School of Business' publicly available datasets created by Aswath Damodaran. We will be using the "Margins by Industry" dataset, which provides financial information at the industry level across various industries. It includes various industry's average net margins and profitability metrics. We will be using this data source as the main benchmark to calculate Industry Net Margin, which is our main accounting variable. This dataset will also help us understand the general financial profitability of various industries.
## Dataset 2: Market Performance
The second dataset will come from Yahoo Finance, scraped programmatically using the yfinance python library. This dataset provides financial market information at the business level, including past dividend payments and payout ratios for publicly listed firms. We will collect dividend information for S&P 500 included in the NYU Stern dataset. We can learn how businesses distribute income to shareholders through dividend payments from this dataset.
## Dataset Integration
These two datasets will be joined using industry or sector classifications as the joining attribute. The NYU Stern dataset provides information on industry, while Yahoo Finance provides sector or industry tags for each company. We can join industry by mapping companies to their respective industries and joining industry-level profitability ratios with company-level dividend payout ratios.
This integration will allow us to check if industries with higher net margins have firms with higher dividend yields, for example.
## Potential Constraints
Industry classifications may not line up between the NYU Stern datasets and Yahoo Finance sector tags. We may need to build a manual mapping table of industry labels to handle this.

# Timeline
Data Acquisition: Download Damodaran’s "Margins by Industry" Excel file and write a Python script using yfinance to pull dividend data for S&P 500 firms.	
Date: March 11 
Responsibility: Grace Jiang

Industry Mapping:	Create a manual mapping table to align NYU Stern industry names with Yahoo Finance sector tags.	
Date: March 20	
Responsibility: Grace Jiang & Richard Li

Data Cleaning:	Handle missing dividend values (NaNs), remove outliers, and convert all financial strings to numeric types in Pandas.	
Date: March 24	
Responsibility: Grace Jiang

Statistical Analysis:	Perform correlation analysis and regression between Net Margin (Industry) and Dividend Yield (Company).	
Date: April 12	
Responsibility: Richard Li

Visualization:	Create scatter plots and heatmaps to illustrate the profitability-yield relationship across sectors.	
Date: April 12	
Responsibility: Richard Li

Report	Validate analysis results, ensure data provenance is documented, and finalize the Project Report.	
Date: April 19
Responsibility: Grace Jiang & Richard Li

Presentation	Prepare presentation slides and final compilation	
Date: May 1	
Responsibility: Grace Jiang & Richard Li

# Constraints
## Naming
Our biggest constraint is **inconsistent industry naming**. The NYU Stern dataset may list a company under *Financial Services*, while Yahoo Finance may categorize it under *Credit Services*.

By limiting our scope to **S&P 500 companies**, we reduce the number of firms requiring manual verification, but we will still need to create a **manual mapping dictionary** to ensure correct joins. This may introduce some bias.

## Time-Lag Issue
Industry profitability data from NYU Stern is typically **updated annually**, while dividend payout ratios from Yahoo Finance **change daily** based on stock prices.

We must clearly define the **reference date** so industry averages and company dividend metrics are comparable. Currently, selecting a date such as **12/31 or 1/1** seems reasonable since it aligns with financial reporting periods.

However, we are unsure whether we will be able to extract the exact historical values for that specific date.

## Survivorship Bias
Our dataset only includes companies **currently in the S&P 500**. It does not include companies that may have been removed from the index or gone bankrupt, which may introduce survivorship bias.


# Gaps

## The "Minimum Count"
We are not yet sure what the **minimum number of companies per industry** should be to ensure meaningful analysis.

If an NYU industry contains only **one S&P 500 company**, that firm may not represent the entire industry well. We may need to **aggregate smaller sub-industries into broader sectors**.

## What Counts as "Profitability"
We are currently using **Net Margin** as our primary profitability metric. However, we are still debating whether **Dividend Yield** might better represent sustainability. We will make a final decision after our initial exploratory data analysis.

## Workflow Automation
We are still determining how to make the workflow **fully reproducible and automated**.

Key considerations include:
- How to store the **manual mapping table** for industry classifications
- Allowing other researchers to **run the same Python scripts and reproduce our results**
- Documenting the **industry matching mechanism**
