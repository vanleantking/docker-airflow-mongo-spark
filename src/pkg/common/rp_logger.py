import logging
import logging.handlers as handlers
import os


def set_up_logger(name, path):
    """
    return logger for log debug [fb, dv360]
    Args:
        name:
        path:

    Returns:

    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    formatter = '%(asctime)s - %(levelname)s: %(message)s'
    logging.basicConfig(
        filename=path,
        filemode='a',
        level=logging.DEBUG,
        format=formatter)
    # add hanlder split by date
    loghandler = handlers.TimedRotatingFileHandler(
        filename=path,
        when="midnight",
        backupCount=30,
        interval=1)
    logger = logging.getLogger(name)
    logger.addHandler(loghandler)
    return logger


def get_logger(name):
    return logging.getLogger(name)
