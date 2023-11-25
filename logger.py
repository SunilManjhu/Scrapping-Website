import logging
from logging.handlers import RotatingFileHandler
import datetime

def setup_logger(log_file="app.log"):
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    # If this module is run as a standalone script, configure the logger
    log_filename = f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    setup_logger(log_file=log_filename)
