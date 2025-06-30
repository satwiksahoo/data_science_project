from src.datascience import logger
from src.datascience.pipeline.data_ingestion import data_ingestion_training_pipeline
from src.datascience.pipeline.data_validation import data_validation_training_pipeline
from src.datascience.pipeline.data_transformation import data_transformation_training_pipeline


STAGE_NAME = 'data ingestion stage'


try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_ingestion_training_pipeline()
        obj.initiate_data_ingestion()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

except Exception as e:  
        logger.exception(e)
        raise e  





STAGE_NAME = 'data validation stage'


try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_validation_training_pipeline()
        obj.initiate_data_validation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

except Exception as e:  
        logger.exception(e)
        raise e  





STAGE_NAME = 'data transformation stage'


try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = data_transformation_training_pipeline()
        obj.initiate_data_transformation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

except Exception as e:  
        logger.exception(e)
        raise e  

