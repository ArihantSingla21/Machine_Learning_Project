import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


# It creates the necessary directories if they do not exist.
# This function saves a given object to a specified file path using dill serialization.
## this function is to save the object in the pickle file
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
    # This function evaluates multiple machine learning models based on their performance
    # on training and testing datasets. It uses GridSearchCV for hyperparameter tuning
    # and returns a report containing the R2 score for each model on the test dataset.
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            gs = GridSearchCV(model,params[list(models.keys())[i]],cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        logging.info("Error in model trainer")
        raise CustomException(e,sys)
        
## this function is to load the object from the pickle file, and furthur more help us in connecting the model to the predict function
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        logging.info("Error in load object")
        raise CustomException(e,sys)