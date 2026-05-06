# S&P 500 Dividend Policy and Industry Profitability Analysis

## Contributors

* **Grace Jiang**
  - Data lifecycle (Module 1)
  - Data cleaning (Module 10)
  - Data integration (Modules 7/8)
  - Data quality (Module 9)
  - Reproducibility and transparency (Module 13)

* **Richard Li**
  - ata collection and acquisition (Module 3)
  - Ethical data handling (Module 2)
  - Storage and organization (Modules 4/5)
  - Metadata and data documentation (Module 15)
  - Workflow automation and provenance (Modules 11/12)

---

## Summary

The goal of this study was to explore the relationship between the overall profitability of an industry and the dividend payout ratios of the S&P 500 constituents in that industry. In classic corporate finance theory, more profitable industries should provide a relatively safe “home base” for firms to return capital to shareholders. However, we wanted to know if the average net margin of an industry (a measure of overall collective financial health) could be a reliable predictor of the dividend policies of highly-touted, individual firms? This knowledge is valuable to investors and analysts who rely on industry benchmarks when evaluating corporate behavior and expected returns.
To support this analysis, we developed a reproducible end-to-end data pipeline connecting firm-specific market data and industry-wide accounting data. We scraped financial information programatically for all S&P 500 components using the `yfinance` Python library, including payout ratios and dividend yields. At the same time, we acquired industry-level profitability benchmarks from the NYU Stern Datasets maintained by Professor Aswath Damodaran. The critical methodological challenge was that the granularity of labels for Yahoo Finance’s industries did not align with Damodaran’s broader categories. We developed rule-based transformations in OpenRefine using GREL (General Refine Expression Language) such that the entire mapping process was machine-readable and reproducible via an exported `history.json` file.
Our statistical analysis found that Industry Net Margin is an extremely poor predictor of firm-level dividend behavior in the current market environment. The OLS R-squared for the regression model using ordinary least squares regression was 0.054, which demonstrates that there is very little relationship between industry-level profitability and the dividend payout ratios of constituent firms. Industry Net Margin explains essentially no variance in corporate distribution behavior (5.4%), meaning that the model leaves 94.6% of the variance unexplained. Additionally, our regression analysis showed a slight negative coefficient for Net Margin, which contradicts the intuitive expectation that more profitable industries would result in higher payouts.
Our results ultimately demonstrate that industry-level net margins cannot be used, at least on their own, to predict the dividend payout policies of S&P 500 companies. If one were to rely on industry health as a proxy for corporate distribution behavior, one would be setting himself/her-self up for highly inaccurate forecasts. This suggests that corporate dividend policies are likely driven by a combination of company-specific factors—such as internal growth opportunities, debt-to-equity ratios, and cash reserve requirements—overriding industry-wide measures of corporate profitability. These project results highlight the need for multi-variable financial modeling and the dangers of using single industry benchmarks to understand corporate governance.

---

## Files/Storage and Organization

### Directory Structure
The project is organized into a clean directory structure to facilitate ease of navigation and reproducibility:

| Folder / File | Contents |
| :--- | :--- |
| `data/` | Contains all raw, intermediate, and final analytical datasets, including the OpenRefine history. |
| `scripts/` | Contains all Python scripts used for data acquisition, integration, cleaning, and statistical modeling. |
| `README.md` | The main project report containing the summary, methodology, findings, and reproduction steps. |
| `reports/` | Contains project planning and status reporting documents generated during project development. |


### Storage Strategy
Our storage strategy is mainly on interoperability and structured data management:
* **Tabular Data**: The primary datasets are stored as CSV files, ensuring they can be easily loaded into Python via `pandas` or audited using standard spreadsheet software.
* **Semi-structured Provenance**: The OpenRefine curation steps are stored in a semi-structured JSON format (`history.json`), which serves as a machine-readable audit trail of all manual-to-automated mapping transformations.

---

## Data Profile

Each data set used within this project is described below in a self-contained profile including source, acquisition, coverage, description, license, format, variables and ethical considerations.

#### **Market Data via yfinance (API-sourced)**

**Source:** Yahoo Finance historical market data, accessed from the `yfinance` Python library

**Acquisition:** Data is retrieved via the `yfinance` library, which scrapes and fetches data from Yahoo Finance's API endpoints. The acquisition process involves using python based requests and automated handling for historical price downloads and fundamental data. 

**Coverage:** Downloaded data coverage is limited to current components of the S&P 500 index as of early 2026. This ensures a sample of large cap influential firms representing a broad cross-section of the U.S. economy. For the purposes of this project, coverage includes payout ratios for selected tickers.

**Description:** This dataset represents the “ground truth” for firm level behaviour and is the source of our dependent variables. It includes rich financial payout data, company ID and granular industry tags.

**License:** The yfinance library is released under the Apache License 2.0 (a permissive open-source license). The data downloaded is subject to the Yahoo Finance Terms of Service, which prohibit its use for free tier accounts other than personal, non-commercial, and educational purposes.

**Format:** Data was extracted and stored in Comma Separated Values ( .csv ) format, to allow for easy manipulation using the pandas library and version control through Git.

**Variables**
* **Ticker**: A unique string identifier for each company (e.g., "AAPL", "MSFT").
* **Company Name**: The full legal name of the firm.
* **Industry**: The highly granular industry classification assigned by Yahoo Finance.
* **Sector**: The broader economic sector grouping.
* **Payout Ratio**: A floating-point decimal representing the percentage of earnings paid as dividends (e.g., **0.50** for 50%).
* **Dividend Yield**: A floating-point value calculated as the annual dividend payment divided by the stock price.



**Ethical Considerations:** This dataset consists entirely of public corporate financial records derived from SEC filings and stock market activity. No private or sensitive individual information is involved. Our programmatic access was performed ethically, respecting the API's intended use for research and ensuring all findings are shared within the academic scope of the course.

***

#### **NYU Stern Margins by Industry (Aggregated Dataset)**

**Source:** Compiled by Professor Aswath Damodaran at the NYU Stern School of Business, utilizing raw data from Bloomberg, Morningstar, and SEC filings.

**Acquisition:** Downloaded as a curated spreadsheet from the NYU Stern Damodaran "Data: Current" repository. The raw file is stored locally at `data/marginGlobal.xls`.

**Coverage:** Approximately 95 distinct industry sectors, offering a comprehensive snapshot of profitability benchmarks. For this project, we specifically focused on the industry-level profitability data relevant to the firms included in the S&P 500 index.

**Description:** Objective industry profitability benchmarks. Used to get a macro view of operating and net margin health across the economy by comparing company profitability to industry-wide measures.

**License:** Publicly available for educational and research purposes. Proper attribution to Aswath Damodaran and NYU Stern is suggested for any project or publication utilizing the data. To quote: "I hope you find this data useful and there are no strings attached... If you do use my data and wish to acknowledge that you did get the data off my site, I thank you." We think it's functionally equivalent to Public Domain (CC0 1.0).

**Format:** Originally provided in Excel (.xls) format, subsequently converted to CSV for data cleaning and integration.

**Variables:**
* **Industry Name**: The specific sector classification (e.g., Aerospace, Banking).
* **Number of firms**: The count of companies included in the industry sample.
* **Gross Margin**: Total revenue minus cost of goods sold, divided by revenue.
* **Operating Margin (Pre-tax)**: Operating income divided by sales.
* **Net Margin**: Net income divided by sales.
* **EBITDA/Sales**: Earnings before interest, taxes, depreciation, and amortization relative to revenue.

**Ethical Considerations:** The data is extremely aggregated at the industry level, so there are no concerns about corporate confidentiality or individual privacy. The utility of the compilation is a potential source of increased reliability, as it is aggregating over multiple firms and is less likely to be an outlier or reporting error.

---

## Data Quality

We performed data quality checks using `scripts/quality_report.py`. This script performs both file integrity checks and data profiling. It computes SHA-256 hashes of the raw input files and reports dataset dimensions, missing values, duplicate rows, and summary statistics for the raw Yahoo Finance dataset, the raw Damodaran dataset, the merged dataset, and the final cleaned dataset.

### Data Integrity

To ensure reproducibility, we computed SHA-256 hashes for the raw input datasets:

- `data/sp500_dividend_data.csv`: `72c68f354a5b0f4f08bc8a84d9a8974fad65949c603dd1d5f80d7059389fb478`
- `data/marginGlobal.xls`: `89fe631c20f3494bb8afbd6f4407bc2000e3c94e58603da1f2d1f3acd1113e79`

These are file fingerprints. If something has been changed in the file, its hash would be different. This allows others to verify that they obtained the same data as you and that they can reproduce the results.

### Raw Yahoo Finance Dataset

The raw Yahoo Finance dataset (collected using the `yfinance` library) contains 503 rows and 6 columns. The profiling output is summarized below:

| Column         | Missing Values |
|----------------|---------------|
| Ticker         | 0             |
| Company        | 0             |
| Industry       | 1             |
| Sector         | 1             |
| DividendYield  | 96            |
| PayoutRatio    | 1             |

The most interesting issue is the 96 missing values of DividendYield. We do not treat this as a data error: for many firms dividend does not exist or dividend yield is not reported. We treat it as a data issue during the cleaning phase and we fill it with 0.

The missing value in Industry is a problem, because it prevents us to map it to the Damodaran categories. We cannot merge this single row properly, so we drop it later.

Script output also confirms that there are 0 duplicate rows in this data set.

### Raw Damodaran Dataset

We have missing values in several columns (typically speaking, 7–8 missing values per column) and this is to be expected, because the data set is a reporting table, not a clean relational data set.

We do not treat this as an issue: we do not use all the columns for the analysis, so we do not clean the unused columns. Cleaning those columns would not help to create the final data set.

There are also 0 duplicate rows in this dataset.

### Merged Dataset

After integration, the merged dataset contains 503 rows and 9 columns. The profiling results show:

| Issue                        | Count |
|-----------------------------|------|
| Missing DividendYield       | 96   |
| Missing DamodaranIndustry   | 1    |
| Missing NetMargin           | 1    |

The missing values in `DamodaranIndustry` and `NetMargin` correspond to a single observation that could not be matched due to missing industry information. This issue is not ignored because it affects the ability to assign industry-level benchmarks. The observation is removed during cleaning.

Missing values in `DividendYield` are treated separately. These are taken to reflect the absence of dividend information and are filled with 0 to preserve firms in the data set.

The dataset also contains 0 duplicate rows.

### Summary Statistics and Plausibility

Key summary statistics from the profiling output:

| Variable        | Min   | Max     |
|----------------|------|---------|
| DividendYield  | 0.02 | 9.44    |
| PayoutRatio    | 0.00 | 12.20   |
| NetMargin      | -0.04| 0.35    |

Maximum `Payout Ratio` value of 12.20 is too high and suggests that there are extreme values that could influence analysis in ways we may not want. The values are not ignored but removed during the cleaning stage.

The ranges for `DividendYield` and `NetMargin` are acceptable and reasonable given the behaviour we would expect these variables to take. As such there are no additional filtering steps taken on these two variables apart from standard cleaning of the data set.

### Cleaned Dataset

After cleaning, the final dataset contains 493 rows and 9 columns, with:

- 0 missing values in all columns  
- 0 duplicate rows  

Outliers were removed by restricting `PayoutRatio` to values below 5. As a result, the maximum `PayoutRatio` decreased from 12.20 to 4.71.

### Data Quality Limitations

Not all data quality issues are created equally, and some issues will be intentionally left uncorrected:

- Missing values in `DividendYield` are not removed because they represent firms without dividend information rather than corrupted data.
- Missing values in the Damodaran dataset are not fully cleaned because only a subset of columns is used.
- Differences in industry granularity are not fully resolved, but are handled through mapping to broader categories.

These decisions are made to balance data completeness and analytical validity, ensuring that the dataset remains representative while minimizing bias.

### Conclusion

Overall, the data quality assessment indicates that the data sets can be used but need to be cleaned. The main data quality issues that were identified were missing values in dividend related variables, one industry missing classification, inconsistent industry naming, and extreme values in payout ratios. These were systematically addressed through reproducible transformations and resulted in a clean dataset ready for analysis.

---

## Data Cleaning

The data cleaning/curation step of this project was by far the most resource-intensive step in our data pipeline. Its goal was to take semantically heterogeneous financial data and transform it into a high-integrity data set suitable for statistical modeling. We took a modular approach to cleaning designed to be reproducible, rather than a manual “human mapping.” This section outlines the three main phases of our curation process: rule-based industry curation, relational data integration, and numerical standardization.

### Phase 1: Industry Alignment and Standardization (OpenRefine)

The biggest challenge in our data lifecycle was the semantic incompatibility between the granular industry labels used by Yahoo Finance and the benchmark industries offered by the Damodaran dataset. We chose not to perform labor-intensive manual “human mapping,” and instead used OpenRefine to implement rule-based transformations using the Google/General Refine Expression Language (GREL).

**Rationale for the Methodological Pivot**
A manual mapping table was an initial thought, but we soon recognized that such a function would serve as a “black box” that would be impossible for outside researchers to audit or reproduce.

Using OpenRefine, all curation steps were logged in the `history.json` file. This allowed us to track our mapping logic in an transparent and scalable way.

**Some GREL Transformations**
We applied several levels of logic to standardize labels for the Damodaran benchmarks:
* **Keyword-Based Grouping**: Many industries provided by Yahoo Finance were too granular for the Damodaran benchmarks.  We used GREL expressions like `contains(value.toLowercase(), "retail")` to map labels such as "Internet Retail," "Specialty Retail," and "Grocery Retail" into a unified "Retail (General)" category.
* **Prefix-Based Aggregation**: For some specialized sectors like Real Estate Investment Trusts, we used `startsWith(value, "REIT - ")` to ensure that all sub-categories (Industrial, Residential, Office, etc.) would be mapped to the appropriate benchmark “R.E.I.T.” label.
* **Naming Normalization**: We used rules to address simple naming discrepancies (“Semiconductors” vs. “Semiconductor”) that caused non-exact matches when joining the two dataframes down the road. These labels were later normalized to the Damodaran labels using string manipulation rules.
* **Column Creation**: The output of these transformations was stored in a new field titled `DamodaranIndustry`. We kept the original Yahoo labels for provenance purposes, but this new field provided a clean join key.

The full sequence of transformations are saved in the `data/history.json` file. This file can be thought of as a “recipe” that can be applied to the raw data at any point and used to recreate the mapped file, `sp500_yahoo_mapped_to_damodaran.csv`.

### Phase 2: Relational Data Integration (The Merge)

After our firm-level and benchmark industry labels were standardized, we ran the firm-level and industry-level data integration using the `scripts/merge_data.py` script.

**Integration Logic**
We used the pandas library and performed a relational left join. We used the firm-level dataset (`sp500_yahoo_mapped_to_damodaran.csv`) as the left table and the Damodaran industry benchmark dataset as the right table. We joined on the standardized `DamodaranIndustry` column.

**Handling Unmatched Records**
An important part of this phase was handling data that failed to meet a benchmark but still maximizing the overall data coverage. Our merge script was designed to handle firms that did not receive a benchmark. We joined 502 out of 503 total observations in our final run. The single observation that did not join was the original dataset from Yahoo Finance that had no industry classification, making it impossible to join a benchmark to it. The result of this integration is saved as `data/final_dataset.csv`.

### Phase 3: Numerical Standardization and Statistical Cleaning

The final phase of our dataset is a clean-up phase, where we ran the `scripts/clean_data.py` script to ensure we had the proper data structure and statistical properties to feed into our OLS regression.

**1. Data Type Casting**
Ensuring we do not have any computational errors, we explicitly cast all critical financial variables to float64 numerical types (`Dividend Yield`, `Payout Ratio`, and `Net Margin`). All downstream statistical calculations in statsmodels will be performed with precision as a result. (Dividend Yied was only used for testing in an early phase, and only here for potential future research.)

**2. Zero-Imputation Strategy**
Some of the S&P 500 firms, especially in highly growth-oriented sectors like Technology, do not pay dividends. In the raw data, these firms will show up as NaN on `Payout Ratio` and `Dividend Yield`. We decided to strategically impute these NaNs as 0.0. This is a critical curation decision: treating non-dividend payers as “zero” as opposed to “missing” allows us to have a representative set of all the S&P 500. If we simply removed these rows, we would be left with only a set of mature firms, creating a huge selection bias.

**3. Outlier Mitigation and Bounding**
Financial data is fraught with extreme outliers, such as a company that has seen its earnings collapse but still manages to pay its dividend results in a `Payout Ratio` of greater than 1,000%. We do not want any of these outliers to influence our regression coefficients in a detrimental way. As a result, we applied the following statistical bounds:
* **Payout Ratio Bounding**: We removed any observations where the `Payout Ratio` was less than 0 or greater than **5.0** (500%). 
* **Dividend Yield Bounding**: We removed any observations with a `Dividend Yield` greater than **20%**. 
These thresholds were selected to ensure that our dataset reflects "steady-state" corporate policies rather than temporary financial distress or accounting anomalies.

**4. Final Filtering**
At the final step we removed any remaining row without a critical `Net Margin` benchmark from the Damodaran dataset.

### Final Dataset Integrity
The result of this rigorous cleaning process is the `data/clean_final_dataset.csv`, which contains 493 high-quality observations with no missing values in any critical field. We achieved this by using rule-based mapping in OpenRefine and precise numerical cleaning in Python. The final dataset is 100% reproducible from the raw files.

---

## Findings

During the analytical phase of this project, we employed a `Ordinary Least Squares regression model (OLS)` to determine whether or not industry-level profitability (as measured by `Net Margin`) is a strong predictor for firm-level Dividend `Payout Ratios` for a set of S&P 500 companies. We were interested in determining the explanatory power of industry benchmarks over individual corporate policies.

### Statistical Performance and Predictive Capability
The output from our statistical scripts have given us a clear indication that our model has some serious limitations:

**Model Fit**: The model returned an **R-squared ($R^2$) of 0.054** and an **Adjusted R-squared of 0.052**. This statistic is important because it shows that the Net Margin at the industry level explained only **5.4%** of the variance in the firm-level payout ratio. Therefore, more than **94.6%** of the variance in how S&P 500 companies pay out dividends to shareholders is not explained by industry profitability alone.
**Significance Paradox**: The model yielded an **F-statistic of 28.21** with a highly significant p-value of **$1.63 \times 10^{-07}$**. While this is important because it shows that the relationship between these variables is statistically significant (i.e. not due to random chance), the extremely low further shows that the relationship is fairly weak and has little predictive utility for financial forecasting.
**Coefficient Analysis**: The coefficient for `Net_Margin` was calculated at **-0.0051** with a p-value of **0.000**. This finding is quite surprising because it indicates that, for every 1% increase in the average profitability of an industry, the constituent firm's payout ratio is expected to decrease by ~0.0051%. This is somewhat unintuitive because, typically, more profitable industries would allow for higher dividends payouts.

### Visual Interpretation of the Relationship
The visualizations produced from our data set further support the weak correlation between these financial ratios:

**Regression Scatter Plot**: The plot shows significant dispersion in the data points. Most S&P 500 firms fall within the lower range of the payout spectrum (0.0-0.6) regardless if their industry net margin is 5% or 25%. The resulting regression line is nearly flat and provides a visual indication that the independent variable provides little leverage in predicting the dependent variable. The chart also shows that dividend paying behavior is firm-specific. We noticed that most firms in high-margin sectors, like Tech, retain the majority of their earnings for re-investment and as a result have close-to-zero or low payout ratios. Whereas firms in lower-margin but “mature” sectors like Utilities or Staples, have much higher payouts.

### Conclusion on Predictive Validity
Our final output from our analysis is that Industry Net Margin is not a significant standalone predictor for dividend policies of S&P 500 companies in general. High variance and poor linear correlation is observed. In a professional or academic setting, using industry-wide profitability to predict a particular firm’s dividend payout ratio is highly unreliable. These results suggest that corporate dividend distribution is a function of firm-specific internal strategies (e.g. debt level, growth mandate, cash flow needs) and is not passive reflection of industry-wide profitability. Therefore, while industry benchmarks can be used for general health checks, they should not be used as a replacement for proper firm-level financial analysis in predicting shareholder returns.

---

## Future Work

The completion of the S&Ps 500 dividend policy study serves as a starting point for broader research on corporate financial behavior. By reflecting on the life of our data and the technical concepts we’ve discussed throughout the project, we’ve identified several concrete directions for future work that take us beyond simple linear modeling towards more robust, scalable, and transparent financial analysis.

### Scaling and Scope: Beyond the S&P 500
The most important thing we learned from our analysis is that our sample was too small: we had a high-market-cap sample of only 500 companies that represent the 500 largest firms in the U.S. economy. The S&Ps are survivorship and selection biased. We should do work to collect data from the Russell 3000 or global indices like the MSCI World to answer questions that our current model did not, especially industry-specific questions.
More observations: Going from 500 firms to 3000+ will increase the statistical power of our regression and might be able to show industry-specific trends that we currently don’t see accounting for the Minimum Count “gap” in “Minimum Count”. We should be able to collect these larger datasets programmatically via diverse APIs. This would allow us to test whether the weak correlation we saw across the S&Ps extends to small-cap and mid-cap firms, which may be more correlated with industry profitability benchmarks than their larger cash-rich counterparts.

### Advanced Data Integration and Record Linkage
We used rule-based transformations to integrate datasets together. In future work, maybe we should implement probabilistic record linkage to move beyond keyword-based GREL rules. Like, a pipeline using indexing and blocking to manage computational complexity should be implemented. We should apply comparison functions like Jaro-Winkler or even AI-onvolved approach for industry labels (in which we think reproducibility could be an issue and would need more work to be put into). It is really interesting to see how AI evolves so quickly in almost every moment. And we believe, AI classification on industry/company can be useful to work on.

### Multi-Dimensional Data Quality Assessment
The integration phase shouldn’t be viewed as a clean up after the fact but rather a upstream proactive record linkage that can scale to thousands of firms across multiple different financial sources without touching them manually.

To increase the rigor of our results, future work should extend our analysis to include a multi-dimensional data quality assessment. Rather than a superficial “outlier removal” procedure, we would like to systematically assess dimensions of accuracy, completeness, consistency, and timeliness. For example, as part of a “timeliness” assessment, we should quantify the time-lag problem we identified — computing the exact delta between Damodaran’s annual benchmarks and Yahoo Finance’s real-time payout ratios — and determine if there are any spikes or trends in that delta.

Future work can involve more rigorous data cleaning for semantic/ syntactic snomalies. We want to ensure our numerical inputs are “fit for use” in more complex multivariate models that might include debt-to-equity or free cash flow ratios.

### Longitudinal Automation and Provenance
Finally, the project should move beyond a static analysis and evolve into a longitudinal, dynamic pipeline. Future research should make use of workflow automation tools like Snakemake to manage the end-to-end process from data acquisition to analysis results. By automating this workflow, if new annual benchmarks are released, we can re-run the entire analysis with a single command. This workflow ensures a clear record of data provenance. We should then combine this automation with version control for data artifacts to perform a time-series analysis to determine if the relationship between industry health and dividend policy varies over time — for example, are certain economic cycles (high-inflation, market downturns, etc.) associated with different relationships? This would represent the ultimate “living” research pipeline we desire for reproducible financial data science.

---

## Challenges

One of the biggest challenges we faced throughout this project was the semantic difficulty of working with datasets of fundamentally different levels of granularity. Part of overcoming the industry alignment challenge hurdle we faced was moving to an OpenRefine-based workflow, but the conceptual difficulty of mapping highly-specific Yahoo Finance tags to broader Damodaran benchmarks was a significant manual burden. While we used GREL expressions to automate keyword-based grouping, the high-level decision of whether or not “Internet Retail” really belonged under a general “Retail” benchmark or should have its own more-specific category required a close watcher to ensure that our mapping logic didn’t accidentally wash away important financial distinctions between firms. The mapping process was less of an easy automation and more of a difficult curation task that required a balance between letting the data drive our integration logic and applying our accounting intuition.

But beyond the technical integration we had to do, we also had an interesting issue to deal with in terms of the legal/provenance of our data (specifically the NYU Stern data). Normally, one can just download a standard data set and have a clear example of a machine-readable license such as MIT or Creative Commons. In contrast, Professor Damodaran’s site states his rules of usage in spoken language – an acknowledgement such as “If you do use my data and wish to acknowledge that you did get my data off my site, I thank you. If not, I will not lose any sleep and you should not either.” As a result, we had the interesting problem of having to interpret the spoken-language “terms” of his site as a form of summary of intent (i.e. the data is essentially public domain for intents-and-purposes of academia/personal use with an intent of informal attribution). Dealing with the spoken-language guidance of Professor Damodaran and trying to translate it into an ethical statement for our project report was a challenge in transparency; as we had to ensure our usage remained compliant with academic standards while acknowledging that we were working without a standard license code. It's just overall ambiguous.

We then encountered a procedural hurdle regarding "one-click" automation, as the technical stack created friction between Python-based acquisition and OpenRefine-based curation. Moreover, the findings may suggest that OpenRefine's nature could preclude a unified master script, creating an automation gap where the transition from raw API output to a merged dataset requires manual intervention. Furthermore, the significant friction point may indicate that manual interactions could introduce inconsistencies that a fully automated workflow prevents. In light of these results, the evidence might suggest that rather than providing a single "run-all" script, we should chose to explicitly detail each discrete execution step in the reproducibility section to ensure researchers can achieve computational reproducibility. Documenting this human-mediated provenance risks data provenance transparency. However, the key findings may suggest that documenting this process with enough precision could demonstrate that transparency for external researchers was a daunting task that extended far beyond standard coding. Therefore, the results could indicate that this friction between Python-based acquisition and OpenRefine-based curation appears to create reproducibility challenges researchers must address carefully. 

---

## Reproducing & Metadata

To reproduce the analysis and results of this project, follow the sequence below. Note that individual contributions are documented in the Git commit history as required.

All required datasets, scripts, OpenRefine history files, intermediate outputs, and final outputs are included directly in this GitHub repository. No external Box storage is required.

A lightweight workflow script (`run_workflow.sh`) is included to automate the Python-based portion of the pipeline after the OpenRefine mapping step has been completed.

### Metadata

[View Project Metadata (DCAT JSON-LD)](./metadata.json)

[View Data Dictionary](./data_dictionary.txt)

[View Python Package Record](./pip_freeze.txt)


### 1. Environment Setup

Install dependencies using:

```bash
pip install -r requirements.txt
```

This project was developed using Python and the following major packages:

* `pandas == 2.2.2`
* `yfinance == 1.2.0`
* `statsmodels == 0.14.0`
* `matplotlib == 3.8.0`
* `seaborn == 0.13.0`
* `openpyxl == 3.1.5`
* `scikit-learn == 1.3.0`

A complete record of the package versions used in our development environment is included in:

```text
pip_freeze.txt
```

This file was generated using:

```bash
pip freeze > pip_freeze.txt
```

### 2. Data Acquisition

Run the acquisition script to fetch the current S&P 500 financial data from Yahoo Finance:

```bash
python scripts/pull_dividend_data.py
```

This will generate:

```text
data/sp500_dividend_data.csv
```

The Damodaran benchmark dataset is included directly in the repository as:

```text
data/marginGlobal.xls
```

### 3. Industry Mapping (OpenRefine)

The industry mapping requires OpenRefine to apply the rule-based transformations.

1. Open **OpenRefine** and create a new project using:

```text
data/sp500_dividend_data.csv
```

2. Click **Undo/Redo** and select **Apply**.

3. Paste the contents of:

```text
data/history.json
```

into the text area and click **Perform Operations**.

4. Export the resulting project as:

```text
data/sp500_yahoo_mapped_to_damodaran.csv
```

This file is already included in the repository for reproducibility and transparency.

### 4. Data Quality Assessment

To reproduce the data quality assessment and SHA-256 integrity checks, run:

```bash
python scripts/quality_report.py
```

This script verifies:
- SHA-256 hashes of the raw datasets
- Missing values
- Duplicate rows
- Summary statistics
- Dataset dimensions

for the raw, merged, and cleaned datasets.

### 5. Integration and Cleaning

Run the following scripts to merge the datasets and apply cleaning logic (handling NaNs and outliers):

```bash
python scripts/merge_data.py
python scripts/clean_data.py
```

This generates:

```text
data/final_dataset.csv
data/clean_final_dataset.csv
```

### 6. Analysis and Visualization

To generate the regression statistics and visualizations, run:

```bash
python scripts/analysis_modified.py
python scripts/analysis_visualization_test.py
```

The regression summary will be printed to the console, and the visualizations will be displayed or saved as artifacts.

### 7. Expected Final Outputs

After reproducing the workflow, the following key outputs should exist:

```text
data/sp500_dividend_data.csv
data/sp500_yahoo_mapped_to_damodaran.csv
data/final_dataset.csv
data/clean_final_dataset.csv
```

The final analytical dataset is:

```text
data/clean_final_dataset.csv
```

This dataset contains 493 cleaned observations with no missing values in critical analytical fields.

Additional documentation artifacts included in the repository:

```text
data_dictionary.txt
metadata.json
README.md
reports/ProjectPlan.md
reports/StatusReport.md
requirements.txt
pip_freeze.txt
LICENSE
run_workflow.sh
```

### 8. Licensing and Usage Notes

The code in this repository is intended for educational and research purposes.

Yahoo Finance data was accessed through the `yfinance` Python library and remains subject to Yahoo Finance’s terms of service.

The Damodaran dataset is publicly distributed by Professor Aswath Damodaran (NYU Stern School of Business) for educational and research use with attribution.

---

## References

* **Aroussi, R.** *yfinance: Download market data from Yahoo! Finance's API*. GitHub Repository. [https://github.com/ranaroussi/yfinance](https://github.com/ranaroussi/yfinance)
* **Damodaran, A. (2026).** *Margins by Industry*. NYU Stern School of Business. [https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html)
* **OpenRefine.** *A free, open source, powerful tool for working with messy data*. [https://openrefine.org/](https://openrefine.org/)
* **Yahoo Finance.** *Yahoo Developer API Terms of Use*. [https://legal.yahoo.com/us/en/yahoo/terms/developer/index.html](https://legal.yahoo.com/us/en/yahoo/terms/developer/index.html)
* **scikit-learn developers.** *scikit-learn: Machine Learning in Python*. [https://scikit-learn.org/](https://scikit-learn.org/)
