import logging
def test_loggingdemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    logger.addHandler(filehandler)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)

    logger.debug("debugging")
    logger.info("information")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
