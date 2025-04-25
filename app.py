
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


from src.mlproject.logger import logging  # ✅ Use `logging`, not `logger` unless you've defined `logger` separately
from src.mlproject.exception import CustomException

from src.mlproject.component.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Initialize and start the data ingestion process
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom exception occurred during ingestion.")
        raise CustomException(e, sys)
