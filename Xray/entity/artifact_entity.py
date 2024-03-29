from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader


# Data Ingestion Artifact
@dataclass
class DataIngestionArtifact:
    train_file_path: str  # File path for the training data
    test_file_path: str  # File path for the test data


# Data Transformation Artifact
@dataclass
class DataTransformationArtifact:
    transformed_train_object: DataLoader  # DataLoader object for transformed training data
    transformed_test_object: DataLoader  # DataLoader object for transformed test data
    train_transform_file_path: str  # File path for storing train transforms
    test_transform_file_path: str  # File path for storing test transforms


# Model Trainer Artifact
@dataclass
class ModelTrainerArtifact:
    trained_model_path: str  # File path for the trained model


# Model Evaluation Artifact
@dataclass
class ModelEvaluationArtifact:
    model_accuracy: float  # Accuracy of the trained model


# Model Pusher Artifact
@dataclass
class ModelPusherArtifact:
    bentoml_model_name: str  # Name of the BentoML model
    bentoml_service_name: str  # Name of the BentoML service
