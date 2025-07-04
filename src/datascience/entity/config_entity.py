from dataclasses import dataclass
from pathlib import Path

@dataclass

class data_ingestion_config:
    root_dir : Path
    source_url : str
    local_data_file : str
    unzip_dir : Path



@dataclass
class DataValidationConfig:

    root_dir:Path
    STATUS_FILE : str
    unzip_data_dir : Path
    all_schema : dict



@dataclass
class dataTransformationConfig:
    root_dir : Path
    data_path : Path



@dataclass
class modeltrainerconfig:
    root_dir : Path
    train_data_path : Path
    test_data_path : Path
    model_name : str
    alpha : float
    l1_ratio : float
    target_column : str


@dataclass
class modelevaluationconfig:
    root_dir : Path
    
    test_data_path : Path
    model_path: Path
    all_params : dict
    metric_file_name : Path
    target_column : str
    mlflow_uri : str

