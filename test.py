test = [1, 2, 3, 4, 5, 6, 7, 8]
t = test[1::-1]
print(t)
print(test[1])
t = test[:-3:-1]
print(t)
print(test[-3])


pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(pitchers)
print(first_names)


exit(0)
a = int(input("input your number: \n"))
s = 1
if a == 2:
    print('yes')
    exit(0)
for i in range(2, a+1):
    if a % i == 0:
        print(i)
        break
if i == a:
    print('yes')
else:
    print('no')
