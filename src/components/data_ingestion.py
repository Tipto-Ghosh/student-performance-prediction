import os 
import sys 

from src.exception import CustomException
from src.logger import logging
from src.config.data_ingestion_config import DataIngestionConfig 
from src.utils.database_utils import read_sql_data
import pandas as pd 
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self): 
        try:
            # 1. Read the data from database
            df = read_sql_data()
            logging.info("DataFrame received in data_ingestion file") 
            
            # 2. Create folder if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok = True)
            
            # 3. Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path , index = False , header = True) 
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")
            
            # 4. Now make the train and test data
            train_dataset , test_dataset = train_test_split(df , test_size = 0.2 , random_state = 42)
            
            # 5. save the train data
            train_dataset.to_csv(self.ingestion_config.train_data_path , index = False , header = True)
            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            
            # 6. save the test data
            test_dataset.to_csv(self.ingestion_config.test_data_path , index = False , header = True)
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")
            
            return (self.ingestion_config.train_data_path , self.ingestion_config.test_data_path)
        
        except Exception as ex:
            logging.error("Error occurred while connecting to database" , exc_info = True)
            raise CustomException(ex , sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()