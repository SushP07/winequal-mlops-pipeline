from src.winequal_mlops_pipeline.config.configuration import ConfifigurationManager
from src.winequal_mlops_pipeline.components.model_trainer import ModelTrainer
from src.winequal_mlops_pipeline import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfifigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()