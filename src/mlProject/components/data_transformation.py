#4.update component
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from mlProject.logging import logger
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)
        #load data from config entity

        train,test = train_test_split(data)
        # Split the data into training and test sets. (0.75, 0.25) split.

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        #saved train, test data as csv in data transformation artifacts
        
        logger.info("saved train test data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        



