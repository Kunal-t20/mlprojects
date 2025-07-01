#common inside it that we are using in project 

import os
import sys
import numpy as np
import pandas as pd
import dill # to pick pkl file
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evalute_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}

        for name, model in models.items():
            model_param_grid = param.get(name, {})  # get hyperparams for this model

            if model_param_grid:
                gs = GridSearchCV(model, model_param_grid, cv=3, n_jobs=-1, verbose=1, refit=True)
                gs.fit(X_train, y_train)

                best_model = gs.best_estimator_
            else:
                model.fit(X_train, y_train)
                best_model = model

            y_pred = best_model.predict(X_test)
            test_model_score = r2_score(y_test, y_pred)
            report[name] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)