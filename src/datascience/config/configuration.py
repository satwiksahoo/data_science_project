from src.datascience.constants import *
from src.datascience.utils.common import read_yaml , create_directories
from src.datascience.entity.config_entity import (data_ingestion_config , DataValidationConfig , dataTransformationConfig , modeltrainerconfig , modelevaluationconfig)
class configmanager:
    def __init__(self, config_filepath = config_file_path , params_filepath = param_file_path , schema_filepath = schema_file_path):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> data_ingestion_config:
        config = self.config.data_ingestion
        create_directories([config.root_dir])    


        dataingestion_config = data_ingestion_config(

            root_dir  = config.root_dir,
            source_url = config.source_url ,
            local_data_file = config.local_data_file ,
            unzip_dir = config.unzip_dir

        )

        return dataingestion_config
    


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema  = self.schema.COLUMNS
        create_directories([config.root_dir])    


        datavalidation_config = DataValidationConfig(

            root_dir  = config.root_dir,
            STATUS_FILE = config.STATUS_FILE ,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema

        )

        return datavalidation_config
    

    


    def get_data_transformation_config(self) -> dataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])    


        datatransformation_config = dataTransformationConfig(

            root_dir  = config.root_dir,
            data_path= config.data_path

        )

        return datatransformation_config   
    





    def get_model_trainer(self) -> modeltrainerconfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        create_directories([config.root_dir])    
        schema  = self.schema.TARGET_COLUMN


        modeltrainer_config = modeltrainerconfig(

            root_dir =  config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path , 
            model_name =  config.model_name ,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name

        )

        return modeltrainer_config   
    

    def get_model_evaluation_config(self) -> modelevaluationconfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        create_directories([config.root_dir])    
        schema  = self.schema.TARGET_COLUMN


        modelevaluation_config = modelevaluationconfig(

            root_dir =  config.root_dir,
            
            test_data_path = config.test_data_path , 
            model_path =  config.model_path ,
            all_params = params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri = 'https://dagshub.com/satwiksahoojob/data_science_project.mlflow' 

        )

        return modelevaluation_config           
