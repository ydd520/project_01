# -*- coding: utf-8 -*-
import logging.config
import os



class Log(object):
    log_path = "Logger.conf"
    fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)),log_path)
    print (fileName)
    logging.config.fileConfig(fileName)
    logger = logging.getLogger('root')
    logger.disabled = False

    def info(logMessage):
        Log.logger.info(logMessage)

    def debug(logMessage):
        Log.logger.debug(logMessage)

    def warning(logMessage):
        Log.logger.warning(logMessage)






















