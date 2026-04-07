# Status Report

## Overview
For this project we sought to merge firm level financial data with industry level benchmarks to produce a single "clean" data set to explore the relationship of industry margin and payout ratios. By combining industry level benchmarks for net margin with company specific dividend data we seek to determine if an industry that is, on average, more profitable (e.g. Technology) will have systematically different dividend behaviors than an industry that is less profitable (e.g. Retail). Our primary research question is does industry margin systematically explain differences in dividend behavior for the top performers within an industry among the S&P 500.

Thus far we have moved from conceptual planning to a functioning data set. We have encountered large data curation challenges, especially in terms of semantic compatibility across financial data sets. One of the biggest challenges we have faced early in this process was aligning the industry classification between the two data sets. As we moved into the statistical analysis first phase (led by Richard) we have faced large modeling challenges that have forced us to reevaluate our analytical approach. This report details our progress, the artifacts we have produced, and our major methodological change based on initial statistical results.


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

Then we iteratively refined the mapping table by looking at the unmatched cases and updating mappings.
This iterative process reduced the number of unmatched observations. After refinement, there was only one unmatched observation due to lack of industry information in the source data.

---

## Data Merging

We then merged the firm-level data set with the Damodaran data set on the standardized industry labels that were created in the previous step. This was done by performing a left join in Pandas on the mapped industry column.
Our combined data set includes both firm-level variables (in this case, Ticker and Payout Ratio) as well as industry-level net margin benchmarks.

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

As the statistical analysis lead, I implemented the first rounds of regression testing on the cleaned data set (also with artifact testing scripts) (found here). Our goal was to validate the hypothesis that industries that are more profitable on net margin are likely to have lower payout ratios.

Our main challenge we faced during the analysis phase was the lack of predictive effectiveness in a cross-industry model. While our technical pipeline for merging the data sets is a success (we were able to join the data sets), our initial regression analysis across industries was very poor. Despite aggregating the data at the industry level in order to find trends, the R-squared values remained exceptionally low ($R^2 < 0.10$). This means that Industry Net Margin on its own is not predictive of the payout ratios of S&P 500 companies. This lack of predictive power indicates that our current set of variables are not capable of representing the complexity of what drives a company to dividend.

---

## Gaps and Request for Guidance

In accordance with the “Gaps” portion of our project plan, I am seeking feedback from our instructor/TAs of the direction we are taking analytically.

#### Question for Instructors/TAs:

Should we complete our current model and document the finding that no significant relationship exists between these specific variables, or should we seek to identify and add additional factors (such as Free Cash Flow or Market Capitalization) to our model to see if we can better learn and predict the relationship? We are okay with enriching our data set more if a "no relationship" finding would be considered insufficient for the final project submission.

---

## Individual Contributions

#### Grace Jiang

Grace did the main data curation/ acquisition workflow, wrote the python scripts for downloading data (pull_dividend_data.py e.g.), and integrated all the data together (merge_data.py e.g.). Grace also did the industry mapping table iteration and the final dataset cleaning process, making all the numeric values consistent and removing outliers.

#### Richard Li

Richard did the pilot data analysis, modeling, and documentation so far. Wrote the analysis_modification_tried.py and analysis_visualization.py to quickly test our research questions. Richard noticed the ineffectiveness of our model. He has been documenting these for us in this report and also helped update our project timeline to reflect our recent analytical pivot. (pull_dividend_data.py, merge_data.py). Richard also did industry mapping and data downloading construction.

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
Pilot Modeling Completed. Plan to complete modified version based on feedback for this report by  April 20

Responsibility: Richard Li

#### Visualization:	Create scatter plots and heatmaps to illustrate the profitability-yield relationship across sectors.	
Started. Plan to complete with the modified version of statistical analysis by  April 20

Responsibility: Richard Li

#### Report	Validate analysis results, ensure data provenance is documented, and finalize the Project Report.	
Not started. Planned Date: April 25

Responsibility: Grace Jiang & Richard Li

#### Presentation	Prepare presentation slides and final compilation	
Not started. Planned Date: May 1	

Responsibility: Grace Jiang & Richard Li

---

## Conclusion

From the beginning, the main issue of this project was taking two different industry datasets and mapping them together because their names and levels of detail were different. We overcame this through manual mapping and iteration to get a nice clean data set ready for analysis. However, we now encountered new issues regarding statistical analysis, and are looking forward to the feedback on direction as well as techinical programming advice.
