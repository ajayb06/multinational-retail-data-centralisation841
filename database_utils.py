import yaml
from sqlalchemy import create_engine, text
import pandas as pd
from typing import List,Dict,Any

class DatabaseConnector:

    """Class responsible for database interactions including reading credentials,
    initializing connections, listing tables, and uploading data to the database."""

    def __init__(self):

        """Initializes the DatabaseConnector class."""

        pass

    def read_db_creds(self, filepath: str ='db_creds.yaml')->Dict[str,Any]:

        """Reads database credentials from a YAML file.
        
        Args:
            filepath (str): Path to the YAML file containing database credentials.
        
        Returns:
            Dict[str, Any]: A dictionary containing database credentials.
        """

        with open(filepath, 'r') as file:
            return yaml.safe_load(file)

    def init_db_engine(self)->Any:

        """Initializes and returns a SQL Alchemy database engine using credentials from a YAML file.

        Returns:
            sqlalchemy.engine.base.Engine: A SQL Alchemy database engine.
        """

        creds = self.read_db_creds()
        engine = create_engine(f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(self)->List[str]:

        """Lists all tables in the public schema of the connected database.

        Returns:
            List[str]: A list of table names in the public schema of the database.
        """
        
        engine = self.init_db_engine()
        with engine.connect() as connection:
            query = text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            result = connection.execute(query)
            tables = [row[0] for row in result]
            return tables
    
    def upload_to_db(self, df:pd.DataFrame, table_name:str)->None:

        """Uploads a DataFrame to a specified table in the database.

        Args:
            df (pd.DataFrame): The DataFrame to upload.
            table_name (str): The name of the target table in the database.

        Returns:
            None
        """
        
        creds = self.read_db_creds()
        engine = create_engine(f"postgresql://{creds['MY_USER']}:{creds['MY_PASSWORD']}@{creds['MY_HOST']}:{creds['MY_PORT']}/{creds['MY_DATABASE']}")
        df.to_sql(table_name,engine, if_exists='replace', index=False)
