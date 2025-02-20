import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
import dill


## this function is to save the object in the pickle file
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    