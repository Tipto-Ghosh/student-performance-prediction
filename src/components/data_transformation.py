import sys 
import os 
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder , OrdinalEncoder , StandardScaler
from sklearn.impute import SimpleImputer 
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils.common_utils import save_object
from src.config.data_transformation_config import DataTransformationConfig

class DataTransformation:
    def __init__(self):
        self.data_transformation_config_obj = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        # This function will do the data transformation
        try:
            # seperate the numerical and categorical columns 
            numerical_features = ['reading_score' , 'writing_score']
            categorical_features = ['gender', 
                                    'race_ethnicity', 'lunch', 
                                    'parental_level_of_education' , 'test_preparation_course'
                                    ]
            
            logging.info(f"numerical_features: {numerical_features}")
            logging.info(f"categorical_features: {categorical_features}")
            
            # create the preprocessing pipeline 
            numerical_pipeline = Pipeline(steps = [
                # we need to things: 1. Fill the missing values(imputer) and 2.Standard Scaler to centre the values
                ('imputer' , SimpleImputer(strategy = 'mean')), 
                ('scaler' , StandardScaler())
            ])
            
            logging.info("numerical_pipeline executed")
                        
            # create the categorical pipeline (nominal)
            nominal_pipeline = Pipeline(steps = [
                # 1. Imputer , 2.Encoder
                ('imputer' , SimpleImputer(strategy = 'most_frequent')), 
                ('onehot' , OneHotEncoder(handle_unknown = 'ignore' , drop = 'first')), 
                ('scaler' , StandardScaler(with_mean = False))
            ])
            
            logging.info("nominal_pipeline executed")
            
            # make the preprocessor 
            preprocessor = ColumnTransformer(transformers = [
                ('num' , numerical_pipeline , numerical_features), 
                ('nom' , nominal_pipeline , categorical_features), 
            ])
            
            logging.info("preprocessor executed")
            
            return preprocessor
            
        except Exception as ex:
            logging.error("Error occurred in get_data_transformer_object method" , exc_info = True)
            raise CustomException(ex , sys)

    
    def initiate_data_transformation(self , train_data_path , test_data_path): 
        try:
            # read the train and test data
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            
            print("Columns in train_df:", train_df.columns.tolist())
            
            logging.info("Train and test data reading done from initiate_data_transformation")
            
            
            target_column_name = 'math_score'
            numerical_features = ['reading_score' , 'writing_score']
            categorical_features = ['gender', 
                                    'race_ethnicity', 'lunch', 
                                    'parental_level_of_education' , 'test_preparation_course'
                                    ]
            
            
            X_train = train_df.drop(columns = [target_column_name] , axis = 1)
            y_train = train_df[target_column_name]
            logging.info("From Training data input features and target column seperated")
            
            # Also apply the same transformation tecniques on test data
            X_test = test_df.drop(columns = [target_column_name] , axis = 1)
            y_test = test_df[target_column_name]
            logging.info("From Test data input features and target column seperated")
            
            
            # Apply Data Transformation and Preprocessing on train dataset
            preprocessing_obj = self.get_data_transformer_object()
            X_train = preprocessing_obj.fit_transform(X_train)
            X_test = preprocessing_obj.transform(X_test)
            logging.info("Transformation completed on both input train and test features")
            
            # Now as we seperated the input features and target before so now concate them again
            train_arr = np.c_[X_train , np.array(y_train)]
            test_arr = np.c_[X_test , np.array(y_test)]
            
            logging.info("Recombing input features and target column together for train and test data")
            
            # also save the preprocessor object
            save_object( 
               file_path = self.data_transformation_config_obj.preprocessor_object_file_path,
               obj = preprocessing_obj
            )
            logging.info(f"Preprocessor object saved")
            
            # Also return the transformed train and test data and preprocessor object location for model trainer
            return (
                train_arr , test_arr,
                self.data_transformation_config_obj.preprocessor_object_file_path
            )         
        except Exception as e:
            logging.error("Error occurred in initiate_data_transformation method" , exc_info = True)
            raise CustomException(e , sys)
