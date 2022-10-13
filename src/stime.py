import os

with os.scandir('.') as dir_entries:
    for entry in dir_entries:
        info = entry.stat()
        print(f"{entry.name} : {info.st_mtime}")


def test(*args, **kargs):
    print(args)
    print(kargs)
    print(args[0])
    print(kargs.get('a'))


alpha = 'alpha'
beta = 'beta'
test(alpha, beta, a=1, b=2)

var_one = 123


def func_one(var_one):
    var_one = 234
    var_three = 'abc'


var_two = 456


def func_two():
    var_four = 123
    print(dir())


func_two()

variable1 = 1
variable2 = "abc"
variable3 = (1, 2)
variable4 = ['a', 1]
# Print their Ids
print('Variable1: ', id(variable1))
print('Variable2: ', id(variable2))
print('Variable3: ', id(variable3))
print('Variable4: ', id(variable4))
