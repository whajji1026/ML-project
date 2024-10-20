import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    '''This is a configuration class that defines where the data files 
    (raw data, train data, and test data) will be saved.'''

    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        '''The DataIngestion class is responsible for reading the 
    data, splitting it into training and test sets, and saving 
    these sets to their respective locations.'''
        
        self.ingestion_config=DataIngestionConfig()
    

    def initiate_data_ingestion(self):
        logging.info('entered the data ingestion method or component')
        try:
            ## read the date from somewhre(api, internal db, cloud.. )
            df=pd.read_csv('notebook\data\stud.csv')

            logging.info("read the dataset as dataframe")

            ##ensures that the directory ('artifacts/') exists before attempting to save the file (train.csv). 
            # It prevents the code from failing if the directory is missing, creating it automatically if needed.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            ## creating csv files and saving them in artifacts
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('train test split initiated')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('ingestion of the data completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)



if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()