# mathmodule.py
"""The simplest math module ever.

You can use two functions:
>>> add(2, 5.01)
7.01
>>> multiply(2, 5.01)
10.02
"""


def add(x, y):
    """Add two values.

    >>> add(1, 1)
    2
    >>> add(-1.0001, 1.0001)
    0.0
    """
    return x + y


def multiply(x, y):
    """Multiple two values.

    >>> multiply(1, 1)
    1
    >>> multiply(-1, 1)
    -1
    """
    return x * y


if __name__ == "__main__":
    import doctest

    doctest.testmod()