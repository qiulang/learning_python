#查找某一特定数字在排好序的列表中的索引位置
import math
alist=[1,2,3,4,6,8,9,13,15,18,21,24]
key=int(input('the number we want:'))
buttom=0
cursor=int(len(alist)/2)
loop=0
while loop<math.log(len(alist),2):#循环条件保证如果输入不在alist中的数字避免死循环
    if alist[cursor] < key :
        buttom=cursor
        cursor=int((len(alist)-cursor)/2+cursor)
    if alist[cursor] > key :
        cursor=int((cursor+buttom)/2)
    if alist[cursor] == key:
        print(cursor)
        break
    loop+=1
else:
    print("not in alist")