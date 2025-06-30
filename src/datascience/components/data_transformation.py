import os
import pandas as pd
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import (dataTransformationConfig)

class data_transformation:

    def __init__(self, config: dataTransformationConfig):
        self.config = config


    # def train_test_splitting(self):
    #     data = pd.read_csv(self.config.data_path)

    def train_test_splitting(self):
        try:
            # Load the dataset
            data = pd.read_csv(self.config.data_path)
            logger.info(f"Loaded data from {self.config.data_path} with shape {data.shape}")

            # Train-test split
            train, test = train_test_split(data)

            # Ensure directories exist
            train.to_csv(os.path.join(self.config.root_dir , "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir , "test.csv"), index=False)

            

        

            logger.info(f"Train-test split done. Train shape: {train.shape}, Test shape: {test.shape}")
            return train, test

        except Exception as e:
            logger.exception("Error occurred during train-test split")
            raise e
