import os
import pandas as pd
from src.datascience import logger
from sklearn.metrics import mean_squared_error , mean_absolute_error , r2_score
from urllib.parse import urlparse
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import ElasticNet
import json
from src.datascience.utils.common import save_json
from src.datascience.entity.config_entity import ( modelevaluationconfig)
from pathlib import Path

import tempfile


os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/satwiksahoojob/data_science_project.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'satwiksahoojob'

os.environ['MLFLOW_TRACKING_PASSWORD'] =  '46df081cd1c771ae5c58838602b17d7d7c7de746'

mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])

class model_evaluation:

    def __init__(self, config: modelevaluationconfig):
        self.config = config

    def evaluation_metric(self, actual, pred):

        rmse = np.sqrt(mean_squared_error(actual , pred))
        mae = mean_absolute_error(actual , pred)
        r2  = r2_score(actual , pred)

        return rmse , mae , r2
    

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x  =test_data.drop([self.config.target_column] ,axis=1)
        test_y  =test_data[self.config.target_column]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme 


        with mlflow.start_run():  # 🟢 Start MLflow run

    # Initialize and train model
        #  model = ElasticNet(alpha=self.params.alpha, l1_ratio=self.params.l1_ratio, random_state=42)
        #  model.fit(X_train, y_train)

    # Predict and evaluate
         preds = model.predict(test_x)
        #  mse = mean_squared_error(test_y, preds)
        #  r2 = r2_score(test_y, preds)
         (rmse , mae , r2) = self.evaluation_metric(test_y , preds )

         scores = { 'rmse':rmse ,'mae': mae ,'r2' : r2}
         save_json(path = Path(self.config.metric_file_name), data = scores)
    # Log parameters, metrics, and model
         mlflow.log_param('all params',self.config.all_params)
         mlflow.log_metric("mae", mae)
         mlflow.log_metric("r2", r2)
         mlflow.log_metric("rmse", rmse)

         if tracking_uri_type_store != 'file':
            # mlflow.sklearn.log_model(model, "model" , registered_model_name='ElasticNet model')
            # mlflow.sklearn.log_model(model, "model")

                 

           with tempfile.TemporaryDirectory() as tmp_dir:
             model_path = os.path.join(tmp_dir, "model.joblib")
             joblib.dump(model, model_path)
             mlflow.log_artifact(model_path, artifact_path="model")
            

         else:    
           print("Run logged in MLflow.")


