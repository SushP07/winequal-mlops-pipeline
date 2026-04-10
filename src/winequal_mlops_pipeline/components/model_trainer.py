import pandas as pd
from src.winequal_mlops_pipeline import logger
from sklearn.linear_model import ElasticNet
import joblib
import os
from src.winequal_mlops_pipeline.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Loading training data")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        logger.info("Splitting data into features and target")
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        logger.info("Initializing the ElasticNet model")
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
    

        logger.info("Training the model")
        lr.fit(train_x, train_y)

        logger.info("Saving the trained model")
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))