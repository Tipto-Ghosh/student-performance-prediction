import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np 

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


# save a pkl object as file
def save_object(file_path , obj): 
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path , exist_ok = True)
        
        with open(file_path , "wb") as file:
            pickle.dump(obj , file)
            
    except Exception as e:
        logging.error(f"Error to save object[object File: {file_path}]" , exc_info = True)
        raise CustomException(e , sys)