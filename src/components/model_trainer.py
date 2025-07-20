import os
import sys
import yaml
import mlflow
import numpy as np
from urllib.parse import urlparse
from dataclasses import dataclass
from sklearn.metrics import r2_score , mean_squared_error , mean_absolute_error
from sklearn.model_selection import GridSearchCV
from src.logger import logging
from src.exception import CustomException
from src.config.model_trainer_config import ModelTrainerConfig 
from src.utils.common_utils import load_models , load_model_params
from src.utils.common_utils import evaluate_models , save_object , read_best_model_info
from dotenv import load_dotenv 
from src.utils.mlflow_utils import MLFlowLogger




class ModelTrainer:
    def __init__(self):
        load_dotenv()
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self , train_array , test_array): 
        try:
            logging.info("Split the train and test input data")
            
            X_train , y_train = train_array[ : , : -1] , train_array[ : , -1]
            X_test  , y_test  = test_array[ : , : -1] , test_array[ : , -1]
            
            
            # Get the models which we want to train
            MODELS_PATH = "src/config/models.yaml"
            PARAMS_PATH = "src/config/params.yaml"
            
            # Load models and hyperparameters
            models = load_models(MODELS_PATH)
            params = load_model_params(PARAMS_PATH)
            logging.info("Models and Parameters loaded successfully. Ready to start training")
            
            # Evaluate all models
            model_report: dict = evaluate_models(X_train, X_test, y_train, y_test, models, params)
            logging.info("Model evaluation completed.")
            
            # Select best model
            best_model_name = max(model_report, key = lambda x: model_report[x]['test_r2'])
            best_model_info = model_report[best_model_name]
            
            # If no best model found
            if best_model_info['test_r2'] < 0.6:
                logging.error("No model achieved r2_score greater than 60%", exc_info = True)
                raise CustomException("No Best Model Found")
            
            # Now re-train best model using GridSearchCV
            logging.info(f"Training best model: {best_model_name} again with GridSearchCV")
            
            model = models[best_model_name]
            param_grid = params.get(best_model_name, {})
            
            if not param_grid:
                logging.warning(f"No param grid found for {best_model_name}. Using default model.")
                model.fit(X_train, y_train)
                final_best_model = model
                best_params = {}
            else:
                gs = GridSearchCV(model, param_grid, cv = 3)
                gs.fit(X_train, y_train)
                
                final_best_model = gs.best_estimator_
                best_params = gs.best_params_
            
            # Save best model summary
            best_model_summary = {
                "best_model_name": best_model_name,
                "best_model_params": best_params,
                "train_r2": r2_score(y_train, final_best_model.predict(X_train)),
                "test_r2": r2_score(y_test, final_best_model.predict(X_test))
            }
            
            ARTIFACTS_DIR = "artifacts"
            os.makedirs(ARTIFACTS_DIR , exist_ok = True)
            SUMMARY_PATH = os.path.join(ARTIFACTS_DIR , "best_model_summary.yaml")
            os.makedirs(os.path.dirname(SUMMARY_PATH), exist_ok=True)

            with open(SUMMARY_PATH, "w") as f:
                yaml.dump(best_model_summary, f)

            logging.info(f"Best model summary saved to {SUMMARY_PATH}")
            
            # Save the trained model object
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = final_best_model
            )
            logging.info(f"Best model object saved to {self.model_trainer_config.trained_model_file_path}")
            
            # Final R2 score on test set
            y_pred = final_best_model.predict(X_test)
            test_r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test , y_pred)
            rmse = np.sqrt(mean_squared_error(y_test , y_pred))
            # Do the MLOPs codes
            
            
            
            tracking_url = os.getenv("dagshub_url")
            username = os.getenv("dagshub_username")
            token = os.getenv("dagshub_token")
            
            logging.info("Environment variables loaded from .env")
            
            if not tracking_url or not username or not token:
                raise CustomException("Missing MLflow tracking credentials in .env")
            
            # Set MLflow tracking URI and credentials
            os.environ["MLFLOW_TRACKING_USERNAME"] = username
            os.environ["MLFLOW_TRACKING_PASSWORD"] = token
            mlflow.set_tracking_uri(tracking_url)
            
            mlflow_logger = MLFlowLogger(tracking_uri = tracking_url , model_name = best_model_name)
            
            metrics = {
                "R2 Score" : float(test_r2),
                "MAE" : float(mae),
                "RMSE" : float(rmse)
            }
            mlflow_logger.log_model(final_best_model , best_params , metrics)
            
            METRICES_PATH = os.path.join(ARTIFACTS_DIR , "metrics.yaml")
            os.makedirs(os.path.dirname(METRICES_PATH), exist_ok = True)
            
            with open(METRICES_PATH, "w") as f:
                yaml.dump(metrics, f)
            
            logging.info(f"Model metrics saved to {METRICES_PATH}")
            logging.info(f"Final Model Evaluation -> R2: {test_r2}, MAE: {mae}, RMSE: {rmse}")

            return test_r2

        except Exception as e:
            logging.error("Error occured in initiate_model_trainer." , exc_info = True)
            raise CustomException(e , sys) 