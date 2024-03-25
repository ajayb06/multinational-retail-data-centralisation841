import pandas as pd
from database_utils import DatabaseConnector

class DataCleaning:
    def __init__(self):
        pass

    def clean_user_data(self, df):

        df = df.copy()

        df = df.dropna()

        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

        df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

        return df
    
    def clean_card_data(self, df):

        df = df.copy()

        if df.empty:
         raise ValueError("The DataFrame is empty")

        df['card_number'] = df['card_number'].astype(str)

        df = df[df['card_number'].str.isdigit()]

    
        df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce', format='%m/%y')

        df['expiry_date'] = df['expiry_date'].dt.strftime('%m/%Y')

        return df

    def clean_store_data(self, df):
       
        df = df.copy()

        df.dropna(subset=['store_type', 'continent'], inplace=True)

        df['continent'] = df['continent'].replace({'eeEurope':'Europe'})

        df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce', format='%Y-%m-%d')

        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'], errors='coerce')

        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')

        df.dropna(subset=['longitude', 'latitude', 'staff_numbers'], inplace=True)

        df.reset_index(drop=True, inplace=True)

        return df
    
    def convert_product_weights(self, df):

        df = df.copy()

        conversion_rates = {
            'g': 0.001,
            'kg': 1,
            'ml': 0.001,
            'l': 1,
            'oz': 0.0283495  
        }

    
        def convert_weight(weight):
            
            weight_str = str(weight).lower().strip().replace(' ', '') 

            num_str = ''
            unit = ''

            for char in weight_str:
                if char.isdigit() or char == '.':
                    num_str += char
                else:
                    unit += char  

        
            if num_str and unit:
                try:
                    num = float(num_str)
                    return num * conversion_rates.get(unit, 0)
                except ValueError:
                    return 'NaN' 
                
        df['weight'] = df['weight'].apply(convert_weight)

        return df
      
    def clean_products_data(self, df):

        df = df.copy()

        df.dropna(inplace=True)  

        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', format='%Y-%m-%d')

        columns_to_check = ['weight', 'date_added']

        df = df.dropna(subset=columns_to_check)

        for column in columns_to_check:
            df = df[df[column] != 0]

        return df
    
    def clean_orders_data(self, df):

        df = df.copy()

        df.drop(columns=['first_name', 'last_name', '1'], errors='ignore',inplace=True)

        return df
    
    def clean_dates(self, df):

        df = df.copy()

        df['timestamp'].fillna('default_time', inplace=True) 

        df['timestamp'] = df['timestamp'].fillna(pd.to_datetime('00:00:00').time())  

        return df