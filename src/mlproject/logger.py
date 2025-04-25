import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Log directory and full path
logs_path = os.path.join(os.getcwd(), "logs")
log_file_path = os.path.join(logs_path, LOG_FILE)

# Create directory
os.makedirs(logs_path, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Create console handler for real-time logs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

# Add the console handler to the logger
logging.getLogger().addHandler(console_handler)

# Create and export logger object
logger = logging.getLogger(__name__)
