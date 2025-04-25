import os
import sys
from src.mlproject.exception import CustomException  # ✅ Fix: corrected import syntax
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine  # ✅ Fix: import SQLAlchemy

# Load environment variables
load_dotenv()

# Read credentials from .env
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")  # ✅ Fix: previously you used host again by mistake
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started.")
    try:
        # Create SQLAlchemy engine
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

        logging.info("Connection established successfully.")

        # Query the table
        df = pd.read_sql_query("SELECT * FROM students", engine)  # ✅ Fix: using engine instead of pymysql connection
        logging.info(f"Data fetched successfully. Shape: {df.shape}")
        
        return df

    except Exception as ex:
        raise CustomException(ex, sys)  # ✅ Fix: missing sys argument
