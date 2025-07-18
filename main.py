import sys 
from src.logger import logging 
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.data_ingestion_config import DataIngestionConfig


if __name__ == "__main__":
    # try:
    #     a = 12 / 0 
    # except ZeroDivisionError as zd:
    #     logging.exception("Divided by zero")
    #     raise CustomException(zd , sys)
    
    # Do the Data Ingestion part
    try:
       data_ingestion = DataIngestion()
       data_ingestion.initiate_data_ingestion()
       
    except Exception as ex:
        raise CustomException(ex , sys)