from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
from data_extraction import DataExtractor

data_extractor = DataExtractor()
user_data = data_extractor.read_rds_table('legacy_users')

data_cleaner = DataCleaning()
cleaned_user_data = data_cleaner.clean_user_data(user_data)

db_connector = DatabaseConnector()
db_connector.upload_to_db(cleaned_user_data, 'dim_users')

pdf_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
extracted_card_data  = data_extractor.retrieve_pdf_data(pdf_link)
cleaned_card_details = data_cleaner.clean_card_data(extracted_card_data)
db_connector.upload_to_db(cleaned_card_details, 'dim_card_details')