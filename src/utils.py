import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql

# load the info of .env file
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("databaseName")
data_table = os.getenv("datatable")

def read_sql_data() -> pd.DataFrame: 
    logging.info("Reading SQL database started")
    
    try:
        # connect with the database
        database_conn = pymysql.connect(host = host , user = user , password = password , database = database)
        logging.info(f"Database connection established with: {database}")
        
        df = pd.read_sql_query(f'select * from {data_table}' , database_conn)
        
        print(df.head())
        
        logging.info("Table read completed")
        return df   
    except Exception as ex:
        raise CustomException(ex , sys)