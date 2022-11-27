import os
import json
from Concrete_CS import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import yaml
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file {yaml_file} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"create directory at {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file is saved at {path}")
    
@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    with open(path) as f:
        content= json.load(f)
    logger.info(f"json file is loaded at {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"file is saved at {path}")
    
@ensure_annotations
def load_bin(path: Path)->Any:
    data= joblib.load(path)
    logger.info(f"file is successfully loaded at {path}")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    size_in_kb= round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"