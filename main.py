import sys 
from src.logger import logging 
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.data_ingestion_config import DataIngestionConfig
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    # try:
    #     a = 12 / 0 
    # except ZeroDivisionError as zd:
    #     logging.exception("Divided by zero")
    #     raise CustomException(zd , sys)
    
    # Do the Data Ingestion part
    try:
        data_ingestion = DataIngestion()
        train_data_path , test_data_path = data_ingestion.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        train_data , test_data , preprocessor_path =  data_transformation.initiate_data_transformation(
            train_data_path = train_data_path,
            test_data_path = test_data_path
        )
        
        print(train_data.shape)
        print(test_data.shape)
        print(preprocessor_path)
        
    except Exception as ex:
        raise CustomException(ex , sys)