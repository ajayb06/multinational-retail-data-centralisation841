from sqlalchemy import create_engine, MetaData, Table

# Replace these values with your actual credentials and connection details
db_credentials = {
    "RDS_HOST": "data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com",
    "RDS_USER": "aicore_admin",
    "RDS_PASSWORD": "AiCore2022",
    "RDS_DATABASE": "postgres",
    "RDS_PORT": 5432,
}

# Create a connection URL
db_url = f"postgresql+psycopg2://{db_credentials['RDS_USER']}:{db_credentials['RDS_PASSWORD']}@{db_credentials['RDS_HOST']}:{db_credentials['RDS_PORT']}/{db_credentials['RDS_DATABASE']}"

# Create an SQLAlchemy engine
engine = create_engine(db_url)

# Create a MetaData object
metadata = MetaData()

# Reflect all tables in the database
metadata.reflect(bind=engine)

# Create a connection
with engine.connect() as connection:
    # Iterate over all tables
    for table_name, table_obj in metadata.tables.items():
        print(f"\nTable: {table_name}")
        
        # Select all rows from the table
        query = table_obj.select()
        
        # Execute the query
        result = connection.execute(query)

        # Fetch all rows
        rows = result.fetchall()

        # Print or process the rows
        for row in rows:
            print(row)
