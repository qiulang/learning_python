#! /usr/bin/env python3
def foo(param1, *param2):
    print(param1)
    print(param2)


def bar(param1, **param2):
    print(param1)
    print(param2)


def three_params(param1, *param2, **param3):
    print(param1)
    print(param2)
    print(param3)


def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args:  # If args is not empty.
        print(args)

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs:  # If kwargs is not empty.
        print(kwargs)


print(foo(1, 2, 3, 4, 5))
print("\n")
# print(bar(1, a=2, b=3))
bar(1, a=2, b=3)
print("\n")
print(three_params(1, 2, 3, 4, s=5))

# func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")

func("required argument", 1, 2, '3')
