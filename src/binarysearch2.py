#查找某一特定数字在排好序的列表中的索引位置
import math
alist=[1,2,3,4,6,8,9,13,15,18,21,24]
key=int(input('the number we want:'))
left = 0
right = len(alist) - 1

while left <= right:
    mid = (left + right) // 2

    if alist[mid] == key:
        print(mid)
        break
    elif alist[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("not in alist")