import logging
from typing import Dict, Literal

logger = logging.getLogger(__name__)
logger.propagate = True

def get_model_config(model_size: Literal["small", "medium", "large", "xlarge"]) -> Dict:
    """
    Retrieves the YOLO model configuration based on the specified model size.
    Args:
        model_size (Literal["small", "medium", "large", "xlarge"]): The size of the YOLO model to retrieve the configuration for.
    Returns:
        Dict: A dictionary containing the configuration parameters for the specified YOLO model size.
    Raises:
        ValueError: If an invalid model_size is provided.
    The function returns a dictionary with the following keys:
        - model: The model file name.
        - epochs: The number of training epochs.
        - batch: The batch size for training.
        - task_name: A descriptive name for the training task.

    Specific configurations for each model size:
    - small:
        {
            "model": "yolov8s.pt",
            "epochs": 100,
            "batch": 64,
            "task_name": "YOLOv8s Training"
        }
    - medium:
        {
            "model": "yolov8m.pt",
            "epochs": 200,
            "batch": 32,
            "task_name": "YOLOv8m Training"
        }
    - large:
        {
            "model": "yolov8l.pt",
            "epochs": 400,
            "batch": 16,
            "task_name": "YOLOv8l Training"
        }
    - xlarge:
        {
            "model": "yolov8x.pt",
            "epochs": 400,
            "batch": 8,
            "task_name": "YOLOv8xl Training"
        }
    """
    yolo_configs = {
        "small": {
            "model": "yolov8s.pt",
            "epochs": 100,
            "batch": 64,
            "task_name": "YOLOv8s Training"
        },
        "medium": {
            "model": "yolov8m.pt",
            "epochs": 200,
            "batch": 32,
            "task_name": "YOLOv8m Training"
        },
        "large": {
            "model": "yolov8l.pt",
            "epochs": 400,
            "batch": 16,
            "task_name": "YOLOv8l Training"
        },
        "xlarge": {
            "model": "yolov8x.pt",
            "epochs": 400,
            "batch": 8,           
            "task_name": "YOLOv8xl Training"
        }
    }
    config = yolo_configs.get(model_size)
    if config:
        logger.info(f"Using config {model_size}:\n{config}")
        return config
    else:
        raise ValueError("Invalid model_size input!")