from src.winequal_mlops_pipeline.config.configuration import ConfifigurationManager
from src.winequal_mlops_pipeline.components.data_transformation import DataTransformation
from src.winequal_mlops_pipeline import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
            if status != "True":
                config = ConfifigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Data Schema is not valid")
        except Exception as e:
            logger.exception(e)
            print(e)
            raise e
                   
        