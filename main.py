from src.datascience import logger
from src.datascience.pipeline.data_ingestion import data_ingestion_training_pipeline
from src.datascience.pipeline.data_validation import data_validation_training_pipeline
from src.datascience.pipeline.data_transformation import data_transformation_training_pipeline
from src.datascience.pipeline.model_trainer import model_trainer_training_pipeline
from src.datascience.pipeline.model_evaluation import model_eval_training_pipeline


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





STAGE_NAME = 'model trainer stage'

try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = model_trainer_training_pipeline()
        obj.initiate_model_trainer()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

except Exception as e:  
        logger.exception(e)
        raise e 



STAGE_NAME = 'model evaluation stage'

try:
        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<')  

        obj = model_eval_training_pipeline()
        obj.initiate_model_evaluation()     

        logger.info(f'>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<')  

except Exception as e:  
        logger.exception(e)
        raise e  


