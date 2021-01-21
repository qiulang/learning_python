#! /usr/bin/env python3
import logging
import nclog2


def main():
    # logging.basicConfig(level=logging.WARNING)
    nclog2.foo2()
    has = nclog2.logger.hasHandlers()
    nclog2.logger.warning(has)


if __name__ == "__main__":
    main()
