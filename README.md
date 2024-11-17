# Kayla_Haeussler_MiniProject11  
IDS 706: Mini Project 11  
Data Pipeline with Databricks  
Kayla Haeussler 

[![CI](https://github.com/nogibjj/Kayla_Haeussler_MiniProject10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Kayla_Haeussler_MiniProject10/actions/workflows/cicd.yml)   

## Assignment Requirements
- Create a data pipeline using Databricks
- Include at least one data source and one data sink

## Functionality
This project utilizes PySpark to analyze election data, focusing on incumbent and challenger statistics by state and party. The core functionalities include:

- Data Loading: Reads CSV files into Spark DataFrames for efficient large-scale data processing.  
- Data Transformation: Adds a column containing a confidence interval range for each candidate’s vote share.  
- SQL Query Execution: Runs a Spark SQL query to aggregate counts of incumbents and challengers by state and party.  
- Data Saving: Exports processed DataFrames as CSV files.
Logging: Logs key operations and results to a markdown file for easy review of outputs, titled ```pyspark_output,md```

These functions collectively support election data analysis in distributed computing environments, offering both flexibility and scalability.

