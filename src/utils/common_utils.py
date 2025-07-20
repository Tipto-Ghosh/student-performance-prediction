import os 
import sys 
import pickle
import time
import yaml
import importlib , numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score , mean_absolute_error , mean_squared_error
from src.logger import logging
from src.exception import CustomException


def load_yaml(path : str) -> dict:
    """
    Loads a YAML file and returns its contents as a dictionary.
    """
    with open(path, "r") as file:
        return yaml.safe_load(file)


def load_models(model_config_path: str) -> dict:
    """
    Loads model class instances from YAML config.
    Returns a dictionary {model_name: model_instance}
    """
    
    config = load_yaml(model_config_path)
    models = {}
    for name, import_path in config.items():
        module_path, class_name = import_path.rsplit(".", 1)
        cls = getattr(importlib.import_module(module_path), class_name)
        if "catboost" in import_path.lower():
            models[name] = cls(verbose = False)  
        else:
            models[name] = cls()
    return models

def load_model_params(params_path: str) -> dict:
    """
    Loads model parameters grid from YAML.
    Returns a dictionary {model_name: param_dict}
    """
    return load_yaml(params_path)



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
    

# Make a function which will evaluate a model and make a model performance report
def evaluate_models(X_train, X_test, y_train, y_test, models, params):
    try:
        logging.info("Models Train Phase Started")
        report = {}

        for model_name, model in models.items():
            start = time.time()
            print(f"Training {model_name}...")
            
            param_grid = params.get(model_name, {})

            gs = GridSearchCV(model, param_grid, cv = 3 , n_jobs = -1 , verbose = 1)
            gs.fit(X_train, y_train)
            
            end = time.time()
            print(f"Finished {model_name} in {end - start:.2f} seconds")
            
            best_model = gs.best_estimator_
            best_params = gs.best_params_

            best_model.fit(X_train, y_train)

            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            r2_train = r2_score(y_train, y_train_pred)
            r2_test = r2_score(y_test, y_test_pred)
            
            print(f"r2_train : {r2_train} || r2_test: {r2_test}")
            print(" = " * 30)
            
            report[model_name] = {
                "best_params": best_params,
                "train_r2": r2_train,
                "test_r2": r2_test
            }

        # Handle dynamic path for saving the report
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))
        report_path = os.path.join(ROOT_DIR, "artifacts", "model_report.yaml")
        os.makedirs(os.path.dirname(report_path), exist_ok = True)

        with open(report_path, "w") as f:
            yaml.dump(report, f)

        logging.info(f"Model training complete. Report saved to {report_path}")
        return report

    except Exception as e:
        logging.error("Error Occurred in [evaluate_models] during training", exc_info=True)
        raise CustomException(e, sys)

def read_best_model_info(file_path):
    """
    Reads a YAML file and returns the best model name, parameters, and scores.

    Parameters:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Dictionary with model name, parameters, and R2 scores.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    result = {
        "best_model_name": data.get("best_model_name"),
        "best_model_params": data.get("best_model_params", {}),
        "train_r2": data.get("train_r2"),
        "test_r2": data.get("test_r2")
    }

    return result

def get_regression_metrices(y_true , y_pred):
    r2 = r2_score(y_true , y_pred)
    mae = mean_absolute_error(y_true , y_pred)
    rmse = np.sqrt(mean_squared_error(y_true , y_pred))
    
    return r2 , mae , rmse