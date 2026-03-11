# Project plan

## Overview
The objective of this study is to examine the correlation between the profitability of an industry and the payout ratios of the S&P 500 companies within that industry. We want to see how the average net margin of an industry influences the payout ratios of the top S&P 500 companies. Knowing this information can help us understand how the health of an industry as a whole affects investor returns and corporate policies.
To achieve this goal, we plan on collecting financial data at two different levels. First, we will use Net Margin data to establish industry-level profitability benchmarks (Aswath Damodaran, NYU Stern). Second, we will programmatically scrape current dividend yields and payout ratios for all S&P 500 components using the yfinance API. We will then merge/clean these datasets and map each S&P 500 company to their respective NYU Stern industry. Finally, we will use exploratory data analysis and statistical visualization to find trends between industry-wide health and company dividend performance.

## Team
Grace Jiang

Identify and collect relevant financial data

Clean and preprocess financial data

Integrate datasets at the industry and company levels

Richard Li

Conduct statistical analysis and data exploration

Develop visualizations to illustrate findings

Contribute to interpretation of results

Both members will collaborate on defining the research questions, validating the analysis results, and preparing the final project deliverables.

## Research Questions
The primary goal is to explore the relationship between industry-level Net Margin and dividend payout ratio behavior within the S&P 500.
•	How is the average profitability (Net Margin) of an industry correlated with the dividend payout ratios of the S&P 500 companies within that industry?
•	Is there any obvious difference in dividend payout ratios between high-margin industries (such as Technology) and low-margin industries (such as Retail)?
•	How much does industry-level performance affect the "Dividend Payout Ratio" of top S&P 500 companies?
By answering these questions, we hope to gain insights on how the profitability of an industry as a whole may influence dividend policies and investor income.

## Dataset
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