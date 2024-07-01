import os
from mlProject.logging import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig
from mlProject.components.data_ingestion import DataIngestion
from mlProject.components.data_validation import DataValidation


class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self) -> DataIngestionConfig:
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e
        
    def start_data_validation(self) -> DataValidationConfig:
        try:
            config  = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config =data_validation_config)
            data_validation.validate_all_columns()
            data_validation.validate_column_data_type()
            
        except Exception as e:
            raise e

        
if __name__ == '__main__':
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline = TrainingPipeline()
        training_pipeline.start_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = "Data Validation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline.start_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e