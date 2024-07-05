#4  component
from mlProject.logging import logger
import os
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            logger.info("data load started")
            data=pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            #also get all columns from schema
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"validation status is {validation_status} and this {col} column is not in data ")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"validation status is {validation_status} ")
            return validation_status    
    
        except Exception as e:
            raise e
        
    def validate_column_data_type(self):
        try:
            validation_status = {}
            logger.info("validate each column based on schema started")

            data=pd.read_csv(self.config.unzip_data_dir)
            
            #also get all columns from schema
            all_schema = self.config.all_schema
            for column,expected_type in all_schema.items():
                if column in data.columns:
                    actual_type = data[column].dtype
                    validation_status[column] =str(actual_type)==(expected_type)
                    
                else: 
                    validation_status[column] = False
                    
            with open(self.config.STATUS_FILE, "a") as f:
                f.write(f"column validation as per schema:{validation_status} ")
                        
            return validation_status
            
            
        except Exception as e:
            raise e