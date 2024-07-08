from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import numpy as np
import pandas as pd
import joblib
from mlProject.utils.common import save_json
from pathlib import Path
from mlProject.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
    
    def evaluation_metrics(self,actual,predict):
        r2=r2_score(actual,predict)
        mse= mean_squared_error(actual,predict)
        rmse =np.sqrt(mse)
        mae=mean_absolute_error(actual,predict)
        return r2,rmse,mae

    def save_evluation(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test =test_data.drop([self.config.target_column],axis=1)
        y_test = test_data[[self.config.target_column]]

        prediction = model.predict(X_test)

        (r2,rmse,mae) = self.evaluation_metrics(y_test,prediction)

        #saving to local
        scores = {"r2 score": r2, "rmse score": rmse, "mae score": mae}
        save_json(path = Path(self.config.metrics_file_name), data=scores)




    

