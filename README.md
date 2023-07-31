# README

## Introduction

This project uses time series data about climate change to better understand how air pollution levels have changed over time. To do so, we mainly used data from the 2022 Environmental Performance Index EPI, which evaluates 180 countries’ performance on 40 climate performance indicators (Wolf et al., 2022a) and queried data from World Economic Outlook Database. The EPI gathers all 40 indicators to calculate performance “scores” for countries, ranking their environmental performance overall and their performance by region (Wolf et al., 2022c). Our specific focus for this project is air pollution. As a result, we chose to study indicators for the following: (1) two trend rates, for CO2 and N2O, (2) three measurements disability-adjusted life-years lost per 100,000 people (DALY rate), for household air pollution, ozone exposure, and particulate matter, and (3) four pollution-level indicators, for NO and N2O, for SO2, volatile organic compound levels, and CO. 

## Data Link
- WEO Database: https://www.imf.org/en/Publications/WEO/weo-database/2023/April/select-country-group  
- EPI2022 Raw Data: https://epi.yale.edu/downloads/epi2022rawdata.zip
- Other Related EPI Data: https://epi.yale.edu/downloads

## Report Link
https://bit.ly/air_pollution_analysis_report

## Running Instructions

This repository contains a collection of Jupyter notebooks and data files for analyzing pollution trends as well as the relationship between environmental indicators and fundamental economic factors across various countries and time windows. Please follow the instructions below to run the code and reproduce the visualization analysis.

#### 1. Clone the Repository
First, clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

#### 2. Set Up the Environment
Ensure that you have Python and Jupyter Notebook installed. It is recommended to use a virtual environment to manage dependencies. 

To create and activate a virtual environment, run:
###### For MacOS
```bash
python -m venv env
source env/bin/activate
```

###### For Windows
```bash
py -m venv env
env\Scripts\activate
```

Then, install the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

#### 3. Run the Jupyter Notebooks
Start the Jupyter Notebook server by running:

```bash
jupyter notebook
```

This will open a new browser window with the Jupyter Notebook interface. Now you can navigate to the desired notebook and run the cells as needed.




#### * Notebooks Overview
- <strong>exploration_<indicator_name>.ipynb:</strong> Use this notebook to generate the trend of pollution levels for selected indicators and selected countries over time.    
- **exploration_single_country.ipynb:** Use this notebook to generate time series plots for all indicators across selected countries.  
- **exploration_streamline_indicators.ipynb:** Use this notebook to generate time series plots for all indicators across all the countries.  
- **calculate_pearson_correlation.ipynb:** Use this notebook to plot heatmapw of Pearson correlation coefficients under various perspectives.


#### * View the Plots  
All generated plots are saved in the plots folder. Browse the folder to find the visualizations you are interested in.




