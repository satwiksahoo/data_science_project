from src.datascience.config.configuration import configmanager
from src.datascience.components.model_evaluation import model_evaluation
from src.datascience import logger
from pathlib import Path


STAGE_NAME = 'model evaluation stage'

class model_eval_training_pipeline:

    def __init__(self):
        pass
    

    def initiate_model_evaluation(self):

        try:
          config = configmanager() 
          model_eval_config = config.get_model_evaluation_config()
          model_eval_obj = model_evaluation(config=model_eval_config) 
          model_eval_obj.log_into_mlflow()
           



   
  

        except Exception as e:
         raise e      




if __name__ == '__main__':

    try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = model_eval_training_pipeline()
        obj.initiate_model_evaluation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

    except Exception as e:  
        logger.exception(e)
        raise e  