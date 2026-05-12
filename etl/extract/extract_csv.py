import pandas as pd
from etl.utils.logger import logger


def extract_csv(file_path):
    try:
        logger.info(f"Reading file: {file_path}")
        df = pd.read_csv(file_path)
        logger.info(
            f"File loaded successfully: {file_path}"
        )
        return df

    except Exception as e:
        logger.error(
            f"Error reading {file_path}: {str(e)}"
        )
        raise