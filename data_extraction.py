from database_utils import DatabaseConnector
import pandas as pd  
import tabula

class DataExtractor:
    def __init__(self):
        db_connector = DatabaseConnector()
        self.db_engine = db_connector.init_db_engine()

    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, con=self.db_engine)

    def retrieve_pdf_data(self, link):
        dataframe = tabula.read_pdf(link,pages='all', stream=True)
        combined_database = pd.concat(dataframe, ignore_index=True)
        return combined_database
