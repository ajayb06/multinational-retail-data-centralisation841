# Example Usage to List All Tables

from database_utils import DatabaseConnector

# Initialize the DatabaseConnector
db_connector = DatabaseConnector()

# Get a list of table names
table_names = db_connector.list_db_tables()

# Print the table names
print("Tables in the database:")
for table_name in table_names:
    print(table_name)
