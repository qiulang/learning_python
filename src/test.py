test = [1, 2, 3, 4, 5, 6, 7, 8]
t = test[1::-1]
print(t)
print(test[1])
t = test[:-3:-1]
print(t)
print(test[-3])


pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)

# a = int(input("input your number: \n"))
# s = 1
# if a == 2:
#     print('yes')
#     exit(0)
# for i in range(2, a+1):
#     if a % i == 0:
#         print(i)
#         break
# if i == a:
#     print('yes')
# else:
#     print('no')
max, *t2 = (4, 2, 3, 1, 5, -2)
ii, ia, min = 0, 0, max
# the index is used as an offset, tells the distance from the starting element
for index, tmp in enumerate(t2):
    if tmp > max:
        max, ia = tmp, index+1
    if tmp < min:
        min, ii = tmp, index+1
print(max, ia)
print(min, ii)

max, *t2 = (4,)
print(t2)
t2 = 'you '.split()
print(t2)

a = (3, 5, 7, 1, 4, 546, 43)
s = sum(a)
avg = s/len(a)
print(f'sum:{s}, avg:{avg}')

tt = """
    qiu
    lang
"""

tt2 = """qiu
    lang
"""
print(tt, tt2)

t3 = 'qq' 'ee' 'ttt' 'rteet'
t4 = ['qq', 'ee']
print(t3)
print(t4)
