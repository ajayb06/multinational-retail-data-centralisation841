from database_utils import DatabaseConnector
import pandas as pd  
import tabula
import requests

class DataExtractor:
    def __init__(self):
        db_connector = DatabaseConnector()
        self.db_engine = db_connector.init_db_engine()
        self.api_key = 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'
        self.headers = {'x-api-key': self.api_key}

    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, con=self.db_engine)

    def retrieve_pdf_data(self, link):
        dataframe = tabula.read_pdf(link,pages='all', stream=True)
        combined_database = pd.concat(dataframe, ignore_index=True)
        return combined_database

    def list_number_of_stores(self):
        response = requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', headers=self.headers)
        if response.status_code == 200:
            number_of_stores = response.json().get('number_stores')
            return number_of_stores
        else:
            raise Exception("Failes to retrieve number of stores")
    
    def retrieve_store_data(self):
        number_of_stores = self.list_number_of_stores()
        all_store_data = []
        for store_number in range(number_of_stores):
            response = requests.get(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}', headers=self.headers)
            if response.status_code == 200:
                print(response.json())
                store_data = response.json()
                all_store_data.append(store_data)
            else:
                raise Exception(f'Failed to retreive data for store {store_number}')
        
        return pd.DataFrame(all_store_data)
    