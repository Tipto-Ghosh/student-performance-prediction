import os , sys , yaml
from dataclasses import dataclass
from sklearn.metrics import r2_score , mean_squared_error
from sklearn.model_selection import GridSearchCV
from src.logger import logging
from src.exception import CustomException
from src.config.model_trainer_config import ModelTrainerConfig 
from src.utils.common_utils import load_models , load_model_params
from src.utils.common_utils import evaluate_models , save_object

class ModelTrainer:
    def __init__(self):
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
            
            summary_path = os.path.join("artifacts", "best_model_summary.yaml")
            os.makedirs(os.path.dirname(summary_path), exist_ok=True)

            with open(summary_path, "w") as f:
                yaml.dump(best_model_summary, f)

            logging.info(f"Best model summary saved to {summary_path}")
            
            # Save the trained model object
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=final_best_model
            )
            logging.info(f"Best model object saved to {self.model_trainer_config.trained_model_file_path}")
            
            # Final R2 score on test set
            y_pred = final_best_model.predict(X_test)
            r2_pred = r2_score(y_test, y_pred)
            
            return r2_pred

        except Exception as e:
            logging.error("Error occured in initiate_model_trainer." , exc_info = True)
            raise CustomException(e , sys) 