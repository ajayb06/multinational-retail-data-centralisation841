import pandas as pd
from database_utils import DatabaseConnector

class DataCleaning:
    def __init__(self):
        pass

    def clean_user_data(self, df):
        df = df.dropna()

        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

        df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

        return df
    
    def clean_card_data(self, df):

        df = df.copy()
    # Check if the DataFrame is empty
        if df.empty:
         raise ValueError("The DataFrame is empty")

    # Ensure 'card_number' is of type string
        df['card_number'] = df['card_number'].astype(str)

    # Remove rows where 'card_number' is not a digit
        df = df[df['card_number'].str.isdigit()]

    # Convert 'expiry_date' to datetime format and handle errors
    # Assuming 'expiry_date' is in the format 'mm/yy' initially
        df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce', format='%m/%y')

    # Convert 'expiry_date' back to string in the format 'mm/YYYY'
        df['expiry_date'] = df['expiry_date'].dt.strftime('%m/%Y')

        return df





