# Employee Workforce & Productivity Analytics

## Project Overview

Employee Workforce & Productivity Analytics is an end-to-end data analytics project that analyzes employee workforce data, productivity, training, performance, satisfaction, overtime, and resignation patterns.

The project combines **Python, SQL, SQLite, and Power BI** to perform data analysis and create an interactive analytics dashboard.

## Business Objective

The main objectives of this project are to:

* Analyze employee workforce distribution across departments
* Understand employee performance patterns
* Analyze training hours and performance
* Examine overtime and employee productivity
* Study employee satisfaction
* Analyze resignation patterns
* Build an interactive Power BI dashboard for business insights

## Technology Stack

* **Python**
* **Pandas**
* **NumPy**
* **SQLite**
* **SQL**
* **Power BI**
* **Git & GitHub**

## Dataset

Dataset: **Employee Performance and Productivity Data**

The dataset contains employee-level information such as:

* Employee ID
* Department
* Gender
* Age
* Job Title
* Hire Date
* Years at Company
* Education Level
* Performance Score
* Monthly Salary
* Work Hours per Week
* Projects Handled
* Overtime Hours
* Sick Days
* Remote Work Frequency
* Team Size
* Training Hours
* Promotions
* Employee Satisfaction Score
* Resignation Status

## Project Workflow

```text
Employee Dataset
      ↓
Data Validation using Python
      ↓
Data Analysis using Python
      ↓
SQLite Database
      ↓
SQL Analysis
      ↓
Analysis Result CSV Files
      ↓
Power BI Dashboard
      ↓
Business Insights
```

## Python Data Analysis

Python was used for:

* Dataset validation
* Missing-value checking
* Duplicate checking
* Category analysis
* Numerical analysis
* Department performance analysis
* Productivity analysis
* Training analysis
* Resignation analysis
* Creation of analysis-ready datasets

## SQL Analysis

The employee dataset was loaded into a SQLite database using Python.

SQL was used to analyze:

* Employee count by department
* Department performance
* Overall resignation rate
* Resignation by department
* Resignation by overtime level
* Resignation by satisfaction level
* Training level vs performance

### Database

```text
Database: employee_productivity.db
Table: employee_productivity
Records: 100,000
```

## Training Analysis

Training hours were grouped into four levels:

* Low Training
* Medium Training
* High Training
* Very High Training

The SQL analysis produces:

* Employee count by training level
* Average training hours by training level
* Average performance score by training level

The analysis showed that average performance scores were very close across the training groups in this dataset. Therefore, the project does not treat training as proof of a causal improvement in performance.

## Power BI Dashboard

The Power BI dashboard provides an interactive view of employee workforce and productivity data.

### Dashboard KPIs

* Total Employees
* Average Monthly Salary
* Average Performance Score
* Resignation Rate

### Dashboard Visuals

* Employees by Department
* Average Performance by Department
* Resigned Employees by Department
* Average Projects Handled by Department
* Average Work Hours by Department
* Average Employee Satisfaction by Department
* Overtime Hours vs Performance Score
* Training Hours vs Performance Score

### Interactive Filters

* Department
* Education Level

## Training & Performance Analysis Page

A separate analysis section contains:

* Training Level vs Average Performance
* Employee Count by Training Level
* Average Training Hours by Training Level
* Training Hours vs Performance

## Key Project Insights

The project is designed to help analyze workforce patterns such as:

* Department-wise employee distribution
* Differences in employee performance
* Workforce productivity indicators
* Training distribution
* Employee satisfaction
* Overtime patterns
* Resignation patterns

All observations are based on the available dataset and are presented as descriptive analysis rather than causal conclusions.

## Project Structure

```text
employee-workforce-productivity-analytics/
│
├── data/
│   └── employee_productivity.csv
│
├── development/
│   ├── analysis_performance.py
│   ├── analysis_productivity.py
│   ├── analysis_training.py
│   ├── check_categories.py
│   ├── check_data.py
│   ├── check_numbers.py
│   └── create_analysis_dataset.py
│
├── results/
│   ├── employee_analysis.csv
│   └── training_analysis.csv
│
├── sql/
│   ├── analysis_queries.sql
│   ├── department_analysis.sql
│   └── run_query.py
│
├── .snapshots/
│
├── create_database.py
├── employee_productivity.db
└── README.md
```

## How to Run

### 1. Install dependencies

```bash
pip install pandas
```

### 2. Create the SQLite database

```bash
python create_database.py
```

Expected output:

```text
Database created successfully!
Table created: employee_productivity
Total records: 100000
```

### 3. Run SQL analysis

```bash
python sql/run_query.py
```

The SQL analysis result is saved to:

```text
results/training_analysis.csv
```

## Power BI

The Power BI dashboard was created using the analysis-ready employee dataset and SQL-derived analysis results.

The dashboard includes interactive slicers and multiple workforce, productivity, training, performance, and resignation visualizations.

## Skills Demonstrated

* Python data analysis
* Pandas data manipulation
* SQL querying
* SQLite database management
* Data cleaning and validation
* Exploratory data analysis
* Business analytics
* Power BI dashboard development
* Data visualization
* Git and GitHub project management


## Author

**Sowndarya J**

MCA | Aspiring Data Analyst / Data Scientist
