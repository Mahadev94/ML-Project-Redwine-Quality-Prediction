import os
from sklearn.linear_model import ElasticNet
from pathlib import Path
import pandas as pd
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)

        #now here we have to get X_train, y_train and X_test,y_test
        X_train = train.drop([self.config.target_column],axis=1)
        X_test = test.drop([self.config.target_column],axis=1)

        y_train = train[[self.config.target_column]]
        y_test = test[[self.config.target_column]]

        model =ElasticNet(l1_ratio=self.config.l1_ratio, alpha=self.config.alpha,random_state=42)
        model.fit(X_train,y_train)

        #saving model as pkl file with joblib lib
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
