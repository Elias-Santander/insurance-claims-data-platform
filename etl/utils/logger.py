import logging
import os

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("insurance_etl")
logger.setLevel(logging.INFO)

# ==================================================
# FORMATTER
# ==================================================

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# ==================================================
# FILE HANDLER
# ==================================================

file_handler = logging.FileHandler(
    f"{LOG_DIR}/etl.log"
)
file_handler.setFormatter(formatter)

# ==================================================
# CONSOLE HANDLER
# ==================================================

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# ==================================================
# ADD HANDLERS
# ==================================================

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)