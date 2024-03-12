import inspect
import logging
class baseclass:
    def getlogger(self):
        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        return logger