import yaml
from sqlalchemy import create_engine, text

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
    
db_connector = DatabaseConnector()
table_names = db_connector.list_db_tables()
print("Tables in the database:", table_names)
