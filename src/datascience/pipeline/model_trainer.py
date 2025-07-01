from src.datascience.config.configuration import configmanager
from src.datascience.components.model_trainer import model_trainer
from src.datascience import logger
from pathlib import Path


STAGE_NAME = 'model trainer stage'

class model_trainer_training_pipeline:

    def __init__(self):
        pass
    

    def initiate_model_trainer(self):

        try:
          config = configmanager() 
          model_trainer_config = config.get_model_trainer()
          model_trainer_obj = model_trainer(config=model_trainer_config) 
          model_trainer_obj.train()



   
  

        except Exception as e:
         raise e      




if __name__ == '__main__':

    try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = model_trainer_training_pipeline()
        obj.initiate_model_trainer()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

    except Exception as e:  
        logger.exception(e)
        raise e  