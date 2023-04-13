import os # os is basically use to create path
import sys # system error
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # it is basicaly used to replace the constructor or __init__ function in class where we don't need any output from init function

## Initialize the data ingestion configuration

# When 
@dataclass
class DataIngestionconfig:
    train_data_path: str = os.path.join('artifact','train.csv')
    test_data_path: str = os.path.join('artifact','test.csv')
    raw_data_path: str = os.path.join('artifact','raw.csv')

#create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
    def initate_data_ingestion(self):
        logging.info('Data Ingestion methods start')
        try:
            df=pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return(
                            self.ingestion_config.train_data_path,
                            self.ingestion_config.test_data_path
                        )
  
        except Exception as e:
            logging.info('Exception occurs at Data Ingestion stage')
            raise CustomerException(e,sys)

## run the Data ingestion
# if __name__=='__main__':
#     obj=DataIngestion()
#     train_data,test_data=obj.initate_data_ingestion()

