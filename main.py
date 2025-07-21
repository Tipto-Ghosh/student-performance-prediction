import sys 
from src.logger import logging 
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.data_ingestion_config import DataIngestionConfig
from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig 
from src.config.model_trainer_config import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.pipelines.prediction_pipeline import CustomData , PredictPipeline

if __name__ == "__main__":
    # try:
    #     a = 12 / 0 
    # except ZeroDivisionError as zd:
    #     logging.exception("Divided by zero")
    #     raise CustomException(zd , sys)
    
    # Do the Data Ingestion part
    try:
        # data_ingestion = DataIngestion()
        # train_data_path , test_data_path = data_ingestion.initiate_data_ingestion()
        
        # data_transformation = DataTransformation()
        # train_data , test_data , preprocessor_path =  data_transformation.initiate_data_transformation(
        #     train_data_path = train_data_path,
        #     test_data_path = test_data_path
        # )
        
        # print(train_data.shape)
        # print(test_data.shape)
        # print(preprocessor_path)
        
        # models = load_models("src/config/models.yaml")
        # params = load_model_params("src/config/params.yaml")
        
        # print(models.keys())
        # print(params["Lasso"])
        
        # Data Ingestion
        # data_ingestion = DataIngestion()
        # train_data_path , test_data_path = data_ingestion.initiate_data_ingestion()
        
        # data_transformation = DataTransformation()
        # train_data , test_data , preprocessor_path =  data_transformation.initiate_data_transformation(
        #     train_data_path = train_data_path,
        #     test_data_path = test_data_path
        # )
        
        # print(type(train_data))
        # print(train_data.shape)
        
        # print(type(test_data))
        # print(test_data.shape)
        
      
        
        
        # model_training = ModelTrainer()
        # r2_pred = model_training.initiate_model_trainer(train_array = train_data , test_array = test_data)
        # print(f"Best model r2 score: {r2_pred}")
        
        
        # Let's predict a single row
        test = CustomData(
           gender = 'female',
           race_ethnicity_group = 'group B',
           parental_level_of_education = 'bachelor',
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