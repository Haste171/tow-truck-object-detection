import logging
import argparse
from train import train_model

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("MainLogger")

logger = setup_logging()

def parse_args():
    parser = argparse.ArgumentParser(description="YOLO model operations: training, inference, etc.")
    parser.add_argument("task", type=str, choices=["train", "infer"], help="Task to perform: train or infer.")
    parser.add_argument("--dataset", type=str, help="Path to the dataset (required for training).")
    parser.add_argument("--model_size", type=str, choices=["small", "medium", "large", "xlarge"], default="medium", help="Size of the YOLO model (for training).")
    parser.add_argument("--name", type=str, default="yolov8m_tow_truck_detector", help="Name for the trained model.")
    parser.add_argument("--clear_ml_name", type=str, default="Tow Truck Detection", help="Name of the ClearML project.")
    parser.add_argument("--patience", type=int, default=5, help="Number of epochs with no improvement before stopping training.")
    parser.add_argument("--image", type=str, help="Path to image for inference.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    if args.task == "train":
        if not args.dataset:
            logger.error("--dataset is required for training.")
            raise ValueError("--dataset is required for training.")
        logger.info("Starting training...")
        train_model(
            dataset_path=args.dataset,
            model_size=args.model_size,
            name=args.name,
            clear_ml_name=args.clear_ml_name,
            patience=args.patience
        )
    elif args.task == "infer":
        if not args.image:
            logger.error("--image is required for inference.")
            raise ValueError("--image is required for inference.")
        logger.info(f"Running inference on image: {args.image}")
        # TODO: Placeholder for inference function
        logger.info(f"Running inference on image: {args.image}")
