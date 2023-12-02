import psycopg2

class DatabaseConnector:
    def __inni__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect_to_database(self):
        '''
        Connects to PostgresSQL database

        :return: None
        '''

    def disconnect_from_database(self):
         '''
        Disconnects from PostgresSQL database

        :return: None
        '''
    def execute_query(self, query):
         """
        Executes a SQL query

        :param query: SQL query to be executed.
        :return: None
        """