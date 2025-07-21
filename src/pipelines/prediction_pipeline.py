import os 
import sys 
import pickle
from flask import Flask , request , render_template
import numpy as np 
import pandas as pd 
import mlflow.sklearn
from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
from src.utils.common_utils import load_object
from src.logger import logging


MODEL_PATH = "artifacts/model.pkl"
PREPROCESSOR_PATH = "artifacts/preprocessor.pkl"

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self , features):
        
        try:
            preprocessor = load_object(PREPROCESSOR_PATH)
            model = load_object(MODEL_PATH)
            
            logging.info("preprocessor + model is loaded")
            
            # Do preprocessing of input data
            processed_data = preprocessor.transform(features)
            
            # do the prediction
            pred_result = model.predict(processed_data)
            
            logging.info("prediction is done")
            
            return pred_result
        
        except Exception as e:
            logging.error("Error while doing the prediction")
            raise CustomException(e , sys)

class CustomData:
    def __init__(
       self , gender: str , race_ethnicity_group: str, 
       parental_level_of_education: str , lunch: str,
       test_preparation_course: str,
       reading_score: int, writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity_group = race_ethnicity_group
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity_group],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            
            logging.info("Input data converted to DataFrame successfully")

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)