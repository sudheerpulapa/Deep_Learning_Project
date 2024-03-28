import os
import sys
from Xray.exception import XRayException

class S3Operation:
    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        Syncs a local folder to a specified S3 bucket.

        Args:
            folder (str): Path to the local folder to sync.
            bucket_name (str): Name of the target S3 bucket.
            bucket_folder_name (str): Name of the folder within the bucket.

        Raises:
            XRayException: If there's an error during the synchronization process.
        """
        try:
            # Construct the command for syncing local folder to S3
            command: str = (
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/"
            )

            # Execute the command using os.system
            os.system(command)

        except Exception as e:
            # If any exception occurs, raise XRayException
            raise XRayException(e, sys)

    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        Syncs a folder from a specified S3 bucket to the local machine.

        Args:
            folder (str): Path to the local folder where the S3 contents will be synced.
            bucket_name (str): Name of the source S3 bucket.
            bucket_folder_name (str): Name of the folder within the bucket.

        Raises:
            XRayException: If there's an error during the synchronization process.
        """
        try:
            # Construct the command for syncing S3 folder to local machine
            command: str = (
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}"
            )

            # Execute the command using os.system
            os.system(command)

        except Exception as e:
            # If any exception occurs, raise XRayException
            raise XRayException(e, sys)
