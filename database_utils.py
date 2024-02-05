import yaml
from sqlalchemy import create_engine, text
import pandas as pd

class DatabaseConnector:
    def __init__(self):
        # Initialisation of the DatabaseConnector class
        pass

    def read_db_creds(self, filepath='db_creds.yaml'):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)

    def init_db_engine(self):
        creds = self.read_db_creds()
        engine = create_engine(f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        with engine.connect() as connection:
            query = text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            result = connection.execute(query)
            tables = [row[0] for row in result]
            return tables
    
    def upload_to_db(self, df, table_name):
        creds = self.read_db_creds()
        engine = create_engine(f"postgresql://{creds['MY_USER']}:{creds['MY_PASSWORD']}@{creds['MY_HOST']}:{creds['MY_PORT']}/{creds['MY_DATABASE']}")
        df.to_sql(table_name,engine, if_exists='replace', index=False)
