from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
from data_extraction import DataExtractor

data_extractor = DataExtractor()
data_cleaner = DataCleaning()
db_connector = DatabaseConnector()

user_data = data_extractor.read_rds_table('legacy_users')
cleaned_user_data = data_cleaner.clean_user_data(user_data)
db_connector.upload_to_db(cleaned_user_data, 'dim_users')


pdf_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
extracted_card_data  = data_extractor.retrieve_pdf_data(pdf_link)
cleaned_card_details = data_cleaner.clean_card_data(extracted_card_data)
db_connector.upload_to_db(cleaned_card_details, 'dim_card_details')


number_of_stores = data_extractor.list_number_of_stores()
all_store_data = data_extractor.retrieve_store_data()
cleaned_store_data = data_cleaner.clean_store_data(all_store_data)
db_connector.upload_to_db(cleaned_store_data, 'dim_store_details')


product_data = data_extractor.extract_from_s3('s3://data-handling-public/products.csv')
product_data_weight_converted = data_cleaner.convert_product_weights(product_data)
cleaned_product_data = data_cleaner.clean_products_data(product_data_weight_converted)
db_connector.upload_to_db(cleaned_product_data, 'dim_products')

tables = db_connector.list_db_tables()
print(tables)

order_data = data_extractor.read_rds_table('orders_table')
print(order_data)

cleaned_orders_data = data_cleaner.clean_orders_data(order_data)
db_connector.upload_to_db(cleaned_orders_data, 'order_table')

date_details = data_extractor.extract_json_from_s3('https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')
cleaned_date_details = data_cleaner.clean_dates(date_details)
db_connector.upload_to_db(cleaned_date_details, 'dim_date_times')