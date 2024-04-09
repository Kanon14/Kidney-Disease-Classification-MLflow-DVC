import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.
    
    Args:
        path_to_yaml (Path): The path to the YAML file.
        
    Raises:
        ValueError: If yaml file is empty or malformed
        e: empty file
        
    Returns:
        ConfigBox: A ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories
    
    Args:
        path_to_directories (list): The list of directories to be created.
        verbose (bool, optional): Whether to print the directory creation messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")
            

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a JSON file
    
    Args:
        path (Path): The path to the JSON file.
        data (dict): The data to be saved.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logger.info(f"JSON file: {path} saved successfully")
        

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return a ConfigBox object.
    
    Args:
        path (Path): The path to the JSON file.
        
    Returns:
        ConfigBox: A ConfigBox object
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"JSON file: {path} loaded successfully")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file
    
    Args:
        data (Any): The data to be saved
        path (Path): The path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file
    
    Args:
        path (Path): The path to the binary file
    
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file
    
    Args:
        path (Path): The path to the file
        
    Returns:
        str: The size of the file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    img = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(img)
        f.close()
        

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
        