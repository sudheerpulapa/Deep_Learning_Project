import sys  # Importing the sys module to access system-specific parameters and functions

# Importing specific modules and classes from Xray package
from Xray.cloud_storage.s3_operation import S3Operation
from Xray.constant.training_pipeline import *
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging  # Importing the logging module from Xray package


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        # Initializing the DataIngestion class with a DataIngestionConfig object
        self.data_ingestion_config = data_ingestion_config

        # Creating an instance of the S3Operation class from Xray package
        self.s3 = S3Operation()

    def get_data_from_s3(self) -> None:
        try:
            # Logging a message to indicate entry into the get_data_from_s3 method
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")

            # Synchronizing a folder from S3 to local based on configuration parameters
            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
            )

            # Logging a message to indicate exit from the get_data_from_s3 method
            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            # Raising an XRayException if any error occurs during S3 data retrieval
            raise XRayException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        # Logging a message to indicate entry into the initiate_data_ingestion method
        logging.info(
            "Entered the initiate_data_ingestion method of Data ingestion class"
        )

        try:
            # Calling the get_data_from_s3 method to retrieve data from S3
            self.get_data_from_s3()

            # Creating a DataIngestionArtifact object with train and test file paths
            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path,
            )

            # Logging a message to indicate exit from the initiate_data_ingestion method
            logging.info(
                "Exited the initiate_data_ingestion method of Data ingestion class"
            )

            return data_ingestion_artifact  # Returning the DataIngestionArtifact object

        except Exception as e:
            # Raising an XRayException if any error occurs during data ingestion
            raise XRayException(e, sys)
