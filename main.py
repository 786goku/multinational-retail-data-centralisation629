# main.py

from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

def main():
    # Step 0: Create instances of your classes
    db_connector = DatabaseConnector(dbname='postgres', user='aicore_admin', password='AiCore2022', host='data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com', port='5432')
    data_extractor = DataExtractor()
    data_cleaning = DataCleaning()

    # Step 1: Get data from PDF
    pdf_data = data_extractor.retrieve_pdf_data('your_pdf_link')

    # Step 2: Clean the data
    cleaned_data = data_cleaning.clean_card_data(pdf_data)

    # Step 3: Upload to the database
    db_connector.upload_to_db(cleaned_data, 'dim_card_details')

if __name__ == "__main__":
    main()

    main()
    # Assuming you have instances of your classes
data_extractor = DataExtractor()
data_cleaner = DataCleaning()
db_handler = DatabaseHandler()

# Step 2
number_of_stores = data_extractor.list_number_of_stores("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"})

# Step 3
store_data = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}", {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"})

# Step 4
cleaned_data = data_cleaner.clean_store_data(store_data)

# Step 5
db_handler.upload_to_db(cleaned_data, "dim_store_details")
# Assuming you have a class called DataExtractor and boto3 is installed
import pandas as pd
import boto3
from io import StringIO

class DataExtractor:
    def extract_from_s3(self, s3_address):
        # Assuming you are logged into AWS CLI
        s3 = boto3.client('s3')
        
        # Download and extract information from S3
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        content = response['Body'].read().decode('utf-8')

        # Convert CSV content to pandas DataFrame
        df = pd.read_csv(StringIO(content))

        return df
# Assuming you have instances of your classes
data_extractor = DataExtractor()
data_cleaner = DataCleaning()
db_handler = DatabaseHandler(
    database_url="data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com",
    username="aicore_admin",
    password="AiCore2022"
)

# Step 1
products_data = data_extractor.extract_from_s3('s3://data-handling-public/products.csv')

# Step 2
converted_products_data = data_cleaner.convert_product_weights(products_data)

# Step 3
cleaned_products_data = data_cleaner.clean_products_data(converted_products_data)

# Step 4
db_handler.upload_to_db(cleaned_products_data, "dim_products")
# Assuming you have a class called DatabaseHandler with a method list_db_tables
class DatabaseHandler:
    def list_db_tables(self):
        # Your code here to list all the tables in the database
        pass
# Assuming you have a class called DatabaseHandler with a method read_rds_table
class DatabaseHandler:
    def read_rds_table(self, table_name):
        # Your code here to read the data from the specified table and return a pandas DataFrame
        pass
# Assuming you have a class called DatabaseHandler with a method upload_to_db
class DatabaseHandler:
    def upload_to_db(self, dataframe, table_name):
        # Your code here to upload the DataFrame to the specified table in the database
        pass
# Assuming you have instances of your classes
db_handler = DatabaseHandler()
data_cleaner = DataCleaning()

# Step 1
all_tables = db_handler.list_db_tables()
orders_table_name = "identify_the_orders_table_name"  # Replace with the actual orders table name

# Step 2
orders_data = db_handler.read_rds_table(orders_table_name)

# Step 3
cleaned_orders_data = data_cleaner.clean_orders_data(orders_data)

# Step 4
db_handler.upload_to_db(cleaned_orders_data, "orders_table")

# Assuming you have a class called DataExtractor and boto3 is installed
import pandas as pd
import boto3
from io import StringIO

class DataExtractor:
    def extract_from_s3_json(self, s3_json_address):
        # Assuming you are logged into AWS CLI
        s3 = boto3.client('s3')

        # Download and extract information from S3
        response = s3.get_object(Bucket='data-handling-public', Key='date_details.json')
        content = response['Body'].read().decode('utf-8')

        # Convert JSON content to pandas DataFrame
        df = pd.read_json(StringIO(content))

        return df
# Assuming you have a class called DataCleaning
class DataCleaning:
    def clean_date_times_data(self, date_times_data):
        # Your code here to perform any necessary cleaning on the date_times_data DataFrame
        # This might involve handling missing values, duplicates, etc.
        return date_times_data
# Assuming you have a class called DatabaseHandler
class DatabaseHandler:
    def upload_to_db(self, dataframe, table_name):
        # Your code here to upload the DataFrame to the specified table in the database
        pass
# Assuming you have instances of your classes
data_extractor = DataExtractor()
data_cleaner = DataCleaning()
db_handler = DatabaseHandler(
    database_url="data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com",
    username="aicore_admin",
    password="AiCore2022"
)

# Step 1
date_times_data = data_extractor.extract_from_s3_json('https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')

# Step 2
cleaned_date_times_data = data_cleaner.clean_date_times_data(date_times_data)

# Step 3
db_handler.upload_to_db(cleaned_date_times_data, "dim_date_times")
