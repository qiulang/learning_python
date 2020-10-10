import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

import clog
import nclog
import nclog2


def main():
    # logging.basicConfig(level=logging.DEBUG)
    # clog.clog_test()
    nclog.foo()
    nclog2.foo2()


if __name__ == "__main__":
    main()
