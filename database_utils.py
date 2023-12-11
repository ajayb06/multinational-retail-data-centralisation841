import psycopg2
import yaml
from sqlalchemy import create_engine

class DatabaseConnector:

    def read_db_creds(self, creds_file_path="db_creds.yaml"):
        with open(creds_file_path, "r") as file:
            return yaml.safe_load(file)
        
    def init_db_engine(self):
        creds = self.read_db_creds()
        db_url = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        return create_engine(db_url)
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        with engine.connect() as connection:
            tables = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';").fetchall()
        engine.dispose()
        
        return [table[0] for table in tables]
    
    def upload_to_db(self, data_frame, table_name):
            engine = self.init_db_engine()
            with engine.connect() as connection:
                 data_frame.to_sql(table_name, connection, if_exists='replace', index=False)
            engine.dispose()
        


       