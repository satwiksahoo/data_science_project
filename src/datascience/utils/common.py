import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox (dict-like) object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Parsed YAML file content.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            print(f"[DEBUG] Trying to load YAML from: {path_to_yaml} | Exists: {os.path.exists(path_to_yaml)}")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not structured properly.")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they dont exist.

    Args:
        paths (list[Path]): List of directories to create.
        verbose (bool, optional): Whether to log creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
                logger.info(f"Directory created at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to save JSON.
        data (dict): Data to store.
    """
   
    with open(path, "w") as f:
         json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns as a ConfigBox.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: JSON content.
    """
    
    with open(path) as f:
            content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)



@ensure_annotations
def save_joblib(path: Path, obj: Any):
    """
    Saves a Python object using joblib.

    Args:
        path (Path): Path to save the object.
        obj (Any): Python object (e.g., model) to be saved.
    """
    joblib.dump(obj, path)
    logger.info(f"Object saved using joblib at: {path}")
  


@ensure_annotations
def load_joblib(path: Path) -> Any:
    """
    Loads an object saved with joblib.

    Args:
        path (Path): Path to the saved joblib object.

    Returns:
        Any: Loaded object.
    """
    obj = joblib.load(path)
    logger.info(f"Object loaded from: {path}")
    return obj
   

  