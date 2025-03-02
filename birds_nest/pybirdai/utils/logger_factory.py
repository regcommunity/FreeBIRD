import logging
from pathlib import Path

def return_logger(__file_name__:str):
    return logging.getLogger(__file_name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()
