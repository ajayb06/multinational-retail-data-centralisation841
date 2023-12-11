import csv
import requests
import boto3
import pandas as pd
from database_utils import DatabaseConnector

class DataExtractor:
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        query = f"SELECT * FROM {table_name};"
        with engine.connect() as connection:
            data = pd.read_sql(query, connection)
        engine.dispose()
        return data
