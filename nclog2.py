import logging
import coloredlogs

logger = logging.getLogger(__name__)
LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s : %(message)s"
coloredlogs.install(level='DEBUG', logger=logger, fmt=LOG_FORMAT)
# logger.setLevel(logging.DEBUG)


def foo2():
    logger.info('Try different log message')
