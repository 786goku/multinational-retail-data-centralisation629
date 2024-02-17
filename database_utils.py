# database_utils.py
import yaml

import psycopg2

class DatabaseConnector:
    def __init__(self, dbname, user, password, host, port):
        # Initialize the Database Connector with connection details
        pass

    def connect(self):
        # Method to establish a connection to the database
        pass

    def disconnect(self):
        # Method to close the database connection
        pass

    def upload_data(self, data, table_name):
        # Method to upload data to the database
        pass
def read_db_creds(self):
    with open('db_creds.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials
from sqlalchemy import create_engine

def init_db_engine(self):
    creds = self.read_db_creds()
    db_url = f"sqlite:///{creds['DB_FILE']}"
    engine = create_engine(db_url)
    return engine
def list_db_tables(self):
    engine = self.init_db_engine()
    with engine.connect() as connection:
        table_names = connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        return [name[0] for name in table_names]

def upload_to_db(self, df, table_name):
    engine = self.init_db_engine()
    df.to_sql(table_name, engine, index=False, if_exists='replace')
