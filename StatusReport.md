# Status Report

## Overview

The goal of this project was to take firm-level financial data and merge it with industry-level benchmarks in order to produce a single “clean” dataset for analysis. We scraped company data using yfinance and merged it with Damodaran’s industry margin data. The industry classification step was particularly challenging for us at the beginning because we could not straightforwardly compare industry classifications from the two datasets in a reproducible way.

Our ultimate goal is to see if industry profitability (specifically Net Margin) is a good predictor for the Dividend Payout Ratio of S&P 500 components. Since our initial project plan, we have successfully built a working data pipeline. Our methodology has undergone extensive revision, however, to meet data curation standards.

---

## Data Collection

We scraped firm-level data for S&P 500 companies using the yfinance Python library. Our variables include ticker symbol, company name, industry, sector, dividend yield, and payout ratio.

In addition, we scraped Damodaran’s “Margins by Industry” dataset, which we use as industry-level benchmarks to compare against firms in each industry.

We have done these as we described in the project plan.

---

## Industry Alignment & Challenges

One of the challenges we faced in this project was that the industry labels from Yahoo Finance and Damodaran were not directly compatible. There were two primary issues:

1. **Naming inconsistencies**  
   Some industries had different names across datasets (e.g., “Semiconductors” vs. “Semiconductor”).

2. **Different levels of granularity**  
   Some industries in Yahoo Finance were more detailed than those used by Damodaran (e.g., “Semiconductors and Semiconductor Equipment” vs. “Semiconductors”).

We were able to resolve this issue by implementing rule-based transformations in OpenRefine using Google Refine Expression Language (GREL). Rather than editing each instance manually, we were able to define reusable patterns such as keyword matching (e.g., contains(value.toLowercase(), "asset management")) and category grouping (e.g., using startsWith(value, "REIT - ") to map all industrial or residential REITs to the unified "R.E.I.T." category). 

This approach allowed us to:

- Standardize naming differences across datasets  
- Aggregate more detailed industries into broader Damodaran categories  
- Ensure that the entire mapping process is fully reproducible  

The complete transformation process is tracked and documented in the exported OpenRefine operation history (`openrefine_operations.json`), so that any transformation step can be reproduced from the original raw data.

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
- The cleaned dataset was exported as `sp500_yahoo_mapped_to_damodaran.csv`  
- The full sequence of transformations was exported as `openrefine_operations.json`  

Using these files, the entire mapping process can be reproduced starting from the original raw dataset without any manual intervention.

---

## Data Merging

Due to the nature of our data collection and processing, we were able to merge our firm-level and industry-level data now using the standardized `DamodaranIndustry` field. Our ultimate goal will be to merge our S&P 500 firms with other external data sources in order to perform analysis.

We then joined the cleaned company dataset with Damodaran's industry dataset on standardized DamodaranIndustry field and then each firm got industry level net margin benchmark.

Actually, we finally joined 502 out of 503 observations. We could not join the remaining one because original data set did not have industry information.




---

## Data Cleaning

We did data cleaning after joining the data set:

- Converted financial variables (Dividend Yield, Payout Ratio, Net Margin) to numeric. 
- Filled non-critical missing values (Dividend Yield, Payout Ratio) with zeros.
- Removed observations with missing critical fields (DamodaranIndustry, NetMargin). 
- Removed outliers by applying reasonable bounds:
  - Payout Ratio between 0 and 5  
  - Dividend Yield between 0 and 20  

One observation with missing industry information (from the original dataset) was removed during this step.

The final data set (clean_final_dataset.csv) has 493 observations and no missing values.

---

## Final Dataset

The final dataset (`clean_final_dataset.csv`) is fully cleaned and ready for analysis. It includes:

- Firm-level financial data  
- Standardized industry classifications (Damodaran)  
- Industry-level net margin benchmarks  

This dataset provides a consistent and reproducible foundation for further financial and strategic analysis.

---

## Changes to the Project Plan

We have had significant methodological pivot regarding how we handle Industry Alignment and Mapping in our project. In our initial project plan, we planned to use manual mapping to align the difference in semantics between Yahoo Finance and Damodaran benchmark data set. However, based on feedback on requiring strong enough reproducibility (previous one is hard to reproduce), and requirement of using knowledge we learned in class, as well as guidance we gathered from Campuswire, we realized that our manual “human mapping” worked as a black box and made it hard for external researchers to audit and repeat it.

As a result, we decided to use OpenRefine as a tool to do data transformation/enrichment. This way, our curation actions are recorded in machine-readable operation history instead of static code. In addition to this, we have renamed our primary data artifacts (IndustryMapped column to DamodaranIndustry for example) to make our data more clear and FAIR.

---

## Gaps & Request for Guidance

A gap has appeared during our statistical analysis, which we are still working on right now. While our data curation pipeline is reproducible, our initial modeling effectiveness is low.

Richard ran a linear regression across industries on margins versus payouts. Even with very clean data, R-squareds are ~0.20. So Industry Net Margin is not a very good standalone predictor of S&P 500 dividend policy. We have decoupled these variables, so it seems that there are company-specific factors (perhaps stage of growth, perhaps debt levels) that override industry-wide measures of profitability as predictors.

And thus, we would like to ask for advice regarding our modeling. For example, are we good with just using linear regression? Or should we add more variables?

---

## Individual Contributions

##### Grace Jiang
Grace helped transfer the industry mapping to the OpenRefine workflow, writing the GREL logic for the mapping of industry classifications. Then, she provides the history.json provenance record. She also wrote the primary integration scripts (merge_data.py) and the final cleaning script (clean_data.py), ensuring that all artifacts are correctly formatted and column-named for maximum understandability.

##### Richard Li
Richard's role focused on the analysis and documentation requirements. In addition, he assisted the openrefine processing in terms of the naming and matching. He then developed the regression model scripts and identified the poor predictive effectiveness of our initial variable set. He also created a pilot visualization script for the regression analysis. 
Richard has also been responsible for documenting our methodological pivot in this report and maintaining the project's adherence to Markdown standards. He also updated the timeline to reflect the current roadblock in our research.

---

## Updated Timeline

#### Data Acquisition: Download Damodaran’s "Margins by Industry" Excel file and write a Python script using yfinance to pull dividend data for S&P 500 firms.	

Completed

Responsibility: Grace Jiang

#### Industry Mapping:	Create a manual mapping table to align NYU Stern industry names with Yahoo Finance sector tags.	

Completed

Responsibility: Grace Jiang & Richard Li

#### Data Cleaning:	Handle missing dividend values (NaNs), remove outliers, and convert all financial strings to numeric types in Pandas.	

Completed

Responsibility: Grace Jiang

#### Statistical Analysis:	Perform correlation analysis and regression between Net Margin (Industry) and Dividend Yield (Company).	

Date: April 18	

Responsibility: Richard Li

#### Visualization:	Create scatter plots and heatmaps to illustrate the profitability-yield relationship across sectors.	

Date: April 18

Responsibility: Richard Li

#### Report	Validate analysis results, ensure data provenance is documented, and finalize the Project Report.	

Date: April 24

Responsibility: Grace Jiang & Richard Li

#### Presentation	Prepare presentation slides and final compilation	

Date: May 1	

Responsibility: Grace Jiang & Richard Li

---

## Ket Artifacts

The following key artifacts have been created and committed to the repository:

##### Data Artifacts

history.json: A machine-readable JSON “recipe” of the full operation history for industry mapping and transformation.

sp500_yahoo_mapped_to_damodaran: The firm-level data set with standardized industry labels generated as the output of the OpenRefine mapping process.

final_dataset: The integrated output file generated by the relational join between the firm-level market data and industry benchmarks.

clean_final_dataset.csv: The final clean data set after numeric standardization, imputation based on dividend policy, and filtering of outliers.

##### Script & Documentation Artifacts

pull_dividend_data.py: The Python script used to programmatically retrieve dividend data from the Yahoo Finance API using the yfinance library.

merge_data.py: The integration script that joins the firm-level and industry-level data sets based on standardized labels.

clean_data.py: The script that implements our data quality and cleaning operations on the data so that it meets analytical requirements.

analysis_visualization_test.py: A script generating the statistical visualizations for our findings.

analysis_modification_tried.py: A script modeling and analyzing the data using linear regression.

---

## Conclusion

The main challenge of our work was taking two data sets with different naming conventions and different levels of detail coverage and bringing them together into a single data set. Instead of manually mapping them together, we implemented a reproducible rule-based transformation using OpenRefine and ensured consistency and scalability of the transformation across the data sets, rendering the entire workflow fully reproducible. Currently, we are still looking for some advice regarding modeling, but we think we are close to the end.
