import os
import yaml
from src.winequal_mlops_pipeline import logger
import json

import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError as e:
        logger.error(f"Error occurred while reading yaml file: {e}")
        raise ValueError(f"Error occurred while reading yaml file: {e}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.
    Args:
        path_to_directories (list): List of directories to be created.
        verbose (bool, optional): If True, logs the directories being created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.
    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to be saved as a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns a ConfigBox object.
    Args:
        path (Path): Path to the JSON file.
    Returns:
        ConfigBox: ConfigBox object containing the JSON data.
        """
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves a binary file.
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> str:
    """
    Loads a binary file.

    Args:
        path (Path): Path to the binary file.
    Returns:
        str: Loaded data from the binary file.
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary file loaded from: {path}")
    return data








    