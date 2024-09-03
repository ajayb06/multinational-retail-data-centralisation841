# Multinational-Retail-Data-Dentralisation

#### Project Summary

The primary objective of our project is to unify this information into a star-schema database for optimised queries. The initial phase involves constructing a system that merges all of our existing data into a single, cohesive database. Subsequent phases will focus on utilizing this unified database to extract up-to-date business metrics, thereby enhancing decision-making processes, improving operational efficiency, and providing actionable insights for strategic growth.

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

#### Project Workflow
This project is designed to extract, clean, and store data from multiple sources using a combination of Python scripts. Here is a step-by-step guide to how the project operates:

Step 1: Data Extraction

1. Initialize Data Extraction: Start by running data_extraction.py. This script is responsible for connecting to various data sources and pulling data into the system.
   * For AWS RDS databases, the script connects and pulls data tables into pandas DataFrames.
   * For AWS S3 buckets, it retrieves PDF, CSV, and JSON files and converts them into usable data formats.
   * For REST APIs, it fetches JSON data and loads it directly into a DataFrame.

Step 2: Data Cleaning

2. Clean Extracted Data: After extraction, use data_cleaning.py to process the imported data.
   * Instantiate the DataCleaning class.
   * Call appropriate methods to clean data from each specific source. This may include normalizing formats, correcting errors, and handling missing values.

Step 3: Uploading Data

3. Database Setup and Connection: Before uploading the cleaned data, set up and configure the database connection using "database_utils.py".
   * Use the "DatabaseConnector" class to create a connection to your database. This connection uses credentials stored in a ".yml" configuration file, ensuring that access is secure and configurable.
4. Upload Data: With the database connection established, use the methods defined in "main.py" to upload the cleaned data.
   * The script ensures that data is uploaded in the correct order and integrated into the appropriate tables, such as "dim_date_times" for date-time data or other specific tables based on the project's schema.

Step 4: Operational Execution

5. Run the Main Script: Execute main.py to orchestrate the entire process.
   * This script calls functions from other modules in sequence to ensure data flows smoothly from extraction, through cleaning, to storage.

Step 5: Monitoring and Maintenance

6. Monitor the Process: Keep an eye on the execution process. Ensure there are no errors or interruptions.
7. Maintain the System: Regularly update the scripts and configurations as necessary to adapt to any changes in data source structures or database schema updates.

## Installation
### Prerequisites
- **Python** : The project is developed using Python. Ensure you have Python 3.7 or newer installed on your system. You can download Python from [Python's official site.](https://www.python.org/downloads/)
- **pip**: Python's package installer, pip, should be installed automatically with Python. Ensure it is updated to the latest version.
- **AWS CLI**: This project interacts with AWS services. Install the AWS Command Line Interface (CLI) by following the guidelines available on the [AWS CLI documentation page.](https://aws.amazon.com/cli/)

```bash
git clone https://github.com/ajayb06 multinational-retail-data-centralisation841.git
cd ../retail-data-centralisation841
python main.py
```
### Install required packages
Note: It is recommended that you set up a virtual environment to manage the dependencies effectively.

```bash
pip install -r requirements.txt
```

### Configure AWS credentials
Note: To interact with AWS services, configure your AWS credentials using the AWS CLI.
```bash
aws configure
```
Follow the prompts to input your *AWS Access Key ID*, *Secret Access Key*, *default region*, and output format. These credentials are necessary for the project to access AWS resources.

### Database Configuration
Ensure the database credentials are properly configured in your ".yml" or ".env" file. You should specify the database **host**, **port**, **username**, **password**, and database name according to your setup.

### Running the Project
```bash
python main.py
```

### File Structure

```
multinational-retail-data-centralisation/
│
├── main.py                         # Main entry point for the project
├── data_cleaning.py                # Python script for cleaning and transforming data
├── data_extraction.py              # Python script for data extraction from various sources
├── database_utils.py               # Python utility functions for database interaction
├── requirements.txt                # List of dependencies required for the project
├── .gitignore                      # Files and directories to be ignored by Git
├── README.md                       # Project documentation
└── __pycache__/                    # Directory containing compiled Python files
```


### Next Step
After installation, you can start using the project as needed. If you encounter any issues, review the installation steps and ensure all configurations are correct. If you're still encountering issues contact me via email balakrishnanajay06@gmail.com

### License

MIT License

Copyright (c) 2024 by Ajay Balakrishnan
