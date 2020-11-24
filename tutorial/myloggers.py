import logging
import logging.config
import traceback

def mylogger():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("{}".format(__name__))
    return logger

