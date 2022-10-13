s = 'hi'
s1 = s.center(9,'-')
# center(center(s, i), j) = center(s, j)
s2 = s1.center(20,'-')

print(f'{s1} : {s2}')