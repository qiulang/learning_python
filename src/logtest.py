#! /usr/bin/env python3
import logging
import coloredlogs
from subprocess import PIPE, run

# logging.basicConfig(level=logging.DEBUG)
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

import clog
import nclog
import nclog2

logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"


def setup_root_logger():
    # coloredlogs.install(level='DEBUG')
    # logging.basicConfig(level='INFO', format=FORMAT)
    logging.basicConfig(level='DEBUG')
    info_handler = logging.FileHandler('file-log')
    info_handler.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter(
        '{name} - {funcName} - {lineno} - {message}', style="{")
    f_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console.setFormatter(c_format)
    info_handler.setFormatter(f_format)
    # logger = logging.getLogger('')
    logger.addHandler(console)
    logger.addHandler(info_handler)


def run_test():
    result = run(['npm', 'show', 'jssip-emicnet', 'version'],
                 stdout=PIPE, stderr=PIPE)
    output = result.stdout.decode('utf-8')
    logger.info('npm show jssip-emicnet version')
    logger.info(f'{output}')


def main():
    # logging.basicConfig()
    setup_root_logger()
    clog.clog_test()
    nclog.foo()
    nclog2.foo2()
    run_test()


if __name__ == "__main__":
    main()
