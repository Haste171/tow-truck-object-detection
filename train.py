import logging
from ultralytics import YOLO
from config import get_model_config
from clearml import Task

logger = logging.getLogger(__name__)
logger.propagate = True

def train_model(
    dataset_path: str,
    model_size: str = "medium",
    name: str = "yolov8m_tow_truck_detector",
    clear_ml_name: str = "Tow Truck Detection",
    patience: int = 5
):
    """
    Trains a YOLO model for tow truck detection.

    Args:
        dataset_path (str): Path to the dataset used for training.
        model_size (str, optional): Size of the YOLO model to use. Defaults to "medium".
        name (str, optional): Name for the trained model. Defaults to "yolov8m_tow_truck_detector".
        clear_ml_name (str, optional): Name of the ClearML project. Defaults to "Tow Truck Detection".
        patience (int, optional): Number of epochs with no improvement after which training will be stopped. Defaults to 5.

    Returns:
        None
    """
    logger.info(f"Starting training with model size: {model_size}")
    model_config = get_model_config(model_size)

    task = Task.init(project_name=clear_ml_name, task_name=model_config["task_name"])

    model = YOLO(model_config["model"])
    model.train(
        data=dataset_path,
        epochs=model_config["epochs"],
        imgsz=640,
        batch=model_config["batch"],
        name=name,
        project=clear_ml_name,
        verbose=True,
        exist_ok=True,
        patience=patience 
    )

    logger.info(f"Training completed for {model_size} model. Task closed.")
    task.close()
