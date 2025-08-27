import logging
from logging import getLogger, StreamHandler, basicConfig
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = getLogger(__name__)
    FORMAT = '%(asctime)s - %(filename)s: - %(name)s - %(levelname)s - %(message)s'

    file_handler = RotatingFileHandler(
        os.path.join(log_dir, "main.log"),
        maxBytes=1024 * 1024,
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel('DEBUG')

    stream_handler = StreamHandler()
    stream_handler.setLevel('DEBUG')

    basicConfig(
        level=logging.DEBUG,
        format=FORMAT,
        handlers=[file_handler, stream_handler]
    )
    return logger

logger = setup_logger()