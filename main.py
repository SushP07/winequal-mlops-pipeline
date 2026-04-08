from src.winequal_mlops_pipeline import logger

from src.winequal_mlops_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.winequal_mlops_pipeline.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


logger.info("Welcome to our wine quality mlops pipeline")


STAGE_NAME = "Data Ingestion Stage" 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


