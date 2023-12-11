import psycopg2
import yaml
from sqlalchemy import create_engine

class DatabaseConnector:

    def read_db_creds(self, creds_file_path="db_creds.yaml"):
        with open(creds_file_path, "r") as file:
            return yaml.safe_load(file)
        
    def init_db_engine(self):
        creds = self.read_db_creds()
        db_url = f"postgresl://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        return create_engine(db_url)