# **Economic Data Analysis from Wikipedia**

## **Overview**
This project focuses on extracting and analyzing economic data from Wikipedia pages of sovereign states. The objective is to collect, preprocess, and analyze data to uncover relationships between variables like GDP, Human Development Index (HDI), Gini Index, population, and land area. The workflow includes web scraping, data cleaning, exploratory data analysis, and statistical modeling.

---

## **Key Features**
- **Web Scraping**: Automated data collection using `requests` and `lxml` libraries.
- **Data Cleaning**: Handling missing values, converting data types, and normalizing entries.
- **Descriptive Analysis**: Summary statistics and visualizations to understand data trends.
- **Correlation Analysis**: Investigating relationships between variables such as GDP, population, and inequality.
- **OLS Regression Modeling**: Building predictive models to identify key factors influencing GDP per capita.

---

## **Project Workflow**

### 1. **Web Scraping**
   - Extracts URLs for sovereign states from Wikipedia’s "List of Sovereign States" page.
   - Scrapes key data fields from individual country pages, including:
     - GDP (total and per capita)
     - Population
     - Land Area
     - HDI Index
     - Gini Index
   - Data is compiled into a structured CSV file (`countries_data.csv`).

### 2. **Data Preparation**
   - **Cleaning**: 
     - Converting GDP values to trillions.
     - Handling missing or "Not available" entries.
     - Extracting numeric values from strings.
   - **Preprocessing**: Normalizing data formats for further analysis.

### 3. **Descriptive Statistics**
   - Computes summary statistics for key variables.
   - Applies log transformations to normalize skewed distributions.
   - Generates histograms to visualize distributions and patterns.

### 4. **Exploratory Data Analysis**
   - **Insights from Correlations**:
     - Examines relationships between GDP, HDI, inequality, and population.
     - Visualized through scatter plots with trendlines.
   - **Key Observations**:
     - Countries with high GDP often have better HDI but may exhibit income inequality.
     - Population size and land area show strong positive correlation.

### 5. **OLS Regression Modeling**
   - Uses GDP per capita as the dependent variable.
   - Considers HDI, Gini Index, and population as independent variables.
   - Results reveal that HDI is the strongest predictor of GDP per capita.

---

## **Results and Insights**
- **High GDP, Low HDI**: Countries like Nigeria and Pakistan exhibit high economic output but low human development, highlighting disparities.
- **GDP Per Capita vs Inequality**: Countries like Singapore and Saudi Arabia show high average wealth with significant income inequality.
- **Key Drivers of Economic Growth**: Investments in human development (education, healthcare) are critical for boosting GDP per capita.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - Data Collection: `requests`, `lxml`
  - Data Processing: `pandas`, `numpy`
  - Data Visualization: `matplotlib`, `seaborn`
  - Statistical Modeling: `statsmodels`

---
## **Future Improvements**
Extend the dataset to include additional socio-economic indicators.
Implement advanced statistical or machine learning models.
Automate regular data scraping to keep the dataset updated.

