#required to take data from varies sourec data may be big data,mongo data


import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformationConfig,DataTransformation
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer



@dataclass #decorator
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')  #ingestion data or train data save in this path
    test_data_path: str=os.path.join('artifacts','test.csv')  #similarly test data save in this path 
    raw_data_path: str=os.path.join('artifacts','raw.csv')   #to save raw data

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    #to read or input data 
    def initiate_data_ingestion(self):     
        logging.info("enter the data ingestion method or component")
        try:
            df=pd.read_csv(r'notebook\data\stud.csv')   #we have just changed this coode we can use similar for another way like database(mongo,sql) or api and all
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #os.path.dirname() gets the folder name from that path.
            #os.makedirs() creates that folder if it doesn’t already exist
            #exist_ok=True avoids error if folder already exists.

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train_test_split initiated")

            train_set,test_set=train_test_split(df,test_size=.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    preprocessor_path = data_transformation.data_transformation_config.preprocessor_obj_file_path

    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data, preprocessor_path
    )

    model_trainer = ModelTrainer()
    r2_score = model_trainer.initiate_model(
        train_array=train_arr,
        test_array=test_arr
    )

    print(f"\n✅ Model training completed with R² Score: {r2_score}")
