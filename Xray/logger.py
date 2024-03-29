import logging
import os

from Xray.constant.training_pipeline import TIMESTAMP  # Importing TIMESTAMP constant from training_pipeline module

# Defining the name of the log file using the TIMESTAMP constant
LOG_FILE: str = f"{TIMESTAMP}.log"

# Creating a path for the logs directory using the current working directory and the TIMESTAMP constant
logs_path = os.path.join(os.getcwd(), "logs", TIMESTAMP)

# Creating the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Creating the full file path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module with the specified settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Setting the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Setting the log format
    level=logging.INFO,  # Setting the log level to INFO
)
