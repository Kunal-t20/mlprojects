#common inside it that we are using in project 

import os
import sys
import numpy as np
import pandas as pd
import dill # to pick pkl file
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evalute_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for i, (name, model) in enumerate(models.items()):
            model.fit(X_train, y_train)   # Train
            y_pred = model.predict(X_test)  # Predict
            test_model_score = r2_score(y_test, y_pred)  # Evaluate

            report[name] = test_model_score  # ✅ Corrected line

        
        return report
    except Exception as e:
        raise CustomException(e,sys)