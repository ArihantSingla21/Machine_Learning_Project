import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from src.utils import save_object
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from src.utils import evaluate_models


@dataclass()
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig() 

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "SVR": SVR(),
                "K-Neighbors Regressor": KNeighborsRegressor()
            }

            params ={
                "Decision Tree":{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },
                "Random Forest":{
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    'learning_rate':[.1,.01,.05,.001],
                    "subsample":[0.6,0.7,0.8,0.9,1.0],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{
                },
                "SVR":{
                    'kernel':['linear','rbf','sigmoid','poly'],
                    'gamma':['auto','scale']
                },
                "K-Neighbors Regressor":{
                    'n_neighbors': [3,5,7,9,11],
                    'weights':['uniform','distance'],
                    'algorithm':['auto','ball_tree','kd_tree','brute']
                }
            }

            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models,params)
            print(model_report)
            print("\n====================================================")
            logging.info(f"Model Report : {model_report}")

            # To get best model score from dict 
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info(f"Best found model on training and testing dataset {best_model_name} with r2 score {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            
            score = r2_score(y_test,predicted)
            return score 
            
        except Exception as e:
            logging.info("Error in model trainer")
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = ModelTrainer()
    obj.initiate_model_trainer()