import sys , os
from src.logger import logging 
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.data_ingestion_config import DataIngestionConfig
from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig 
from src.config.model_trainer_config import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.pipelines.prediction_pipeline import CustomData , PredictPipeline
from src.utils.common_utils import load_object


if __name__ == "__main__":
    
    try:
        # Do the data ingestion
        # data_ingest = DataIngestion()
        # train_data_path , test_data_path = data_ingest.initiate_data_ingestion()
        
        # logging.info("-----------Data Ingestion Completed-----------")
        # logging.info(f"train_data_path type: {type(train_data_path)}")
        # logging.info(F"test_data_path type: {type(test_data_path)}")
        # logging.info("----------------------------------------------------")
        
        # # Do the data transformation
        # logging.info("Data Transformation started")
        # data_transform = DataTransformation()
        # train_data , test_data , preprocessor_path = data_transform.initiate_data_transformation(
        #     train_data_path = train_data_path,
        #     test_data_path = test_data_path
        # )
        # logging.info(f"Data Transformation done. [Train shape: {train_data.shape}] , test shape: {test_data.shape}")
        
        # # Do the model training
        # model_trainer = ModelTrainer()
        # test_r2 = model_trainer.initiate_model_trainer(train_array = train_data , test_array = test_data)
        # logging.info(f"Best Models R2 score: {test_r2}")
        # print(f"Best Models R2 score: {test_r2}")
        
        model = load_object("artifacts/model.pkl")
        print(type(model))
        
        
        
        
        # Let's predict a single row
        test = CustomData(
           gender = 'female',
           race_ethnicity_group = 'group B',
           parental_level_of_education = 'some high school',
           lunch = 'standard',
           test_preparation_course = 'none',
           reading_score = 72,
           writing_score = 72
        )
        
        test_df = test.get_data_as_data_frame()
        
        pred_pipe = PredictPipeline()
        result = pred_pipe.predict(test_df)
        print(result)
        
    except Exception as ex:
        raise CustomException(ex , sys)