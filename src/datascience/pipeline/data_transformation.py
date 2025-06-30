from src.datascience.config.configuration import configmanager
from src.datascience.components.data_transformation import data_transformation
from src.datascience import logger
from pathlib import Path


STAGE_NAME = 'data transformation stage'

class data_transformation_training_pipeline:

    def __init__(self):
        pass
    

    def initiate_data_transformation(self):

        try:
          with  open(Path('artifacts/unzip_data_validation/status.txt') , 'r') as f:
             status = f.read().split(" ")[-1].strip()

             if status == "True":
                 
              config = configmanager() 
              data_transformation_config = config.get_data_transformation_config()
              data_transformation_obj = data_transformation(config=data_transformation_config) 
              data_transformation_obj.train_test_splitting()
           
        except Exception as e:  
         logger.exception(e)
         raise e     




if __name__ == '__main__':

    try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_transformation_training_pipeline()
        obj.initiate_data_transformation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

    except Exception as e:  
        logger.exception(e)
        raise e  