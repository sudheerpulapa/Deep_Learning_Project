import os
import sys

# Function to generate detailed error message
def error_message_detail(error: Exception, error_detail: sys) -> str:
    # Get traceback information
    _, _, exc_tb = error_detail.exc_info()

    # Extract file name from traceback
    file_name: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    # Construct detailed error message
    error_message: str = "Error occurred in Python script '{0}' at line number '{1}' with message: '{2}'".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class XRayException(Exception):
    def __init__(self, error_message, error_detail):
        """
        XRayException class to handle exceptions with detailed error messages.
        
        :param error_message: Error message in string format
        :param error_detail: Details of the error provided by sys module
        """
        super().__init__(error_message)

        # Generate detailed error message using the provided error details
        self.error_message: str = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Return the detailed error message
        return self.error_message
