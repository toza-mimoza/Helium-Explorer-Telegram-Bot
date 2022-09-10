# encoding: utf-8
import os
import logging
from definitions import LOGS_DIR

def init_logger(logfile: str):
    """! Initialize the root logger and standard log handlers."""
    # check if logs directory exists, if not create it
    
    if not os.path.exists(LOGS_DIR):
        os.mkdir(LOGS_DIR)

    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)