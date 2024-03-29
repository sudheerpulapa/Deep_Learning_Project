import os
from dataclasses import dataclass

from torch import device

from Xray.constant.training_pipeline import *


# Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str = S3_DATA_FOLDER  # Folder in the S3 bucket containing data
        self.bucket_name: str = BUCKET_NAME  # Name of the S3 bucket
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)  # Directory for storing artifacts
        self.data_path: str = os.path.join(self.artifact_dir, "data_ingestion", self.s3_data_folder)  # Path to data folder
        self.train_data_path: str = os.path.join(self.data_path, "train")  # Path to train data
        self.test_data_path: str = os.path.join(self.data_path, "test")  # Path to test data


# Data Transformation Configuration
@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.color_jitter_transforms: dict = {
            "brightness": BRIGHTNESS,
            "contrast": CONTRAST,
            "saturation": SATURATION,
            "hue": HUE,
        }  # Parameters for color jitter transformations
        self.RESIZE: int = RESIZE  # Image resize dimension
        self.CENTERCROP: int = CENTERCROP  # Dimension for center crop
        self.RANDOMROTATION: int = RANDOMROTATION  # Angle for random rotation
        self.normalize_transforms: dict = {"mean": NORMALIZE_LIST_1, "std": NORMALIZE_LIST_2}  # Normalization parameters
        self.data_loader_params: dict = {"batch_size": BATCH_SIZE, "shuffle": SHUFFLE, "pin_memory": PIN_MEMORY}  # DataLoader parameters
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, "data_transformation")  # Directory for storing transformation artifacts
        self.train_transforms_file: str = os.path.join(self.artifact_dir, TRAIN_TRANSFORMS_FILE)  # Path to train transforms file
        self.test_transforms_file: str = os.path.join(self.artifact_dir, TEST_TRANSFORMS_FILE)  # Path to test transforms file


# Model Trainer Configuration
@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.artifact_dir: int = os.path.join(ARTIFACT_DIR, TIMESTAMP, "model_training")  # Directory for storing model training artifacts
        self.trained_bentoml_model_name: str = "xray_model"  # Name of the trained BentoML model
        self.trained_model_path: int = os.path.join(self.artifact_dir, TRAINED_MODEL_NAME)  # Path to trained model
        self.train_transforms_key: str = TRAIN_TRANSFORMS_KEY  # Key for accessing train transforms
        self.epochs: int = EPOCH  # Number of training epochs
        self.optimizer_params: dict = {"lr": 0.01, "momentum": 0.8}  # Parameters for optimizer
        self.scheduler_params: dict = {"step_size": STEP_SIZE, "gamma": GAMMA}  # Parameters for scheduler
        self.device: device = DEVICE  # Device for training


# Model Evaluation Configuration
@dataclass
class ModelEvaluationConfig:
    def __init__(self):
        self.device: device = DEVICE  # Device for evaluation
        self.test_loss: int = 0  # Placeholder for test loss
        self.test_accuracy: int = 0  # Placeholder for test accuracy
        self.total: int = 0  # Placeholder for total
        self.total_batch: int = 0  # Placeholder for total batch
        self.optimizer_params: dict = {"lr": 0.01, "momentum": 0.8}  # Parameters for optimizer


# Model Pusher Configuration
@dataclass
class ModelPusherConfig:
    def __init__(self):
        self.bentoml_model_name: str = BENTOML_MODEL_NAME  # Name of the BentoML model
        self.bentoml_service_name: str = BENTOML_SERVICE_NAME  # Name of the BentoML service
        self.train_transforms_key: str = TRAIN_TRANSFORMS_KEY  # Key for accessing train transforms
        self.bentoml_ecr_image: str = BENTOML_ECR_URI  # URI for BentoML ECR image
