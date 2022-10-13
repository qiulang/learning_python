#! /usr/bin/env python3
import logging
import nclog2
import re
from datetime import datetime
import sys


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
    # for x in range(1, 5):
    #     sample_func()
    a = ("wsclient", "ccfront", 'wsserver')
    b = ("bv4", "cv4", "wv4")
    d = dict(zip(a, b))
    print(d)
    return False, None


def sample_func():
    # for x in range(1, 5):  # shadows name x from outer scope
    #     print(x)
    print(x)


if __name__ == "__main__":
    result, r2 = main()
    # for x in range(1, 5):
    #     sample_func()

    print(r2)
    print(sys.version_info)
