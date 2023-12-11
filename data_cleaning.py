import pandas as pd

class DataCleaning:
    def clean_user_data(self, user_data):

        cleaned_data = user_data.dropna()

        return cleaned_data