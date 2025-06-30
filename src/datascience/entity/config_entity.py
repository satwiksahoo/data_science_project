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
