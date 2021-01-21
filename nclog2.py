import logging
# import coloredlogs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s : %(message)s"
# coloredlogs.install(level='DEBUG', logger=logger, fmt=LOG_FORMAT)


def foo2():
    logger.info('Try info level log message')
    logger.warning(
        f'Try warning level log message, do I have handler {logger.hasHandlers()}')


foo2()
