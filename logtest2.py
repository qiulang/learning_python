#! /usr/bin/env python3
import logging
import nclog2
import re
from datetime import datetime


def reg_test():
    ts = datetime.now().timestamp()
    print(f'{ts} -- {int(ts)}')
    s = 'if (typeof fn === \'function\') fn({ uid: user_id, ver: \'x3-x4\' })'
    s2 = re.sub(r"(?<=ver: \')(.)*(?=\')", 'a9aa', s)
    print(s2)


def main():
    # logging.basicConfig(level=logging.WARNING)
    # nclog2.foo2()
    # has = nclog2.logger.hasHandlers()
    # nclog2.logger.warning(has)
    for x in range(1, 5):
        sample_func()


def sample_func():
    # for x in range(1, 5):  # shadows name x from outer scope
    #     print(x)
    print(x)


if __name__ == "__main__":
    main()
    for x in range(1, 5):
        sample_func()
