# Multinational-Retail-Data-Dentralisation

#### Project Summary

As a global enterprise offering a diverse range of products worldwide, we're facing a challenge with scattered sales information from various channels, complicating our analysis efforts. The primary objective of our project is to unify this information into a centralized, easily analyzable repository. The initial phase involves constructing a system that merges all of our existing data into a single, cohesive database. Subsequent phases will focus on utilizing this unified database to extract up-to-date business metrics, thereby enhancing our company's capacity for data-informed decision-making.

#### Data Intergration From Multiple Sources
These are the following sources where data was extracted from:
- Data stored in AWS RDS
- PDF stored in a AWS S3 Bucket
- JSON data from REST API
- A CSV file in a AWS S3 Bucket
- JSON file stored in a AWS S3 Bucket

#### Project Utilities
- Main --> The "main.py" script orchestrates the project's workflow. It utilizes methods defined in other scripts to extract data, clean it, and ultimately upload it into a local or cloud-based database. This script acts as the central hub for managing the data flow throughout the project.
- Data Extraction --> Located in "data_extraction.py", this script contains various methods designed to fetch data from multiple sources and load it into pandas DataFrames. The supported sources include:

  * AWS RDS databases
  * PDF and CSV files from AWS S3 buckets
  * JSON data from REST APIs
- Data Cleaning --> The "data_cleaning.py" script features the "DataCleaning" class, which is dedicated to processing and cleaning the data extracted by "data_extraction.py". This class ensures that the data is formatted correctly, free of errors, and prepared for analysis or storage.
- Data Utils --> The "database_utils.py" file contains the "DatabaseConnector" class. This class is crucial for setting up the database engine, utilizing credentials stored in a ".yml" file to securely connect to the database. This setup is essential for the subsequent storage of cleaned data.

