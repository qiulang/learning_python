#! /usr/bin/env python3
import logging
import nclog2
import re


def main():
    # logging.basicConfig(level=logging.WARNING)
    # nclog2.foo2()
    # has = nclog2.logger.hasHandlers()
    # nclog2.logger.warning(has)
    s = 'if (typeof fn === \'function\') fn({ uid: user_id, ver: \'x3x4\' })'
    s2 = re.sub(r"(?<=ver: \')(\w){5}", 'a9aa', s)
    print(s2)


if __name__ == "__main__":
    main()
