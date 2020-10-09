import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything


def foo():
    rest = (4, 5, 6)
    t = 1, 2, 3, *rest
    return t


test = foo()
print(test)
