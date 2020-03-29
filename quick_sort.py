def partition(sub):
    pivot = sub[-1]
    sub2 = sub[:-1]
    index = len(sub)-1
    # for i, val in enumerate(sub2):
    for val in sub2:
        if val > pivot:
            # del sub() 算法不对，先用remove
            sub.remove(val)
            sub = sub+[val]
            index -= 1
    return (index, sub)


def quick_sort(array):
    print(f"quick sort {array}")
    tmp = len(array)
    if tmp <= 1:
        return array
    (pivot, arr) = partition(array)
    print(f"partition {pivot}, {arr}")
    if (tmp <= 3):
        return arr
    # 三个以上元素
    if (pivot >= 2):
        left = quick_sort(arr[:pivot])
    else:
        left = arr[:pivot]
    if (pivot < len(arr)-2):
        right = quick_sort(arr[pivot+1:])
    else:
        right = arr[pivot+1:]
    a2 = left + [arr[pivot]] + right
    print(f"combine left: {left} & rigth:{right} => {a2}")
    return a2
    # quick_sort(array[:pivot])
    # quick_sort(array[pivot+1:])
    # https://stackoverflow.com/questions/18262306/quicksort-with-python


ar = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
a1 = quick_sort(ar)
print(a1)
