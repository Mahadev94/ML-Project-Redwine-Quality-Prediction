import os
from mlProject.logging import logger
from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataTransformationConfig,
                                            ModelTrainerConfig,
                                            ModelEvaluationConfig)

from mlProject.components.data_ingestion import DataIngestion
from mlProject.components.data_validation import DataValidation
from mlProject.components.data_transformation import DataTransformation
from mlProject.components.model_trainer import ModelTrainer
from mlProject.components.model_evaluation import ModelEvaluation


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

    def start_data_transformation(self) -> DataTransformationConfig:
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[3]
                
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("data schema is not valid")
        except Exception as e:
            raise e
        

    def start_model_trainer(self) ->ModelTrainerConfig:
        try:
            config = ConfigurationManager()
            model_trainer_config =config.get_model_trainer_config()
            start_model_trainer =ModelTrainer(config = model_trainer_config)
            start_model_trainer.train_model()
        except Exception as e:
            raise e


    def start_model_evaluation(self) -> ModelEvaluationConfig:
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config =model_evaluation_config)
            model_evaluation.save_evluation()
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

        STAGE_NAME = "Data Transformation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline.start_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = "Model trainer Stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline.start_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = "Model Evaluation Stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline.start_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e