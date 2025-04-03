import pandas as pd
import pathlib
import sys
import sql_commands
import MySQLdb
from sqlalchemy import create_engine

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
PREPARED_DATA_DIR = DATA_DIR.joinpath("prepared")

#database connection engine
engine = create_engine("mysql+mysqldb://root:1234@localhost/Smart_Store", echo=True, future=True)

def create_schema(cursor):
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute(sql_commands.Create_customer_table_mysql)
    cursor.execute(sql_commands.Create_products_table_mysql)
    cursor.execute(sql_commands.Create_sale_table_mysql)

def delete_existing_records(cursor):
    """Delete all existing records from the customer, product, and sale tables."""
    cursor.execute("DELETE FROM customer;")
    cursor.execute("DELETE FROM product;")
    cursor.execute("DELETE FROM sale;")

def insert_customers(customers_df: pd.DataFrame):
    """Insert customer data into the customer table."""
    customers_df.to_sql(name="customer", con=engine, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame):
    """Insert product data into the product table."""
    products_df.to_sql(name="product", con=engine, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame):
    """Insert sales data into the sales table."""
    sales_df.to_sql(name="sale", con=engine, if_exists="append", index=False)

def load_data_to_db():
    try:

        #Connect to MYSQL installed locally
        conn= MySQLdb.connect(host='localhost', user='root',password='1234', database='Smart_Store')
        cursor=conn.cursor()
        #cursor.execute('CREATE DATABASE IF NOT EXISTS Smart_Store3;')
        #cursor.execute('USE Smart_Store3;')

     

        # Create schema and clear existing records
        create_schema(cursor)
        #delete_existing_records(cursor)


        #this is a test script to write into the table.  the dataframes should be loaded using sqlalchemy.
        #cursor.execute("INSERT INTO product VALUES (444,'laptop','Electronics',73.12,102,'Computers')")

        # Load prepared data using pandas
        customers_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("customers_data_prepared.csv"))
        products_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("products_data_prepared.csv"))
        sales_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("sales_data_prepared copy.csv"))
        #print(customers_df)

        # Insert data into the database
        
        insert_customers(customers_df)
        insert_products(products_df)
        insert_sales(sales_df)
        

        
        #this is to read from the database

        #cursor.execute("Select * from sale;")
        #myresult = cursor.fetchall()
        #for x in myresult:
         #   print(x)

        

        conn.commit()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()