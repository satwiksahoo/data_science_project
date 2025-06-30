from src.datascience.config.configuration import configmanager
from src.datascience.components.data_validation import data_validation
from src.datascience import logger


STAGE_NAME = 'data validation stage'

class data_validation_training_pipeline:

    def __init__(self):
        pass
    

    def initiate_data_validation(self):
         config = configmanager() 
         data_validation_config = config.get_data_validation_config()
         data_validation_obj = data_validation(config=data_validation_config) 
         data_validation_obj.data_validation_all_columns()


if __name__ == '__main__':

    try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_validation_training_pipeline()
        obj.initiate_data_validation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

    except Exception as e:  
        logger.exception(e)
        raise e  


