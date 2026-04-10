from src.winequal_mlops_pipeline.config.configuration import ConfifigurationManager
from src.winequal_mlops_pipeline.components.model_evaluation import ModelEvaluation
from src.winequal_mlops_pipeline import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = ConfifigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()