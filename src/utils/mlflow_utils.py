import mlflow
import mlflow.sklearn

from urllib.parse import urlparse
from src.logger import logging 
import os 
import sys 

class MLFlowLogger:
    def __init__(self , tracking_uri , model_name):
        mlflow.set_registry_uri(tracking_uri)
        self.tracking_type = urlparse(mlflow.get_tracking_uri()).scheme
        self.model_name = model_name
        
    
    
    def log_model(self, model, params, metrics, artifact_path = "artifacts/model"):
        mlflow.set_experiment(self.model_name)
        
        with mlflow.start_run():
            mlflow.log_params(params)
            
            for key, val in metrics.items():
                mlflow.log_metric(key, val)
            
            
            logging.info(f"Logging Model: {type(model)}")
            logging.info(f"artifacts path: {type(artifact_path)}")
            
            if "dagshub" in mlflow.get_tracking_uri():
                os.makedirs(artifact_path, exist_ok=True)
                local_model_path = os.path.join(artifact_path, "model.pkl")
                mlflow.sklearn.save_model(model, local_model_path)
                mlflow.log_artifacts(artifact_path)
            else:
                mlflow.sklearn.log_model(model, artifact_path)

            logging.info("Model logged successfully.")

        