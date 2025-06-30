from src.datascience.config.configuration import configmanager
from src.datascience.components.data_ingestion import data_ingestion
from src.datascience import logger

STAGE_NAME = 'data ingestion stage'

class data_ingestion_training_pipeline:

    def __init__(self):
        pass
    

    def initiate_data_ingestion(self):
         config = configmanager() 
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion_obj = data_ingestion(config=data_ingestion_config) 
         data_ingestion_obj.download_file()
         data_ingestion_obj.extract_zip_file()


if __name__ == '__main__':

    try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_ingestion_training_pipeline()
        obj.initiate_data_ingestion()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

    except Exception as e:  
        logger.exception(e)
        raise e  


