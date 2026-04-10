import pandas as pd
from src.winequal_mlops_pipeline import logger
from sklearn.linear_model import ElasticNet
import joblib
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
from src.winequal_mlops_pipeline.constants import *
from src.winequal_mlops_pipeline.utils.common import read_yaml, create_directories, save_json
from src.winequal_mlops_pipeline.entity.config_entity import ModelEvaluationConfig



os.environ["MLFLOW_TRACKING_URI"] = "<MLFLOW_TRACKING_URI>"
os.environ["MLFLOW_TRACKING_USERNAME"] = "<MLFLOW_TRACKING_USERNAME>"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "<MLFLOW_TRACKING_PASSWORD>"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            prediction_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, prediction_qualities)

            # Saving metrics as local
            scores = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2 }
            
            save_json(path = Path(self.config.metric_file_name), data = scores)

            # Logging metrics into mlflow

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)

            # Model registry does not work with file store, hence we are using artifact store

            if tracking_url_type_store != "file":

                # Register the model
                # There are some other ways to use the Model Registry, which depends on the use case,
                # For more information please check the official documentation of MLFlow
                # https://www.mlflow.org/docs/latest/model-registry.html#api-workflow

                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet_WineQualityModel")
            else:
                mlflow.sklearn.log_model(model, "model")
