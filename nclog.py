import logging
import coloredlogs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s : %(message)s"
# coloredlogs.install(level='DEBUG', logger=logger, fmt=LOG_FORMAT)


def foo():
    rest = (4, 5, 6)
    t = 1, 2, 3, *rest
    logger.info(t)
    return t


# test = foo()
# print(test)
