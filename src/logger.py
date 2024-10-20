import logging
import os
from datetime import datetime
from src.exception import CustomException
import sys

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)



# # Test case in the exception.py file
# if __name__ == "__main__":

#     try:
#     # An operation that causes an error (division by zero)
#         result = 1 / 0

#     except Exception as e:
#         # Log the error message using the custom exception and the logger
#         logging.error("An error occurred")
        
#         # Raise a custom exception and log the details
#         custom_exception = CustomException(str(e), sys)
#         logging.error(custom_exception)


