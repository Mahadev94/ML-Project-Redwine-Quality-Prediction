from src.mlProject.logging import logger
from mlProject.pipeline.training_pipeline import TrainingPipeline


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

        STAGE_NAME = "Model trainer stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline.start_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e